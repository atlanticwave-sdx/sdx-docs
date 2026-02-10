# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'AtlanticWave-SDX'
copyright = '2023, AtlanticWave-SDX Contributors'
author = 'AtlanticWave-SDX Contributors'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    'sphinx.ext.todo'
]

# 1. FIX: Removed "frontmatter" from here because it's built-in.
# You can leave this as an empty list.
myst_enable_extensions = []

# 2. FIX: This promotes your 'title: 2026.1.0' from the YAML to be the H1.
# This solves the "H2 before H1" error and ensures you only have ONE title.
myst_title_to_header = True

# 3. Suppress the header warning just in case
suppress_warnings = ["myst.header"]

# -----------------------------------------

templates_path = ['_templates']

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]

language = 'en'

# Display todos by setting to True
todo_include_todos = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
