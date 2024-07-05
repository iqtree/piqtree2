# piqtree2

[![PyPI Version](https://img.shields.io/pypi/v/piqtree2)](https://pypi.org/project/piqtree2/)
[![Python Version](https://img.shields.io/pypi/pyversions/piqtree2)](https://pypi.org/project/piqtree2/)

[![CI](https://github.com/iqtree/piqtree2/workflows/CI/badge.svg)](https://github.com/iqtree/piqtree2/actions/workflows/ci.yml)
<!-- [![Coverage Status](https://coveralls.io/repos/github/iqtree/piqtree2/badge.svg?branch=main)](https://coveralls.io/github/iqtree/piqtree2?branch=main) -->
[![License](https://img.shields.io/github/license/iqtree/piqtree2)](https://github.com/iqtree/piqtree2/blob/main/LICENSE)

## Instructions to build and install the piqtree2 Python library

Assumes user is using the devcontainer in this directory.

1. Initialise and update the IQ-TREE submodule

```bash
git submodule update --init --recursive
```

2. Build IQ-TREE 2

Run either `build_tools/before_all_linux.sh` or `build_tools/before_all_mac.sh` depending on your OS.


3. Build and Install piqtree2

```bash
pip install -e ".[dev]"
```

4. Run Tests

```bash
pytest
```