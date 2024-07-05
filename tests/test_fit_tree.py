import piqtree2
import pytest
from cogent3 import get_app, load_aligned_seqs, make_tree


@pytest.fixture
def three_otu(DATA_DIR):
    aln = load_aligned_seqs(DATA_DIR / "example.fasta", moltype="dna")
    aln = aln.take_seqs(["Human", "Rhesus", "Mouse"])
    return aln.omit_gap_pos(allowed_gap_frac=0)


def test_piqtree_fit(three_otu):
    tree_topology = make_tree(tip_names=three_otu.names)
    app = get_app("model", "JC69", tree=tree_topology)
    expected = app(three_otu)
    got = piqtree2.fit_tree(three_otu, tree_topology, "JC", rand_seed=1)
    assert got.params["lnL"] == pytest.approx(expected.lnL)
