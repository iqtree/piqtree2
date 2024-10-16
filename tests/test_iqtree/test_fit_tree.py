import pytest
from cogent3 import ArrayAlignment, get_app, make_tree

import piqtree2
from piqtree2.model import DnaModel, Model


def check_likelihood(got:float, expected:float) -> None:
    assert got == pytest.approx(expected)

def check_motif_probs(got:dict, expected:dict) -> None:
    expected_keys = set(expected.keys())
    got_keys = set(got.keys())
    # Check that the base characters are the same
    assert expected_keys == got_keys

    # Check that the probs are the same
    expected_values = [expected[key] for key in expected_keys]
    got_values = [got[key] for key in expected_keys]
    assert all(got == pytest.approx(exp) for got, exp in zip(got_values, expected_values))

def check_rate_parameters(got:dict, expected:dict) -> None:
    # Collect all rate parameters in got and expected
    exclude = {"length", "ENS", "paralinear", "mprobs"}
    expected_keys = {
        k
        for k in expected[0].params
        if k not in exclude
    }
    got_keys = {k for k in got[0].params if k not in exclude}


    # Check that the keys of rate are the same
    assert expected_keys == got_keys

    # Check that the values of rate are the same
    expected_values = [expected[0].params[key] for key in expected_keys]
    got_values = [got[0].params[key] for key in expected_keys]

    assert all(got == pytest.approx(exp, rel=1e-2) for got, exp in zip(got_values, expected_values))

def check_branch_lengths(got:dict, expected:dict) -> None:
    # Check that the keys of branch lengths are the same
    assert got.keys() == expected.keys()

    # Check that the branch lengths are the same
    expected_values = [expected[key] for key in expected]
    got_values = [got[key] for key in expected]

    assert all(got == pytest.approx(exp, rel=1e-2) for got, exp in zip(got_values, expected_values))

@pytest.mark.parametrize(
    ("iq_model", "c3_model"),
    [
        (DnaModel.JC, "JC69"),
        (DnaModel.K80, "K80"),
        (DnaModel.GTR, "GTR"),
        (DnaModel.TN, "TN93"),
        (DnaModel.HKY, "HKY85"),
        (DnaModel.F81, "F81"),
    ],
)
def test_fit_tree(three_otu: ArrayAlignment, iq_model: DnaModel, c3_model: str) -> None:
    tree_topology = make_tree(tip_names=three_otu.names)
    app = get_app("model", c3_model, tree=tree_topology)
    expected = app(three_otu)

    got1 = piqtree2.fit_tree(three_otu, tree_topology, Model(iq_model), rand_seed=1)
    check_likelihood(got1.params["lnL"], expected.lnL)
    check_motif_probs(got1.params["mprobs"], expected.tree.params["mprobs"])
    check_rate_parameters(got1.get_edge_vector(), expected.tree.get_edge_vector())
    check_branch_lengths(got1.get_distances(), expected.tree.get_distances())

    # Should be within an approximation for any seed
    got2 = piqtree2.fit_tree(three_otu, tree_topology, Model(iq_model), rand_seed=None)
    check_likelihood(got2.params["lnL"], expected.lnL)
    check_motif_probs(got2.params["mprobs"], expected.tree.params["mprobs"])
    check_rate_parameters(got2.get_edge_vector(), expected.tree.get_edge_vector())
    check_branch_lengths(got2.get_distances(), expected.tree.get_distances())
