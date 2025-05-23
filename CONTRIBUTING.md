# Contributing

## Project set up

To set up a developer environment perform the following steps:

1. Check out the source code and change into its folder.
2. Install [uv](https://docs.astral.sh/uv/).
3. Set up the virtual environment and pre-commit hooks:
   ```bash
   sh scripts/set_up_project.sh
   ```

## Testing

To run the test suite:

```bash
uv run pytest
```

## Publishing a release

1. Update the version number in `pyproject.toml`:
   ```toml
   [project]
   name = "sanpo"
   version = "0.x.x"
   ```
2. Test and build the distribution archives:
   ```bash
   $ uv run pytest
   $ rm -rf dist
   $ uv build
   ```
3. Tag a release (simply replace 0.x.x with the current version number):
   ```bash
   $ git tag -a -m "Tag version 0.x.x" v0.x.x
   $ git push --tags
   ```
4. Upload the release to PyPI:
   ```bash
   $ uv publish
   ```
5. Publish the related
   [GitHub release](https://github.com/roskakori/sanpo/releases/new).
