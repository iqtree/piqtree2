"""Python wrappers to random tree generation in the IQ-TREE library."""

from enum import Enum, auto
from typing import Optional

import cogent3
from _piqtree2 import iq_random_tree

from piqtree2.iqtree._decorator import iqtree_func

iq_random_tree = iqtree_func(iq_random_tree)


class TreeGenMode(Enum):
    """Setting under which to generate random trees."""

    YULE_HARDING = auto()
    UNIFORM = auto()
    CATERPILLAR = auto()
    BALANCED = auto()
    BIRTH_DEATH = auto()
    STAR_TREE = auto()


def random_trees(
    num_taxa: int,
    tree_mode: TreeGenMode,
    num_trees: int,
    rand_seed: Optional[int] = None,
) -> tuple[cogent3.PhyloNode]:
    """Generate a collection of random trees.

    Generates a random collection of trees through IQ-TREE.

    Parameters
    ----------
    num_taxa : int
        The number of taxa per tree.
    tree_mode : TreeGenMode
        How the trees are generated.
    num_trees : int
        The number of trees to generate.
    rand_seed : Optional[int], optional
        The random seed - 0 or None means no seed, by default None.

    Returns
    -------
    tuple[cogent3.PhyloNode]
        A collection of random trees.

    """
    if rand_seed is None:
        rand_seed = 0  # The default rand_seed in IQ-TREE
    trees = iq_random_tree(num_taxa, tree_mode.name, num_trees, rand_seed)
    return tuple(
        cogent3.make_tree(newick) for newick in trees.split("\n") if newick != ""
    )
