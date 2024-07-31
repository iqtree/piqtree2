"""Python wrappers to RF distances in the IQ-TREE library."""

import cogent3
import numpy as np
from _piqtree2 import iq_robinson_fould

from piqtree2.iqtree._decorator import iqtree_func

iq_robinson_fould = iqtree_func(iq_robinson_fould)


def robinson_foulds(*trees: cogent3.PhyloNode) -> np.ndarray:
    """Pairwise Robinson-Foulds distance between a collection of trees.

    For the given collection of trees, returns a numpy array containing
    the pairwise distances between the given trees.

    Returns
    -------
    np.ndarray
        Pairwise Robinson-Foulds distance.

    """
    pairwise_distances = np.zeros((len(trees), len(trees)))
    for i in range(1, len(trees)):
        for j in range(i):
            rf = iq_robinson_fould(str(trees[i]), str(trees[j]))
            pairwise_distances[i, j] = rf
            pairwise_distances[j, i] = rf
    return pairwise_distances
