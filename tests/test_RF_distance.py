import pyiqtree

def test_RF_distance():
    tree1 = "(A,B,(C,D));"
    tree2 = "(A,C,(B,D));"
    assert pyiqtree.RF_distance(tree1, tree2) == expected_distance  # Replace with actual expected value
