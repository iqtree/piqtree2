from enum import Enum, auto
from typing import Any, Optional, Sequence, Union

import cogent3
import numpy as np
import yaml
from _piqtree2 import iq_build_tree, iq_fit_tree, iq_random_tree, iq_robinson_fould

from ._decorators import iqtree_func

iq_build_tree = iqtree_func(iq_build_tree)
iq_fit_tree = iqtree_func(iq_fit_tree)
iq_random_tree = iqtree_func(iq_random_tree)
iq_robinson_fould = iqtree_func(iq_robinson_fould)


def robinson_foulds(*trees: cogent3.PhyloNode) -> np.ndarray:
    pairwise_distances = np.zeros((len(trees), len(trees)))
    for i in range(1, len(trees)):
        for j in range(i):
            rf = iq_robinson_fould(str(trees[i]), str(trees[j]))
            pairwise_distances[i, j] = rf
            pairwise_distances[j, i] = rf
    return pairwise_distances


class TreeGenMode(Enum):
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
    if rand_seed is None:
        rand_seed = 0  # The default rand_seed in IQ-TREE
    trees = iq_random_tree(num_taxa, tree_mode.name, num_trees, rand_seed)
    return tuple(
        cogent3.make_tree(newick) for newick in trees.split("\n") if newick != ""
    )


def _rename_iq_tree(tree: cogent3.PhyloNode, names: Sequence[str]) -> None:
    for tip in tree.tips():
        tip.name = names[int(tip.name)]


def _process_tree_yaml(tree_yaml: dict, names: Sequence[str]) -> cogent3.PhyloNode:
    newick = tree_yaml["PhyloTree"]["newick"]
    tree = cogent3.make_tree(newick)

    candidates = tree_yaml["CandidateSet"]
    likelihood = None
    for candidate in candidates.values():
        if newick in candidate:
            likelihood = float(candidate.split(" ")[0])
            break
    if likelihood is None:
        msg = "IQ-TREE output malformated."
        raise OSError(msg)

    tree.params["lnL"] = likelihood

    _rename_iq_tree(tree, names)
    return tree


def build_tree(
    aln: Union[cogent3.Alignment, cogent3.ArrayAlignment],
    model: str,
    rand_seed: Optional[int] = None,
) -> cogent3.PhyloNode:
    if rand_seed is None:
        rand_seed = 0  # The default rand_seed in IQ-TREE

    names = aln.names
    seqs = [str(seq) for seq in aln.iter_seqs(names)]

    yaml_result = yaml.safe_load(iq_build_tree(names, seqs, model, rand_seed))
    return _process_tree_yaml(yaml_result, names)


def fit_tree(
    aln: Union[cogent3.Alignment, cogent3.ArrayAlignment],
    tree: cogent3.PhyloNode,
    model: str,
    rand_seed: Optional[int] = None,
) -> cogent3.PhyloNode:
    if rand_seed is None:
        rand_seed = 0  # The default rand_seed in IQ-TREE

    names = aln.names
    seqs = [str(seq) for seq in aln.iter_seqs(names)]
    newick = str(tree)

    yaml_result = yaml.safe_load(iq_fit_tree(names, seqs, model, newick, rand_seed))
    return _process_tree_yaml(yaml_result, names)
