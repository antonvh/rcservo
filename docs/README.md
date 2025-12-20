# Documentation

This directory contains the Sphinx documentation for rcservo.

## Building the Documentation

### Prerequisites

Install the required packages:

```bash
pip install sphinx sphinx-rtd-theme
```

Or use the docs extra:

```bash
pip install -e ".[docs]"
```

### Generate HTML Documentation

On Linux/macOS:

```bash
cd docs
make html
```

On Windows:

```bash
cd docs
make.bat html
```

The built documentation will be in `docs/_build/html/`.

### View the Documentation

Open `docs/_build/html/index.html` in your web browser.

## Documentation Structure

- `conf.py` - Sphinx configuration
- `index.rst` - Main documentation entry point
- `api.rst` - API reference (auto-generated from docstrings)
- `usage.rst` - Usage guide and examples
- `modules.rst` - Module documentation index
