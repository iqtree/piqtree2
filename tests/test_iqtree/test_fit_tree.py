import piqtree2
import pytest
from cogent3 import ArrayAlignment, get_app, make_tree
from piqtree2.model import DnaModel, Model


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
    assert got1.params["lnL"] == pytest.approx(expected.lnL)

    # Should be within an approximation for any seed
    got2 = piqtree2.fit_tree(three_otu, tree_topology, Model(iq_model), rand_seed=None)
    assert got2.params["lnL"] == pytest.approx(expected.lnL)

    # Check motif and rate parameters
    expected_motif_prob = expected.tree.params["mprobs"]
    for k, v in expected_motif_prob.items():
        assert k in got2.params["mprobs"]
        assert got2.params["mprobs"][k] == pytest.approx(v)

    exclude = {"length", "ENS", "paralinear", "mprobs"}
    expected_rates = {
        k: v
        for k, v in expected.tree.get_edge_vector()[0].params.items()
        if k not in exclude
    }
    for k, v in expected_rates.items():
        assert k in got2.get_edge_vector()[0].params
        assert got2.get_edge_vector()[0].params[k] == pytest.approx(
            v,
            rel=1e-2,
        )
