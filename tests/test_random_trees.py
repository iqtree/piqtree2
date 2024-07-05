import piqtree2
import pytest


@pytest.mark.parametrize("num_taxa", [10, 50, 100])
@pytest.mark.parametrize("num_trees", [1, 10, 20])
@pytest.mark.parametrize("tree_mode", list(piqtree2.TreeGenMode))
def test_random_trees(
    num_taxa: int,
    tree_mode: piqtree2.TreeGenMode,
    num_trees: int,
) -> None:
    trees = piqtree2.random_trees(
        num_taxa,
        tree_mode,
        num_trees,
        rand_seed=1,
    )
    assert len(trees) == num_trees

    for tree in trees:
        assert len(tree.tips()) == num_taxa
