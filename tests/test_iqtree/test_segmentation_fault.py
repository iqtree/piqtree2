"""Test combinations of calls which under previous versions resulted in a segmentation fault."""

import pytest
from cogent3 import make_aligned_seqs, make_tree
from piqtree2 import TreeGenMode, build_tree, fit_tree, random_trees
from piqtree2.exceptions import IqTreeError
from piqtree2.model import DnaModel, Model


def test_two_build_random_trees():
    """
    Calling build tree twice followed by random trees with a bad input
    used to result in a Segmentation Fault in a previous version.
    """
    aln = make_aligned_seqs({"a": "GGG", "b": "GGC", "c": "AAC", "d": "AAA"})

    build_tree(aln, Model(DnaModel.JC), 1)
    build_tree(aln, Model(DnaModel.JC), 2)

    with pytest.raises(IqTreeError):
        random_trees(2, TreeGenMode.BALANCED, 3, 1)


def test_two_fit_random_trees():
    """
    Calling fit tree twice followed by random trees with a bad input
    used to result in a Segmentation Fault in a previous version.
    """
    aln = make_aligned_seqs({"a": "GGG", "b": "GGC", "c": "AAC", "d": "AAA"})
    tree = make_tree("(a,b,(c,d));")

    fit_tree(aln, tree, Model(DnaModel.JC), 1)
    fit_tree(aln, tree, Model(DnaModel.JC), 2)

    with pytest.raises(IqTreeError):
        random_trees(2, TreeGenMode.BALANCED, 3, 1)
