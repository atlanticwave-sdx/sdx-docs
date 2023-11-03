# AtlanticWave-SDX Documentation

[![rtd-docs-badge]][rtd-docs]

This repository contains some documentation for AtlanticWave-SDX
project.  This is work in progress -- most of our documentation
currently lives elsewhere, and we are evaluating a GitHub based
workflow of documenting the project.

The documentation sources live in [sources] directory.  They are text
documents with [reStructuredText][reST] markup.  HTML version of the
documents is produced by processing them with [Sphinx], and they are
hosted by [readthedocs.org], at https://sdx-docs.readthedocs.io/.

Some additional information about reStruredText can be found in
[Sphinx manual][Sphinx+reST].


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

[sources]: ./sources
[reST]: https://docutils.sourceforge.io/rst.html
[readthedocs.org]: https://about.readthedocs.com/
[Sphinx]: https://www.sphinx-doc.org/en/master/index.html
[Sphinx+reST]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

[rtd-docs]: https://sdx-docs.readthedocs.io/en/latest/?badge=latest
[rtd-docs-badge]: https://readthedocs.org/projects/sdx-docs/badge/?version=latest (Documentation Status)

