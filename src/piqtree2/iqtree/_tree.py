"""Python wrappers to tree searching functions in the IQ-TREE library."""

from collections.abc import Sequence
from typing import Optional, Union

import cogent3
import yaml
from _piqtree2 import iq_build_tree, iq_fit_tree

from piqtree2.exceptions import ParseIqTreeError
from piqtree2.iqtree._decorator import iqtree_func
from piqtree2.model import DnaModel, Model

iq_build_tree = iqtree_func(iq_build_tree, hide_files=True)
iq_fit_tree = iqtree_func(iq_fit_tree, hide_files=True)

# the order defined in IQ-TREE
RATE_PARS = ["A/C", "A/G", "A/T", "C/G", "C/T", "G/T"]
MOTIF_PARS = ["A", "C", "G", "T"]


def _rename_iq_tree(tree: cogent3.PhyloNode, names: Sequence[str]) -> None:
    for tip in tree.tips():
        tip.name = names[int(tip.name)]


def _intrude_edge_pars(tree: cogent3.PhyloNode, **kwargs: dict) -> None:
    for node in tree.get_edge_vector():
        # skip the rate parameters when node is the root
        if node.is_root():
            kwargs = {k: v for k, v in kwargs.items() if k == "mprobs"}
            del node.params["edge_pars"]
        node.params.update(kwargs)


def _reform_edge_pars(tree: cogent3.PhyloNode, model: Model) -> cogent3.PhyloNode:
    rate_pars = dict(
        zip(RATE_PARS, map(float, tree.params["edge_pars"]["rates"].split(", "))),
    )
    motif_pars = {
        "mprobs": dict(
            zip(
                MOTIF_PARS,
                map(float, tree.params["edge_pars"]["state_freq"].split(", ")),
            ),
        ),
    }

    if model.substitution_model in {DnaModel.JC, DnaModel.F81}:
        _intrude_edge_pars(
            tree,
            **motif_pars,  # skip rate_pars since rate parameters are constant in JC and F81
        )
        return tree

    if model.substitution_model in {DnaModel.K80, DnaModel.HKY}:
        rate_pars = {"kappa": rate_pars["A/G"]}

    elif model.substitution_model is DnaModel.TN:
        rate_pars = {"kappa_r": rate_pars["A/G"], "kappa_y": rate_pars["C/T"]}

    elif model.substitution_model is DnaModel.GTR:
        del rate_pars["G/T"]

    _intrude_edge_pars(
        tree,
        **rate_pars,
        **motif_pars,
    )  # add global rate parameters to the edges

    return tree


def _process_tree_yaml(
    tree_yaml: dict,
    names: Sequence[str],
) -> cogent3.PhyloNode:
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
        raise ParseIqTreeError(msg)

    tree.params["lnL"] = likelihood

    if "ModelDNA" in tree_yaml:  # parse only DNA model which is not in Lie model list
        tree.params["edge_pars"] = {
            "rates": tree_yaml["ModelDNA"]["rates"],
            "state_freq": tree_yaml["ModelDNA"]["state_freq"],
        }

    _rename_iq_tree(tree, names)

    return tree


def build_tree(
    aln: Union[cogent3.Alignment, cogent3.ArrayAlignment],
    model: Model,
    rand_seed: Optional[int] = None,
) -> cogent3.PhyloNode:
    """Reconstruct a phylogenetic tree.

    Given a sequence alignment, uses IQ-TREE to reconstruct a phylogenetic tree.

    Parameters
    ----------
    aln : Union[cogent3.Alignment, cogent3.ArrayAlignment]
        The sequence alignment.
    model : Model
        The substitution model with base frequencies and rate heterogeneity.
    rand_seed : Optional[int], optional
        The random seed - 0 or None means no seed, by default None.

    Returns
    -------
    cogent3.PhyloNode
        The IQ-TREE maximum likelihood tree from the given alignment.

    """
    if rand_seed is None:
        rand_seed = 0  # The default rand_seed in IQ-TREE

    names = aln.names
    seqs = [str(seq) for seq in aln.iter_seqs(names)]

    yaml_result = yaml.safe_load(iq_build_tree(names, seqs, str(model), rand_seed))
    tree = _process_tree_yaml(yaml_result, names)

    if "edge_pars" in tree.params:
        tree = _reform_edge_pars(tree, model)
    return tree


def fit_tree(
    aln: Union[cogent3.Alignment, cogent3.ArrayAlignment],
    tree: cogent3.PhyloNode,
    model: Model,
    rand_seed: Optional[int] = None,
) -> cogent3.PhyloNode:
    """Fit branch lengths to a tree.

    Given a sequence alignment and a fixed topology,
    uses IQ-TREE to fit branch lengths to the tree.

    Parameters
    ----------
    aln : Union[cogent3.Alignment, cogent3.ArrayAlignment]
        The sequence alignment.
    tree : cogent3.PhyloNode
        The topology to fit branch lengths to.
    model : Model
        The substitution model with base frequencies and rate heterogeneity.
    rand_seed : Optional[int], optional
        The random seed - 0 or None means no seed, by default None.

    Returns
    -------
    cogent3.PhyloNode
        A phylogenetic tree with same given topology fitted with branch lengths.

    """
    if rand_seed is None:
        rand_seed = 0  # The default rand_seed in IQ-TREE

    names = aln.names
    seqs = [str(seq) for seq in aln.iter_seqs(names)]
    newick = str(tree)

    yaml_result = yaml.safe_load(
        iq_fit_tree(names, seqs, str(model), newick, rand_seed),
    )
    tree = _process_tree_yaml(yaml_result, names)

    if "edge_pars" in tree.params:
        tree = _reform_edge_pars(tree, model)
    return tree
