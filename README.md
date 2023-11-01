# AtlanticWave-SDX Documentation.

[![rtd-docs-badge][rtd-docs]]

This repository contains some documentation for AtlanticWave-SDX
project.  This is work in progress -- most of our documentation
currently lives elsewhere, and we are evaluating a GitHub based
workflow of documenting the project.


## Writing the docs

Edit the source files in source directory.  They are in
reStructuredText format.


## Building the docs

First, install Sphinx and a theme, preferably in a virtual
environment:

```console
$ python3 -m venv venv --upgrade-deps
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Then run:

```console
$ make html
```

<!-- URLs -->

[rtd-docs]: https://sdx-docs.readthedocs.io/en/latest/?badge=latest
[rtd-docs-badge]: https://readthedocs.org/projects/sdx-docs/badge/?version=latest (Documentation Status)

