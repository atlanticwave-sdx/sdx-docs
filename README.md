# AtlanticWave-SDX Documentation

[![rtd-docs-badge]][rtd-docs]

This repository contains some documentation for AtlanticWave-SDX
project.  This is work in progress -- most of our documentation
currently lives elsewhere, and we are evaluating a GitHub based
workflow of documenting the project.

The documentation sources live in [sources] directory.  They are text
documents with [reStructuredText][reST] markup.  HTML version of the
documents is produced by processing them with [Sphinx], and they are
hosted by [readthedocs.org], at [https://sdx-docs.readthedocs.io/].

Some additional information about reStruredText can be found in
[Sphinx manual][Sphinx+reST].


## Writing the docs

The setup will require Python.  First, install the requirements,
preferably in a virtual environment:

```console
$ python3 -m venv venv --upgrade-deps
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Then make the edits you want, and then run:

```console
$ make html
```

The resulting HTML files will be under [build/html].


## Contributing to AtlanticWave-SDX Documentation

Please start a pull request.  If the changes are large, it would be a
good idea to file an issue first so that we can discuss the changes
first.


## Publishing the docs

Publishing is automated: https://sdx-docs.readthedocs.io/ will be
updated when pull requests are merged to `main` branch of this
repository.


<!-- URLs -->

[sources]: ./sources
[build/html]: ./build/html

[reST]: https://docutils.sourceforge.io/rst.html
[readthedocs.org]: https://about.readthedocs.com/
[Sphinx]: https://www.sphinx-doc.org/en/master/index.html
[Sphinx+reST]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

[sdx-docs-rtd]: https://sdx-docs.readthedocs.io/

[rtd-docs]: https://sdx-docs.readthedocs.io/en/latest/?badge=latest
[rtd-docs-badge]: https://readthedocs.org/projects/sdx-docs/badge/?version=latest (Documentation Status)

