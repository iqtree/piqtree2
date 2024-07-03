import pytest
from cogent3 import get_app, load_aligned_seqs, make_tree


@pytest.fixture
def three_otu(DATA_DIR):
    aln = load_aligned_seqs(DATA_DIR / "example.fasta", moltype="dna")
    aln = aln.take_seqs(["Human", "Rhesus", "Mouse"])
    return aln.omit_gap_pos(allowed_gap_frac=0)


def test_piqtree_fit(three_otu):
    tree = make_tree(tip_names=three_otu.names)
    app = get_app("model", "JC69", tree=tree)
    expect = app(three_otu)
    piphylo = get_app("piqtree_fit", tree=tree, model="JC")
    got = piphylo(three_otu)
    assert got.params["lnL"] == pytest.approx(expect.lnL)
