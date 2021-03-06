# Sudokuku

[![Python Version](https://img.shields.io/pypi/pyversions/sudokuku?style=flat-square)](https://pypi.org/project/sudokuku)
[![License](https://img.shields.io/pypi/l/sudokuku?style=flat-square)](https://github.com/jonasstrube/sudokuku/blob/main/LICENSE)

[![PyPI Package Version](https://shields.io/pypi/v/sudokuku?style=flat-square)](https://pypi.org/project/sudokuku)
[![PyPI Downloads](https://img.shields.io/pypi/dm/sudokuku?style=flat-square)](https://pypi.org/project/sudokuku)
![GitHub Repository Size](https://shields.io/github/repo-size/jonasstrube/sudokuku?style=flat-square)
![GitHub Last Commit](https://img.shields.io/github/last-commit/jonasstrube/sudokuku?style=flat-square)
[![codecov](https://img.shields.io/codecov/c/github/jonasstrube/sudokuku?style=flat-square)](https://codecov.io/gh/jonasstrube/sudokuku)

A package for solving sudokus

## Contributing

Contributions are always welcome.

### Testing

You can run all tests via

    py -m pytest

You can also look up code coverage, for example using [pytest-cov](https://pypi.org/project/pytest-cov/).

    py -m pytest --cov sudokuku/

For testing your own changes, install sudokuku in development mode. The package installation will link directly to your local development files, not to the official files you downloaded from pypi.

    pip install -e ./
