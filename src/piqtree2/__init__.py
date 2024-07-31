"""piqtree2 - access the power of IQ-TREE within Python."""

from ._iq_wrappers import (
    TreeGenMode,
    build_tree,
    fit_tree,
    random_trees,
    robinson_foulds,
)
from ._options import available_models

__version__ = "0.1.1.dev0"

__all__ = [
    "build_tree",
    "fit_tree",
    "random_trees",
    "robinson_foulds",
    "TreeGenMode",
    "available_models",
]
