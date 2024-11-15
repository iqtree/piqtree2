"""piqtree2 - access the power of IQ-TREE within Python."""

from piqtree2.iqtree import (
    TreeGenMode,
    build_tree,
    fit_tree,
    jc_distances,
    model_finder,
    nj_tree,
    random_trees,
    robinson_foulds,
)
from piqtree2.model import (
    Model,
    available_freq_type,
    available_models,
    available_rate_type,
)

__version__ = "0.3.1"

__all__ = [
    "available_freq_type",
    "available_models",
    "available_rate_type",
    "build_tree",
    "fit_tree",
    "jc_distances",
    "Model",
    "model_finder",
    "nj_tree",
    "random_trees",
    "robinson_foulds",
    "TreeGenMode",
]
