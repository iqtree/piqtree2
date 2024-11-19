"""cogent3 apps for piqtree2."""

import cogent3
import cogent3.app.typing as c3_types
from cogent3.app import composable
from cogent3.util.misc import extend_docstring_from

from piqtree2 import (
    TreeGenMode,
    build_tree,
    fit_tree,
    jc_distances,
    nj_tree,
    random_trees,
)
from piqtree2.model import Model


@composable.define_app
class piqtree_phylo:
    @extend_docstring_from(build_tree)
    def __init__(
        self,
        submod_type: str,
        freq_type: str | None = None,
        rate_model: str | None = None,
        *,
        invariant_sites: bool = False,
        rand_seed: int | None = None,
        bootstrap_reps: int | None = None,
    ) -> None:
        self._model = Model(
            submod_type=submod_type,
            invariant_sites=invariant_sites,
            rate_model=rate_model,
            freq_type=freq_type,
        )
        self._rand_seed = rand_seed
        self._bootstrap_reps = bootstrap_reps

    def main(
        self,
        aln: c3_types.AlignedSeqsType,
    ) -> cogent3.PhyloNode | cogent3.app.typing.SerialisableType:
        return build_tree(
            aln, self._model, self._rand_seed, bootstrap_replicates=self._bootstrap_reps
        )


@composable.define_app
class piqtree_fit:
    @extend_docstring_from(fit_tree)
    def __init__(
        self,
        tree: cogent3.PhyloNode,
        submod_type: str,
        freq_type: str | None = None,
        rate_model: str | None = None,
        *,
        rand_seed: int | None = None,
        invariant_sites: bool = False,
    ) -> None:
        self._tree = tree
        self._model = Model(
            submod_type=submod_type,
            invariant_sites=invariant_sites,
            rate_model=rate_model,
            freq_type=freq_type,
        )
        self._rand_seed = rand_seed

    def main(
        self,
        aln: c3_types.AlignedSeqsType,
    ) -> cogent3.PhyloNode | cogent3.app.typing.SerialisableType:
        return fit_tree(aln, self._tree, self._model, self._rand_seed)


@composable.define_app
@extend_docstring_from(random_trees)
def piqtree_random_trees(
    num_taxa: int,
    tree_mode: TreeGenMode,
    num_trees: int,
    rand_seed: int | None = None,
) -> tuple[cogent3.PhyloNode]:
    return random_trees(num_taxa, tree_mode, num_trees, rand_seed)


@composable.define_app
@extend_docstring_from(nj_tree)
def piqtree_jc_dists(
    aln: c3_types.AlignedSeqsType,
) -> c3_types.PairwiseDistanceType:
    return jc_distances(aln)


@composable.define_app
@extend_docstring_from(nj_tree)
def piqtree_nj(dists: c3_types.PairwiseDistanceType) -> cogent3.PhyloNode:
    return nj_tree(dists)


_ALL_APP_NAMES = [
    "piqtree_phylo",
    "piqtree_fit",
    "piqtree_random_trees",
    "piqtree_jc_dists",
    "piqtree_nj",
]
