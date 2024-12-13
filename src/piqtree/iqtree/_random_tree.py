"""Python wrappers to random tree generation in the IQ-TREE library."""

from enum import Enum, auto

import cogent3
from _piqtree import iq_random_tree

from piqtree.iqtree._decorator import iqtree_func

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
    num_trees: int,
    num_taxa: int,
    tree_mode: TreeGenMode,
    rand_seed: int | None = None,
) -> tuple[cogent3.PhyloNode]:
    """Generate a collection of random trees.

    Generates a random collection of trees through IQ-TREE.

    Parameters
    ----------
    num_trees : int
        The number of trees to generate.
    num_taxa : int
        The number of taxa per tree.
    tree_mode : TreeGenMode
        How the trees are generated.
    rand_seed : int | None, optional
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
