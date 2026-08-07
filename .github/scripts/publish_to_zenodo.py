# Based on examples on https://developers.zenodo.org/

import json
import os
import requests
import yaml

ACCESS_TOKEN = os.environ["ZENODO_TOKEN"]
CONCEPT_ID = os.environ["ZENODO_CONCEPT_ID"]

print(CONCEPT_ID)
print(ACCESS_TOKEN)

BASE_URL = "https://zenodo.org/api"

TITLE_SUFFIX = " - CodeRefinery lesson"


json_headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

upload_headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

def load_metadata():
    with open("metadata.yml", encoding="utf-8") as f:
        return yaml.safe_load(f)


def authors_to_creators(authors):
    creators = []

    for author in authors:
        if "family-names" in author:
            creator = {
                "name": (
                    f"{author['family-names']}, "
                    f"{author['given-names']}"
                )
            }
        else:
            creator = {"name": author["name"]}

        if author.get("orcid"):
            creator["orcid"] = author["orcid"].removeprefix("https://orcid.org/")

        creators.append(creator)

    return creators



# Load metadata from metadata.yml

meta = load_metadata()

description = meta.get("abstract", "")

if meta.get("repository-code"):
    description += (
        f'<br><p>Source code: '
        f'<a href="{meta["repository-code"]}">{meta["repository-code"]}</a></p>'
    )

if meta.get("url"):
    description += (
        f'<br><p>Lesson website: '
        f'<a href="{meta["url"]}">{meta["url"]}</a></p>'
    )

description += (
    '<br><p>CodeRefinery website: '
    '<a href="https://coderefinery.org">https://coderefinery.org</a></p>'
)

metadata = {
    "title": meta["title"] + TITLE_SUFFIX,
    "upload_type": "lesson",
    "description": description,
    "creators": authors_to_creators(meta["authors"]),
    "keywords": meta.get("keywords", []),
    "version": meta.get("version"),
    "license": meta.get("license"),
}

if meta.get("maintainers"):
    contributors = authors_to_creators(meta["maintainers"])
    for contributor in contributors:
        contributor["type"] = "ContactPerson"
    metadata["contributors"] = contributors


# Discard any unpublished draft left over from a previous failed run.
# Zenodo only allows one unpublished new-version draft per concept at
# a time, so a stray one would make the newversion call below fail.

r = requests.get(
    f"{BASE_URL}/deposit/depositions",
    params={"q": f"conceptrecid:{CONCEPT_ID}", "all_versions": "true"},
    headers=json_headers,
)

r.raise_for_status()

for dep in r.json():
    if not dep.get("submitted"):
        print(f"Discarding leftover draft {dep['id']}")
        requests.delete(dep["links"]["self"], headers=json_headers).raise_for_status()


# Find the current latest version of this concept.
# newversion only works when called on the latest version's own
# deposit ID, and that ID changes with every new release.

r = requests.get(
    f"{BASE_URL}/records",
    params={"q": f"conceptrecid:{CONCEPT_ID}", "all_versions": "true"},
    headers=json_headers,
)

r.raise_for_status()

hits = r.json()["hits"]["hits"]

latest_id = hits[0]["id"]
for hit in hits[1:]:
    if hit["id"] > latest_id:
        latest_id = hit["id"]

print(f"Latest existing version: {latest_id}")


# Create new version of existing concept DOI

r = requests.post(
    f"{BASE_URL}/deposit/depositions/{latest_id}/actions/newversion",
    headers=json_headers)

r.raise_for_status()

latest_draft = r.json()["links"]["latest_draft"]


# Get draft deposition information

r = requests.get(
    latest_draft,
    headers=json_headers,
)

r.raise_for_status()

deposition = r.json()

deposition_id = deposition["id"]
bucket_url = deposition["links"]["bucket"]

print(f"Draft deposition: {deposition_id}")


# newversion copies over the previous version's files. Remove them so
# this version ends up with only its own zip and PDF.

for f in deposition.get("files", []):
    requests.delete(
        f"{BASE_URL}/deposit/depositions/{deposition_id}/files/{f['id']}",
        headers=json_headers,
    ).raise_for_status()

    print(f"Removed inherited file {f['filename']}")

# Upload lesson PDF from the gh-pages branch
# (built by sphinx.yml as OUTPUT_BASENAME.pdf, OUTPUT_BASENAME being
# "{owner}-{repo}")

tag = os.environ["GITHUB_REF_NAME"]
repo_name = os.environ['GITHUB_REPOSITORY']
owner, repo = repo_name.split("/", 1)

pdf_source_name = f"{owner}-{repo}.pdf"
pdf_name = f"{owner}-{repo}-{tag}.pdf"

pdf_url = (
    f"https://raw.githubusercontent.com/"
    f"{repo_name}/gh-pages/{pdf_source_name}"
)

pdf_download = requests.get(pdf_url)
pdf_download.raise_for_status()

with open(pdf_name, "wb") as fp:
    fp.write(pdf_download.content)

with open(pdf_name, "rb") as fp:
    r = requests.put(
        f"{bucket_url}/{pdf_name}",
        data=fp,
        headers=upload_headers
    )

r.raise_for_status()

print(f"Uploaded {pdf_name}")

# Upload release archive


archive_url = (
    f"https://github.com/"
    f"{repo_name}"
    f"/archive/refs/tags/{tag}.zip"
)

archive_name = f"{owner}-{repo}-{tag}.zip"

download = requests.get(archive_url)
download.raise_for_status()

with open(archive_name, "wb") as fp:
    fp.write(download.content)

with open(archive_name, "rb") as fp:
    r = requests.put(
        f"{bucket_url}/{archive_name}",
        data=fp,
        headers=upload_headers
    )

r.raise_for_status()

print(f"Uploaded {archive_name}")


# Update metadata

data = {
    "metadata": metadata
}

r = requests.put(
    f"{BASE_URL}/deposit/depositions/{deposition_id}",
    data=json.dumps(data),
    headers=json_headers
)

r.raise_for_status()

print("Metadata updated")


# Publish


r = requests.post(
    f"{BASE_URL}/deposit/depositions/{deposition_id}/actions/publish",
    headers=json_headers,
)

r.raise_for_status()

record = r.json()

print(f"Published DOI: {record.get('doi')}")
print(f"Record URL: {record['links']['html']}")
