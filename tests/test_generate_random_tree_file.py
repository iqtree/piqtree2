import pyiqtree
import os

def test_generate_random_tree_file(tmpdir):
    filename = os.path.join(tmpdir, "random_tree.tree")
    pyiqtree.generate_random_tree_file(10, 1234, "uniform", filename)
    assert os.path.exists(filename)
