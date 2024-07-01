import piqtree2
import pytest


@pytest.mark.parametrize("num_taxa", [10, 50, 100])
@pytest.mark.parametrize("num_trees", [1, 10, 20])
def test_random_trees(num_taxa: int, num_trees: int) -> None:
    trees = piqtree2.random_trees(
        num_taxa,
        piqtree2.TreeGenMode.UNIFORM,
        num_trees,
        rand_seed=1,
    )
    assert len(trees) == num_trees

    for tree in trees:
        assert len(tree.tips()) == num_taxa
