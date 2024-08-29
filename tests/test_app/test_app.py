from pathlib import Path

import piqtree2
import pytest
from cogent3 import ArrayAlignment, get_app, load_aligned_seqs, make_tree
from piqtree2.model import DnaModel, Model


@pytest.fixture()
def three_otu(DATA_DIR: Path) -> ArrayAlignment:
    aln = load_aligned_seqs(DATA_DIR / "example.fasta", moltype="dna")
    aln = aln.take_seqs(["Human", "Rhesus", "Mouse"])
    return aln.omit_gap_pos(allowed_gap_frac=0)


@pytest.fixture()
def four_otu(DATA_DIR: Path) -> ArrayAlignment:
    aln = load_aligned_seqs(DATA_DIR / "example.fasta", moltype="dna")
    aln = aln.take_seqs(["Human", "Chimpanzee", "Rhesus", "Mouse"])
    return aln.omit_gap_pos(allowed_gap_frac=0)


def test_piqtree_phylo(four_otu: ArrayAlignment):
    expected = make_tree("(Human,Chimpanzee,(Rhesus,Mouse));")
    app = get_app("piqtree_phylo", model=Model(DnaModel.JC))
    got = app(four_otu)
    assert expected.same_topology(got)


def test_piqtree_fit(three_otu: ArrayAlignment):
    tree = make_tree(tip_names=three_otu.names)
    app = get_app("model", "JC69", tree=tree)
    expected = app(three_otu)
    piphylo = get_app("piqtree_fit", tree=tree, model=Model(DnaModel.JC))
    got = piphylo(three_otu)
    assert got.params["lnL"] == pytest.approx(expected.lnL)


@pytest.mark.parametrize("num_taxa", [10, 50, 100])
@pytest.mark.parametrize("num_trees", [1, 10, 20])
@pytest.mark.parametrize("tree_mode", list(piqtree2.TreeGenMode))
def test_piqtree_random_trees(
    num_taxa: int,
    tree_mode: piqtree2.TreeGenMode,
    num_trees: int,
):
    trees = piqtree2.random_trees(
        num_taxa,
        tree_mode,
        num_trees,
        rand_seed=1,
    )
    assert len(trees) == num_trees

    for tree in trees:
        assert len(tree.tips()) == num_taxa
