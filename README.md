# sdx-docs

Some documentation for AtlanticWave-SDX project

## Writing the docs

Edit the source files in source directory.  They are in
reStructuredText format.


## Building the docs

First, install Sphinx and a theme, preferably in a virtual
environment:

```console
$ python3 -m venv venv --upgrade-deps
$ source venv/bin/activate
$ pip install sphinx sphinx-book-theme
```

Then run:

```console
$ make html
```
