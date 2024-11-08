"""Python wrappers to tree searching functions in the IQ-TREE library."""

from collections.abc import Sequence

import cogent3
import cogent3.app.typing as c3_types
import numpy as np
import yaml
from _piqtree2 import iq_build_tree, iq_fit_tree, iq_nj_tree
from cogent3 import make_tree

from piqtree2.exceptions import ParseIqTreeError
from piqtree2.iqtree._decorator import iqtree_func
from piqtree2.model import DnaModel, Model

iq_build_tree = iqtree_func(iq_build_tree, hide_files=True)
iq_fit_tree = iqtree_func(iq_fit_tree, hide_files=True)
iq_nj_tree = iqtree_func(iq_nj_tree, hide_files=True)


# the order defined in IQ-TREE
RATE_PARS = "A/C", "A/G", "A/T", "C/G", "C/T", "G/T"
MOTIF_PARS = "A", "C", "G", "T"


def _rename_iq_tree(tree: cogent3.PhyloNode, names: Sequence[str]) -> None:
    for tip in tree.tips():
        tip.name = names[int(tip.name)]


def _insert_edge_pars(tree: cogent3.PhyloNode, **kwargs: dict) -> None:
    # inserts the edge parameters into each edge to match the structure of
    # cogent3.PhyloNode
    for node in tree.get_edge_vector():
        # skip the rate parameters when node is the root
        if node.is_root():
            kwargs = {k: v for k, v in kwargs.items() if k == "mprobs"}
            del node.params["edge_pars"]
        node.params.update(kwargs)


def _edge_pars_for_cogent3(tree: cogent3.PhyloNode, model: Model) -> None:
    rate_pars = tree.params["edge_pars"]["rates"]
    motif_pars = {"mprobs": tree.params["edge_pars"]["mprobs"]}
    # renames parameters to conform to cogent3's naming conventions
    if model.substitution_model in {DnaModel.JC, DnaModel.F81}:
        # skip rate_pars since rate parameters are constant in JC and F81
        _insert_edge_pars(
            tree,
            **motif_pars,
        )
        return
    if model.substitution_model in {DnaModel.K80, DnaModel.HKY}:
        rate_pars = {"kappa": rate_pars["A/G"]}

    elif model.substitution_model is DnaModel.TN:
        rate_pars = {"kappa_r": rate_pars["A/G"], "kappa_y": rate_pars["C/T"]}

    elif model.substitution_model is DnaModel.GTR:
        del rate_pars["G/T"]

    # applies global rate parameters to each edge
    _insert_edge_pars(
        tree,
        **rate_pars,
        **motif_pars,
    )


def _parse_nonlie_model(tree: cogent3.PhyloNode, tree_yaml: dict) -> None:
    # parse motif and rate parameters in the tree_yaml for non-Lie DnaModel
    model_fits = tree_yaml.get("ModelDNA", {})

    state_freq_str = model_fits.get("state_freq", "")
    rate_str = model_fits.get("rates", "")

    # parse motif parameters, assign each to a name, and raise an error if not found
    if state_freq_str:
        # converts the strings of motif parameters into dictionary
        state_freq_list = [
            float(value) for value in state_freq_str.replace(" ", "").split(",")
        ]
        tree.params["edge_pars"] = {
            "mprobs": dict(zip(MOTIF_PARS, state_freq_list, strict=True)),
        }
    else:
        msg = "IQ-TREE output malformated, motif parameters not found."
        raise ParseIqTreeError(msg)

    # parse rate parameters, assign each to a name, and raise an error if not found
    if rate_str:
        rate_list = [float(value) for value in rate_str.replace(" ", "").split(",")]
        tree.params["edge_pars"]["rates"] = dict(
            zip(RATE_PARS, rate_list, strict=True),
        )
    else:
        msg = "IQ-TREE output malformated, rate parameters not found."
        raise ParseIqTreeError(msg)


def _parse_lie_model(
    tree: cogent3.PhyloNode,
    tree_yaml: dict,
    lie_model_name: str,
) -> None:
    # parse motif and rate parameters in the tree_yaml for Lie DnaModel
    model_fits = tree_yaml.get(lie_model_name, {})

    # parse motif parameters, assign each to a name, and raise an error if not found
    state_freq_str = model_fits.get("state_freq", "")
    if state_freq_str:
        state_freq_list = [
            float(value) for value in state_freq_str.replace(" ", "").split(",")
        ]
        tree.params[lie_model_name] = {
            "mprobs": dict(zip(MOTIF_PARS, state_freq_list, strict=True)),
        }
    else:
        msg = "IQ-TREE output malformated, motif parameters not found."
        raise ParseIqTreeError(msg)

    # parse rate parameters, skipping LIE_1_1 (aka JC69) since its rate parameter is constant thus absent
    if "model_parameters" in model_fits:
        model_parameters = model_fits["model_parameters"]

        # convert model parameters to a list of floats if they are a string
        if isinstance(model_parameters, str):
            tree.params[lie_model_name]["model_parameters"] = [
                float(value) for value in model_parameters.replace(" ", "").split(",")
            ]
        else:
            # directly use the float
            tree.params[lie_model_name]["model_parameters"] = model_parameters


def _process_tree_yaml(
    tree_yaml: dict,
    names: Sequence[str],
) -> cogent3.PhyloNode:
    newick = tree_yaml["PhyloTree"]["newick"]

    tree = cogent3.make_tree(newick)
    t2t_matrix = tree.tip_to_tip_distances()[0]
    candidates = tree_yaml["CandidateSet"]
    likelihood = None
    for candidate in candidates.values():
        candidate_likelihood, candidate_newick = candidate.split(" ")
        candidate_tree = cogent3.make_tree(candidate_newick)
        candidate_t2t_matrix = candidate_tree.tip_to_tip_distances()[0]
        if np.allclose(t2t_matrix, candidate_t2t_matrix):
            likelihood = float(candidate_likelihood)
            break
    if likelihood is None:
        msg = "IQ-TREE output malformated, likelihood not found."
        raise ParseIqTreeError(msg)

    tree.params["lnL"] = likelihood

    # parse non-Lie DnaModel parameters
    if "ModelDNA" in tree_yaml:
        _parse_nonlie_model(tree, tree_yaml)

    # parse Lie DnaModel parameters, handling various Lie model names
    elif key := next(
        (key for key in tree_yaml if key.startswith("ModelLieMarkov")),
        None,
    ):
        _parse_lie_model(tree, tree_yaml, key)

    # parse rate model, handling various rate model names
    if key := next((key for key in tree_yaml if key.startswith("Rate")), None):
        tree.params[key] = tree_yaml[key]

    _rename_iq_tree(tree, names)

    return tree


def build_tree(
    aln: cogent3.Alignment | cogent3.ArrayAlignment,
    model: Model,
    rand_seed: int | None = None,
    bootstrap_replicates: int = 0,
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
    bootstrap_replicates : int, optional
        The number of bootstrap replicates to perform, by default 0.
        If 0 is provided, then no bootstrapping is performed. 
        At least 1000 is required to perform bootstrapping.

    Returns
    -------
    cogent3.PhyloNode
        The IQ-TREE maximum likelihood tree from the given alignment.

    """
    if rand_seed is None:
        rand_seed = 0  # The default rand_seed in IQ-TREE

    names = aln.names
    seqs = [str(seq) for seq in aln.iter_seqs(names)]

    yaml_result = yaml.safe_load(
        iq_build_tree(names, seqs, str(model), rand_seed, bootstrap_replicates),
    )
    tree = _process_tree_yaml(yaml_result, names)

    # for non-Lie models, populate parameters to each branch and
    # rename them to mimic cogent3.PhyloNode
    if "edge_pars" in tree.params:
        _edge_pars_for_cogent3(tree, model)
    return tree


def fit_tree(
    aln: cogent3.Alignment | cogent3.ArrayAlignment,
    tree: cogent3.PhyloNode,
    model: Model,
    rand_seed: int | None = None,
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

    # for non-Lie models, populate parameters to each branch and
    # rename them to mimic cogent3.PhyloNode
    if "edge_pars" in tree.params:
        _edge_pars_for_cogent3(tree, model)
    return tree


def nj_tree(pairwise_distances: c3_types.PairwiseDistanceType) -> cogent3.PhyloNode:
    """Construct a neighbour joining tree from a pairwise distance matrix.

    Parameters
    ----------
    pairwise_distances : c3_types.PairwiseDistanceType
        Pairwise distances to construct neighbour joining tree from.

    Returns
    -------
    cogent3.PhyloNode
        The neigbour joining tree.

    See Also
    --------
    jc_distances : construction of pairwise JC distance matrix from alignment.
    """
    newick_tree = iq_nj_tree(
        pairwise_distances.keys(),
        np.array(pairwise_distances).flatten(),
    )
    return make_tree(newick_tree)
