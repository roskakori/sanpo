# sanpo

`sanpo` is a command line tool to sanitize PO files from gettext for version
control.

## The problem

The [gettext](https://www.gnu.org/software/gettext/) collects text to be
translated from source code in PO files that can be sent to translators. These
files contain metadata about the project that can be helpful when using an
email based workflow.

When creating a PO file the first time, these metadata look like this:

```
TODO: Example.
```

However, when having the PO file under version control, these metadata get in
the way. Most of them are available from the commit history. And when
running `gettext` automatically as part of the build process, the
`PO-Revision-Date` get updated every time even if none of the messages
changed, resulting in spuriously modified PO files without any actual
changes worth committing.

## The solution

Your localized software does not use the PO files directly but the MO files
compiled from them, they unhelpful metadata can be removed. Which is exactly
what `sanpo` does.

A typical build chain would look like this:

1. gettext  - collect PO file
2. msgfmt - compile into MO file
3. sanpo - remove unhelpful metadata from PO
4. commit possible changes in PO file

`sanpo` simple takes one or more PO files as argument, for example:

```bash
sanpo locale/de/LC_MESSAGES/django.po locale/en/LC_MESSAGES/django.po locale/hu/LC_MESSAGES/django.po
```
