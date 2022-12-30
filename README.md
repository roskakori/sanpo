[![PyPI](https://img.shields.io/pypi/v/sanpo)](https://pypi.org/project/sanpo/)
[![Python Versions](https://img.shields.io/pypi/pyversions/sanpo.svg)](https://www.python.org/downloads/)
[![Build Status](https://github.com/roskakori/sanpo/actions/workflows/build.yaml/badge.svg)](https://github.com/roskakori/sanpo/actions/workflows/build.yaml)
[![Test Coverage](https://img.shields.io/coveralls/github/roskakori/sanpo)](https://coveralls.io/r/roskakori/sanpo?branch=main)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/github/license/roskakori/sanpo)](https://opensource.org/licenses/BSD-3-Clause)

# sanpo

`sanpo` is a command line tool to sanitize PO files from gettext for version
control.

## The problem

The [gettext](https://www.gnu.org/software/gettext/) tool collects text to be
translated from source code in PO files that can be sent to translators. These
files contain metadata about the project that can be helpful when using an
email based workflow.

When creating a PO file the first time, these metadata look like this:

```
"Project-Id-Version: PACKAGE VERSION\n"
"Report-Msgid-Bugs-To: \n"
"POT-Creation-Date: 2021-09-06 16:16+0200\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language-Team: LANGUAGE <LL@li.org>\n"
"Language: \n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"
"Plural-Forms: nplurals=2; plural=(n != 1);\n"
```

However, when having the PO file under version control, these metadata get in
the way. Most of them are available from the commit history. And when
running `gettext` automatically as part of the build process, the
`PO-Revision-Date` gets updated every time even if none of the messages
changed, resulting in spuriously modified PO files without any actual
changes worth committing.

## The solution

Because your localized software does not use the PO files directly but the MO
files compiled from them, the unhelpful metadata can be removed. Which is
exactly what `sanpo` does.

A typical build chain would look like this:

1. gettext - collect PO file
2. msgfmt - compile into MO file
3. sanpo - remove unhelpful metadata from PO
4. commit possible changes in PO file

`sanpo` simple takes one or more PO files as argument, for example:

```bash
sanpo locale/de/LC_MESSAGES/django.po locale/en/LC_MESSAGES/django.po locale/hu/LC_MESSAGES/django.po
```

After this, the remaining metadata are:

```
"Language: \n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"
"Plural-Forms: nplurals=2; plural=(n != 1);\n"
```

Using the special pattern `**` folders can be scanned recursively.

To sanitize PO files for all languages in a certain folder, use for example:

```bash
sanpo locale/**/django.po
```

## Django

For [Django](https://www.djangoproject.com/) projects, the typical workflow
is:

1. django-admin makemessages
2. django-admin compilemessages
3. sanpo
4. commit possible changes in PO file
