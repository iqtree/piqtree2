"""piqtree2 - access the power of IQ-TREE within Python."""

from piqtree2.iqtree import (
    TreeGenMode,
    build_tree,
    fit_tree,
    random_trees,
    robinson_foulds,
)
from piqtree2.models import available_models

__version__ = "0.1.1.dev0"

__all__ = [
    "available_models",
    "build_tree",
    "fit_tree",
    "random_trees",
    "robinson_foulds",
    "TreeGenMode",
]
