# piqtree2

## Instructions to build and install the piqtree2 Python library

Assumes user is using the devcontainer in this directory.

1. Initialise and update the IQ-TREE submodule

```bash
git submodule update --init --recursive
```

2. Apply IQ-TREE patch

```bash
cd iqtree2
git apply ../fpic-iqtree.patch
```

3. Build IQ-TREE

```bash
mkdir build && cd build
cmake -DIQTREE_FLAGS="single" -DBUILD_LIB=ON ..
make -j
```

4. Move static library to libiqtree directory

```bash
cd ../..
mv iqtree2/build/libiqtree2.a piqtree2/libiqtree/
```

5. Build and Install PyIQTree

```bash
pip install ".[dev]"
```

6. Run Tests

```bash
pytest tests/test_RF_distance.py tests/test_generate_random_tree_file.py
```