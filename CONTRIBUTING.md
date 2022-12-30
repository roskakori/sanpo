# Contributing

## Project set up

To set up a developer environment perform the following steps:

1. Check out the source code and change into its folder.
2. Set up the [poetry](https://python-poetry.org/) environment:
   ```bash
   poetry install
   ```
3. Set up the [pre-commit](https://pre-commit.com/) checks:
   ```bash
   poetry run pre-commit install --install-hooks
   ```

## Testing

To run the test suite:

```bash
poetry run pytest
```

## Publishing a release

1. Update the version number in `pyproject.toml`:
   ```toml
   [tool.poetry]
   name = "sanpo"
   version = "0.x.x"
   ```
2. Test and build the distribution archives:
   ```bash
   $ poetry run pytest
   $ poetry build
   ```
3. Tag a release (simply replace 0.9.x with the current version number):
   ```bash
   $ git tag -a -m "Tag version 0.x.x" v0.x.x
   $ git push --tags
   ```
4. Upload the release to PyPI:
   ```bash
   $ poetry publish
   ```
5. Publish the related
   [GitHub release](https://github.com/roskakori/sanpo/releases/new).
