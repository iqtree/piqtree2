import piqtree2
import pytest
from cogent3 import get_app, load_aligned_seqs, make_tree
from piqtree2.model import DnaModel, Model


@pytest.fixture()
def three_otu(DATA_DIR):
    aln = load_aligned_seqs(DATA_DIR / "example.fasta", moltype="dna")
    aln = aln.take_seqs(["Human", "Rhesus", "Mouse"])
    return aln.omit_gap_pos(allowed_gap_frac=0)


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
def test_fit_tree(three_otu, iq_model, c3_model):
    tree_topology = make_tree(tip_names=three_otu.names)
    app = get_app("model", c3_model, tree=tree_topology)
    expected = app(three_otu)

    got1 = piqtree2.fit_tree(three_otu, tree_topology, Model(iq_model), rand_seed=1)
    assert got1.params["lnL"] == pytest.approx(expected.lnL)

    # Should be within an approximation for any seed
    got2 = piqtree2.fit_tree(three_otu, tree_topology, Model(iq_model), rand_seed=None)
    assert got2.params["lnL"] == pytest.approx(expected.lnL)
