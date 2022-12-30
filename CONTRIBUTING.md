# Contributing

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

To run the test suite:

```bash
poetry run pytest
```
