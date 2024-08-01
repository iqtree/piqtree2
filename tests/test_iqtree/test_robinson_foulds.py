import numpy as np
import piqtree2
from numpy.testing import assert_array_equal


def test_robinson_foulds():
    tree1 = "(A,B,(C,D));"
    tree2 = "(A,C,(B,D));"
    pairwise_distances = piqtree2.robinson_foulds(tree1, tree2)
    assert_array_equal(pairwise_distances, np.array([[0, 2], [2, 0]]))
