"""Sphinx directive that renders metadata.yml as a table."""

import os

import yaml
from docutils import nodes
from docutils.parsers.rst import Directive


def _author_name(author):
    if "family-names" in author:
        return f"{author['given-names']} {author['family-names']}"
    return author["name"]


class LessonMetadataDirective(Directive):
    """Renders the repository's metadata.yml as an HTML table."""

    has_content = False
    required_arguments = 0
    optional_arguments = 0

    def run(self):
        env = self.state.document.settings.env
        metadata_path = os.path.join(env.srcdir, "..", "metadata.yml")

        with open(metadata_path, encoding="utf-8") as f:
            meta = yaml.safe_load(f)

        fields = [
            ("Title", meta.get("title")),
            (
                "Authors",
                ", ".join(_author_name(a) for a in meta.get("authors", [])),
            ),
            ("Version", meta.get("version", "")),
            ("DOI", meta.get("doi")),
            ("License", meta.get("license")),
            ("Lesson website", meta.get("url")),
            ("Source repository", meta.get("repository-code")),
            ("Keywords", ", ".join(meta.get("keywords", []))),
            ("Educational level", meta.get("educationalLevel")),
            ("Language", meta.get("inLanguage")),
            ("Teaches", meta.get("teaches")),
            ("Is part of", meta.get("isPartOf")),
            ("Audience", meta.get("audience")),
            ("Competency required", meta.get("competencyRequired")),
            ("Accessibility summary", meta.get("accessibilitySummary")),
            ("Learning resource type", meta.get("learningResourceType")),
        ]

        rows = "\n".join(
            f"<tr><th>{label}</th><td>{value}</td></tr>"
            for label, value in fields
            if value
        )

        html = f'<table class="docutils lesson-metadata-table">\n{rows}\n</table>'

        return [nodes.raw("", html, format="html")]


def setup(app):
    app.add_directive("lesson-metadata", LessonMetadataDirective)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
