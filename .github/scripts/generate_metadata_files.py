"""Generate CITATION.cff and bioschemas.yml from metadata.yml."""

import json

import yaml

METADATA_FILE = "metadata.yml"
CITATION_FILE = "CITATION.cff"
BIOSCHEMAS_FILE = "bioschemas.yml"

TITLE_SUFFIX = " - CodeRefinery lesson"

SPDX_LICENSE_URLS = {
    "CC-BY-4.0": "https://creativecommons.org/licenses/by/4.0/",
}


def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def license_url(spdx_id):
    return SPDX_LICENSE_URLS.get(spdx_id, spdx_id)


def bioschemas_authors(authors):
    result = []
    for author in authors:
        if "family-names" in author:
            result.append(
                {
                    "@type": "Person",
                    "name": f"{author['given-names']} {author['family-names']}",
                }
            )
        else:
            result.append({"@type": "Organization", "name": author["name"]})
    return result


def write_citation_cff(meta):
    citation = {
        "cff-version": "1.2.0",
        "message": (
            "If you use this lesson material, please cite it using "
            "these metadata."
        ),
        "authors": meta["authors"],
        "title": meta["title"] + TITLE_SUFFIX,
        "type": "dataset",
        "abstract": meta.get("abstract", ""),
        "version": meta["version"],
        "doi": meta["doi"],
        "date-released": meta["version"],
        "url": meta["url"],
        "license": meta["license"],
        "repository-code": meta["repository-code"],
    }

    if meta.get("maintainers"):
        citation["contact"] = meta["maintainers"]

    with open(CITATION_FILE, "w", encoding="utf-8") as f:
        yaml.safe_dump(citation, f, sort_keys=False, allow_unicode=True)


def write_bioschemas(meta):
    bioschemas = {
        "@context": "https://schema.org/",
        "@type": "LearningResource",
        "@id": meta["url"],
        "description": meta.get("abstract", ""),
        "keywords": ", ".join(meta.get("keywords", [])),
        "name": meta["title"] + TITLE_SUFFIX,
        "author": bioschemas_authors(meta["authors"]),
        # Disabled for now.
        # "maintainer": bioschemas_authors(meta.get("maintainers", [])),
        "about": meta.get("abstract", ""),
        "audience": meta.get("audience", ""),
        "competencyRequired": meta.get("competencyRequired", ""),
        "educationalLevel": meta.get("educationalLevel", ""),
        "identifier": f"https://doi.org/{meta['doi']}",
        "inLanguage": meta.get("inLanguage", ""),
        "learningResourceType": meta.get("learningResourceType", ""),
        "license": license_url(meta["license"]),
        "teaches": meta.get("teaches", ""),
        "url": meta["url"],
        "accessibilitySummary": meta.get("accessibilitySummary", ""),
        "isPartOf": meta.get("isPartOf", ""),
        "version": meta["version"],
    }

    with open(BIOSCHEMAS_FILE, "w", encoding="utf-8") as f:
        json.dump(bioschemas, f, indent=4)
        f.write("\n")


def main():
    meta = load_yaml(METADATA_FILE)
    write_citation_cff(meta)
    write_bioschemas(meta)


if __name__ == "__main__":
    main()
