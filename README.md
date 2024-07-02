# piqtree2

## Instructions to build and install the piqtree2 Python library

Assumes user is using the devcontainer in this directory.

1. Initialise and update the IQ-TREE submodule

```bash
git submodule update --init --recursive
```

2. Build IQ-TREE

In the iqtree2 folder:

```bash
mkdir build && cd build
cmake -DIQTREE_FLAGS="single" -DBUILD_LIB=ON ..
make -j
```

3. Move static library to libiqtree directory

```bash
cd ../..
mv iqtree2/build/libiqtree2.a src/piqtree2/libiqtree/
```

4. Build and Install piqtree2

```bash
pip install ".[dev]"
```

5. Run Tests

```bash
pytest
```