import pyiqtree

def test_RF_distance():
    tree1 = "(A,B,(C,D));"
    tree2 = "(A,C,(B,D));"
    assert pyiqtree.calculate_RF_distance(tree1, tree2) == 2  # Replace with actual expected value
