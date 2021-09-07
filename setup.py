"""
Setup for pygount.
Developer cheat sheet
---------------------
Tag a release (simply replace ``1.x.x`` with the current version number)::
  $ git tag -a -m "Tagged version 1.x.x." v1.x.x
  $ git push --tags
Upload release to PyPI::
  $ python3 setup.py bdist_wheel
  $ twine check dist/*.whl
  $ twine upload --config-file ~/.pypirc dist/*.whl
"""
# Copyright (c) 2016-2021, Thomas Aglassinger.
# All rights reserved. Distributed under the BSD License.
import os

from setuptools import find_packages, setup

from sanpo import __version__

# Read the long description from the README file.
_setup_folder = os.path.dirname(__file__)
with open(os.path.join(_setup_folder, "README.md"), encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="sanpo",
    version=__version__,
    description="Sanitize PO files from gettext for version control",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/roskakori/sanpo",
    project_urls={
        "Issue Tracker": "https://github.com/roskakori/sanpo/issues",
    },
    author="Thomas Aglassinger",
    author_email="roskakori@users.sourceforge.net",
    license="BSD",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Internationalization",
        "Topic :: Software Development :: Version Control",
    ],
    keywords=["clean", "gettext", "po", "sanitize"],
    packages=find_packages(exclude=["tests"]),
    install_requires=[""],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["sanpo=sanpo.command:main"]},
)
