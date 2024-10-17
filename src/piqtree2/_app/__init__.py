"""cogent3 apps for piqtree2."""

from typing import Optional, Union

import cogent3
import cogent3.app.typing as c3_types
from cogent3.app import composable
from cogent3.util.misc import extend_docstring_from

from piqtree2 import TreeGenMode, build_tree, fit_tree, nj_tree, random_trees
from piqtree2.model import (
    Model,
    available_freq_type,
    available_models,
    available_rate_type,
)


@composable.define_app
class piqtree_phylo:
    @extend_docstring_from(build_tree)
    def __init__(
        self,
        model: str,
        rand_seed: Optional[int] = None,
    ) -> None:
        self._model = Model(model)
        self._rand_seed = rand_seed

    def main(
        self,
        aln: Union[cogent3.Alignment, cogent3.ArrayAlignment],
    ) -> Union[cogent3.PhyloNode, cogent3.app.typing.SerialisableType]:
        return build_tree(aln, self._model, self._rand_seed)


@composable.define_app
@extend_docstring_from(fit_tree)
def piqtree_fit(
    aln: Union[cogent3.Alignment, cogent3.ArrayAlignment],
    tree: cogent3.PhyloNode,
    model: Model,
    rand_seed: Optional[int] = None,
) -> Union[cogent3.PhyloNode, cogent3.app.typing.SerialisableType]:
    model = Model(model)
    return fit_tree(aln, tree, model, rand_seed)


@composable.define_app
@extend_docstring_from(random_trees)
def piqtree_random_trees(
    num_taxa: int,
    tree_mode: TreeGenMode,
    num_trees: int,
    rand_seed: Optional[int] = None,
) -> tuple[cogent3.PhyloNode]:
    return random_trees(num_taxa, tree_mode, num_trees, rand_seed)


@composable.define_app
@extend_docstring_from(nj_tree)
def piqtree_nj(dists: c3_types.PairwiseDistanceType) -> cogent3.PhyloNode:
    return nj_tree(dists)


@composable.define_app(app_type=composable.NON_COMPOSABLE)
def piqtree_list_available(select: str, element_type: str = "model") -> cogent3._Table:
    """returns a table of listing the available options

    Parameters
    ----------
    moltype
        "dna" or "protein". If None, all models are returned.

    Returns
    -------
    A cogent3 Table
    """
    func = {
        "model": available_models,
        "rate": available_rate_type,
        "freq": available_freq_type,
    }[element_type]

    return func(select)


_ALL_APP_NAMES = [
    "piqtree_phylo",
    "piqtree_fit",
    "piqtree_random_trees",
    "piqtree_nj",
    "piqtree_list_available",
]
