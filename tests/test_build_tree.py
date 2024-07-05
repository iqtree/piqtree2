import piqtree2
import pytest
from cogent3 import load_aligned_seqs, make_tree


@pytest.fixture()
def four_otu(DATA_DIR):
    aln = load_aligned_seqs(DATA_DIR / "example.fasta", moltype="dna")
    aln = aln.take_seqs(["Human", "Chimpanzee", "Rhesus", "Mouse"])
    return aln.omit_gap_pos(allowed_gap_frac=0)


def test_phylogenetic_analysis(four_otu):
    expected = make_tree("(Human,Chimpanzee,(Rhesus,Mouse));")

    got1 = piqtree2.build_tree(four_otu, "JC", rand_seed=1)
    assert expected.same_topology(got1)

    # Should be similar for any seed
    got2 = piqtree2.build_tree(four_otu, "JC", rand_seed=None)
    assert expected.same_topology(got2)
