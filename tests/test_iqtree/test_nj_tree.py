from cogent3 import ArrayAlignment, make_tree

from piqtree import jc_distances, nj_tree


def test_nj_tree(five_otu: ArrayAlignment) -> None:
    expected = make_tree("(((Human, Chimpanzee), Rhesus), Manatee, Dugong);")

    dists = jc_distances(five_otu)
    actual = nj_tree(dists)

    assert expected.same_topology(actual)
