# piqtree2

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