# PyPI Publishing Checklist

This checklist ensures the `rcservo` package is ready for publication on PyPI.

## Pre-Publication Checklist

### ✅ Package Structure
- [x] Single-file module: `rcservo.py` with `Servo` class and `scale()` function
- [x] Proper `__version__`, `__author__`, and `__all__` defined
- [x] Graceful handling of MicroPython imports

### ✅ Metadata (pyproject.toml)
- [x] Project name: `rcservo`
- [x] Version: `0.1.0` (use semantic versioning)
- [x] Description and readme
- [x] Python version requirement: `>=3.7`
- [x] License: MIT
- [x] Authors: `Anton Vanhoucke`
- [x] Keywords for discoverability
- [x] Classifiers for proper categorization
- [x] Build system configured (setuptools + wheel)
- [x] py_modules configured (single-file package)

### ✅ Documentation
- [x] README.md with clear installation and usage examples
- [x] LICENSE file (MIT)
- [x] DEVELOPMENT.md with contributor guidelines
- [x] Sphinx documentation in `docs/` folder
- [x] MANIFEST.in for distribution files

### ✅ Assets
- [x] Logo: `img/rcservo.png`
- [x] Badges in README (PyPI, License, MicroPython)

### ✅ Testing & Quality
- [x] Basic test suite in `tests/` folder
- [x] .gitignore configured
- [x] No syntax errors in main module

## Steps to Publish to PyPI

### 1. Update GitHub URLs (Required)
Before publishing, update the GitHub URLs in `pyproject.toml`:

```toml
[project.urls]
Homepage = "https://github.com/antonvh/rcservo"
Documentation = "https://github.com/antonvh/rcservo#readme"
Repository = "https://github.com/antonvh/rcservo.git"
Issues = "https://github.com/antonvh/rcservo/issues"
```

Also update the image URL in `README.md` if needed:
```markdown
<img alt="rcservo logo" src="https://raw.githubusercontent.com/antonvh/rcservo/main/img/rcservo.png" width="200">
```

### 2. Test the Package Build Locally

```bash
# Install build tools
pip install build twine

# Clean previous builds & build
rm -rf build/ dist/ *.egg-info && python -m build

# Check contents
ls -lh dist/
```

### 3. Validate Package with Twine

```bash
twine check dist/*
```

### 4. Upload to PyPI

```bash
twine upload dist/*
```

### 5. Verify the Package

Visit `https://pypi.org/project/rcservo/` and verify:
- [ ] Package name and description are correct
- [ ] Logo/README renders properly
- [ ] Installation instructions work
- [ ] Version number is correct

### 6. Test Installation from PyPI

```bash
# Create a fresh virtual environment
python -m venv test-env
source test-env/bin/activate

# Install from PyPI
pip install rcservo

# Test import
python -c "from rcservo import Servo, scale; print('Installation successful!')"
```

## Versioning & Future Releases

### Semantic Versioning

Follow [semver.org](https://semver.org/):
- **MAJOR** (0.x.0): Breaking changes
- **MINOR** (x.1.0): New features, backward compatible
- **PATCH** (x.x.1): Bug fixes

### Updating for New Releases

1. Update version in `pyproject.toml`:
   ```toml
   version = "0.2.0"
   ```

2. Update `__version__` in `rcservo.py`:
   ```python
   __version__ = "0.2.0"
   ```

3. Create a Git tag:
   ```bash
   git tag v0.2.0
   git push origin main --tags
   ```

4. Rebuild and upload:
   ```bash
   rm -rf build/ dist/ *.egg-info
   python -m build
   twine upload dist/*
   ```

## Common Issues & Solutions

### Issue: "InvalidDistribution: File has bad syntax: setup.py"
**Solution:** This package uses `pyproject.toml` only. No `setup.py` is needed.

### Issue: "HTTPError: 400 Client Error: File already exists"
**Solution:** PyPI doesn't allow re-uploading the same version. Increment the version number.

### Issue: "Filename or Version Predates PEP 440"
**Solution:** Ensure version format is correct (e.g., `0.1.0`, not `0.1`).

### Issue: "README doesn't render on PyPI"
**Solution:** Check README.md format is valid Markdown. Validate with:
```bash
twine check dist/*
```

## Resources

- [PyPI Help](https://pypi.org/help/)
- [Setuptools Documentation](https://setuptools.pypa.io/)
- [Python Packaging Guide](https://packaging.python.org/)
- [PEP 427 - Wheel Format](https://www.python.org/dev/peps/pep-0427/)
- [PEP 440 - Version Identification](https://www.python.org/dev/peps/pep-0440/)

## Questions?

- **PyPI Account Issues:** [PyPI Support](https://pypi.org/help/)
- **Package Distribution:** Check [setuptools docs](https://setuptools.pypa.io/)
- **MicroPython Concerns:** See [MicroPython docs](https://docs.micropython.org/)
