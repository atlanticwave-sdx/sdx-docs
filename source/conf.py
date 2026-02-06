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

templates_path = ['_templates']

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "_external/**",
    "_external/sdx-release",
    "_external/sdx-release/**",
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
