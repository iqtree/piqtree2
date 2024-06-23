import typing
import cogent3
from  cogent3.composable import define_app

from enum import Enum

class TreeMode(Enum):
    UNIFORM = "UNIFORM",
    UNKNOWN = "UNKNOWN"

@define_app
def robinson_foulds(*trees: cogent3.PhyloNode) -> tuple[int,...]:
    # call libiqtree to calculate the Robinson-Foulds distance between trees
    pass

@define_app
def random_tree(num_taxa: int, tree_mode: TreeMode, num_trees: int, rand_seed: typing.Optional[int]=None) -> tuple[cogent3.PhyloNode]:
    # call libiqtree to generate random trees
    pass

@define_app
def build_tree(aln: cogent3.Alignment, *arguments) -> cogent3.PhyloNode:
    # call libiqtree to build a tree
    return cogent3.PhyloNode()

@define_app
def fit_tree(aln: cogent3.Alignment, tree: cogent3.PhyloNode, *params) -> cogent3.PhyloNode:
    # call libiqtree to fit a tree
    return tree