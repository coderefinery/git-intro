# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Introduction to version control with Git"
html_title = project
copyright = "CodeRefinery contributors"
author = "CodeRefinery contributors"
github_user = "coderefinery"
github_repo_name = "git-intro"  # auto-detected from dirname if blank
github_version = "main"
conf_py_path = "/content/"  # with leading and trailing slash

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # githubpages just adds a .nojekyll file
    "sphinx.ext.githubpages",
    "sphinx_lesson",
    # remove once sphinx_rtd_theme updated for contrast and accessibility:
    "sphinx_rtd_theme_ext_color_contrast",
    "sphinx_coderefinery_branding",
]

# Settings for myst_nb:
# https://myst-nb.readthedocs.io/en/latest/computation/execute.html#notebook-execution-modes
#nb_execution_mode = "off"
#nb_execution_mode = "auto"   # *only* execute if at least one output is missing.
#nb_execution_mode = "force"
nb_execution_mode = "cache"

# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
myst_enable_extensions = [
    "colon_fence",  # ::: can be used instead of ``` for better rendering
]

# Settings for sphinx-copybutton
copybutton_exclude = ".linenos, .gp"

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "examples",
    "README*",
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "jupyter_execute",
    "*venv*",
    "img/gitink/README.md",
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    #"prev_next_buttons_location": False,
    "style_external_links": True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["css"]


# HTML context:
from os.path import basename, dirname, realpath

html_context = {
    "display_github": True,
    "github_user": github_user,
    # Auto-detect directory name.  This can break, but
    # useful as a default.
    "github_repo": github_repo_name or basename(dirname(realpath(__file__))),
    "github_version": github_version,
    "conf_py_path": conf_py_path,
}

import os

if os.environ.get("GITHUB_REF", "") == "refs/heads/main":
    html_js_files = [
        (
            "https://plausible.cs.aalto.fi/js/script.js",
            {"data-domain": "coderefinery.github.io", "defer": "defer"},
        ),
    ]


def setup(app):
    app.add_css_file("style.css")
