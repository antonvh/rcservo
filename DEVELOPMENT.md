# Development Guide

This document provides instructions for setting up a development environment for the `rcservo` project and contributing to it.

## Development Prerequisites

- Python 3.7 or higher
- Git
- pip and virtual environment tools

## Setting Up the Development Environment

### 1. Clone the Repository

```bash
git clone https://github.com/antonvh/rcservo.git
cd rcservo
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install the Package in Editable Mode with Development Dependencies

```bash
pip install -e ".[dev]"
```

This installs the package in editable mode along with all development, testing, and documentation dependencies.

## Project Structure

``` text
rcservo/
├── rcservo.py              # Main module (single-file package)
├── package.json            # mip manifest for MicroPython installs
├── tests/                  # Test suite
│   ├── __init__.py
│   └── test_servo.py       # Servo class tests
├── docs/                   # Sphinx documentation
│   ├── conf.py
│   ├── index.rst
│   ├── Makefile
│   └── make.bat
├── img/                    # Assets (logo, etc.)
├── pyproject.toml          # Project metadata and build config
├── README.md               # User-facing documentation
├── DEVELOPMENT.md          # This file
├── LICENSE                 # MIT License
└── MANIFEST.in             # Distribution manifest
```

## Running Tests

### Basic Test Run

```bash
pytest
```

### Run with Coverage

```bash
pip install pytest-cov
pytest --cov=rcservo tests/
```

### Run Specific Test File

```bash
pytest tests/test_servo.py -v
```

## Building Documentation

### Building Docs Prerequisites

Documentation is already installed if you ran `pip install -e ".[dev]"`. If not:

```bash
pip install -e ".[docs]"
```

### Build HTML Documentation

```bash
cd docs
make html
```

The built documentation will be available at `docs/_build/html/index.html`.

### View Documentation Locally

```bash
open docs/_build/html/index.html  # macOS
xdg-open docs/_build/html/index.html  # Linux
start docs/_build/html/index.html  # Windows
```

## Code Style and Linting

While `rcservo` is minimal, we recommend following PEP 8 standards:

```bash
pip install black flake8 isort
black rcservo.py tests/
isort rcservo.py tests/
flake8 rcservo.py tests/
```

## Building the Package

### Local Build

```bash
pip install build
python -m build
```

This generates distribution files in `dist/`:

- `rcservo-0.1.0.tar.gz` (source distribution)
- `rcservo-0.1.0-py3-none-any.whl` (wheel)

### Test Installation

```bash
pip install dist/rcservo-0.1.0-py3-none-any.whl
python -c "from rcservo import Servo, scale; print('Success!')"
```

## Publishing to PyPI

### Prerequisites

1. Create an account on [PyPI](https://pypi.org/account/register/)
2. Create a PyPI API token in your account settings
3. Store credentials in `~/.pypirc`:

```ini
[distutils]
index-servers =
    pypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = pypi_YOUR_API_TOKEN_HERE
```

Or use environment variables:

```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi_YOUR_API_TOKEN_HERE
```

### Build and Upload

```bash
# Clean previous builds
rm -rf build/ dist/ *.egg-info

# Build distributions
python -m build

# Upload to PyPI
pip install twine
twine upload dist/*
```

### Test PyPI Upload (Recommended First)

```bash
twine upload --repository testpypi dist/*
```

Then test installation:

```bash
pip install --index-url https://test.pypi.org/simple/ rcservo
```

## Version Bumping

Update the version in `pyproject.toml`:

```toml
[project]
version = "0.2.0"
```

Also update `__version__` in `rcservo.py` if needed.

## Creating a Release

1. **Update version** in `pyproject.toml`
2. **Update CHANGELOG** (if applicable)
3. **Commit changes:**

   ```bash
   git add -A
   git commit -m "Bump version to 0.2.0"
   git tag v0.2.0
   git push origin main --tags
   ```

4. **Build and publish:**

   ```bash
   python -m build
   twine upload dist/*
   ```

## Contributing

### Before Submitting a Pull Request

1. **Fork** the repository
2. **Create a feature branch:** `git checkout -b feature/your-feature`
3. **Make changes** and add tests if applicable
4. **Run tests:** `pytest`
5. **Lint code:** `flake8 rcservo.py`
6. **Build docs (if modified):** `cd docs && make html`
7. **Commit** with clear messages
8. **Push** to your fork
9. **Open a Pull Request** with a clear description

### Code Guidelines

- Keep `rcservo.py` minimal and focused
- Add docstrings to all public functions and classes
- Use type hints where helpful (Python 3.7+ compatible)
- Write tests for new functionality
- Update documentation for user-facing changes

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'rcservo'`

**Solution:** Install in editable mode:

```bash
pip install -e .
```

### Issue: Tests fail with MicroPython dependencies

**Solution:** Tests gracefully handle missing MicroPython imports. Run with standard CPython.

### Issue: Documentation won't build

**Solution:** Ensure Sphinx is installed:

```bash
pip install -e ".[docs]"
cd docs && make clean && make html
```

## Resources

- [PyPI Packaging Guide](https://packaging.python.org/)
- [Setuptools Documentation](https://setuptools.pypa.io/)
- [MicroPython Documentation](https://docs.micropython.org/)
- [PEP 8 Style Guide](https://pep8.org/)

## Questions?

Open an issue on [GitHub](https://github.com/antonvh/rcservo/issues) with the `question` or `help` label.
