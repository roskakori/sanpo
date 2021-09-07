# Contributing

To set up a developer environment perform the following steps:

1. Check out the source code and change into its folder.
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   . venv/bin/activate
   ```
3. Install the required packages:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

To run the test suite:

```bash
python setup.py test
```

To activate the current version in this folder and call the command line too:

```bash
python setup.py develop
sanpo --version
```
