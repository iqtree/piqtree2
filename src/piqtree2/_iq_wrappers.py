from __future__ import annotations

from enum import Enum, auto

import cogent3
import numpy as np
import yaml
from _piqtree2 import iq_build_tree, iq_fit_tree, iq_random_tree, iq_robinson_fould


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
    rand_seed: int | None = None,
) -> tuple[cogent3.PhyloNode]:
    if rand_seed is None:
        rand_seed = 0  # The default rand_seed in IQ-TREE
    trees = iq_random_tree(num_taxa, tree_mode.name, num_trees, rand_seed)
    return tuple(
        cogent3.make_tree(newick + ";") for newick in trees.split(";") if newick != ""
    )


def _rename_iq_tree(tree: cogent3.PhyloNode, names: list[str]) -> None:
    for tip in tree.tips():
        tip.name = names[int(tip.name)]


def build_tree(
    aln: cogent3.Alignment, model: str, rand_seed: int | None = None
) -> cogent3.PhyloNode:
    if rand_seed is None:
        rand_seed = 0  # The default rand_seed in IQ-TREE

    names = aln.names
    seqs = [str(seq) for seq in aln.iter_seqs(names)]

    yaml_result = yaml.safe_load(iq_build_tree(names, seqs, model, rand_seed))
    tree = cogent3.make_tree(yaml_result["PhyloTree"]["newick"])

    _rename_iq_tree(tree, names)
    return tree


def fit_tree(
    aln: cogent3.Alignment,
    tree: cogent3.PhyloNode,
    model: str,
    rand_seed: int | None = None,
) -> cogent3.PhyloNode:
    if rand_seed is None:
        rand_seed = 0  # The default rand_seed in IQ-TREE

    names = aln.names
    seqs = [str(seq) for seq in aln.iter_seqs(names)]
    newick = str(tree)

    yaml_result = yaml.safe_load(iq_fit_tree(names, seqs, model, newick, rand_seed))
    tree = cogent3.make_tree(yaml_result["PhyloTree"]["newick"])

    _rename_iq_tree(tree, names)
    return tree
