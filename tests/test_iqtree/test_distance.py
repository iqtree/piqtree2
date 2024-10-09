from cogent3 import ArrayAlignment

from piqtree2 import jc_distances


def test_mash_distance(five_otu: ArrayAlignment) -> None:
    dists = jc_distances(five_otu)

    assert (
        dists["Human", "Chimpanzee"] < dists["Human", "Dugong"]
    )  # chimpanzee closer than rhesus
    assert (
        dists["Human", "Rhesus"] < dists["Human", "Manatee"]
    )  # rhesus closer than manatee
    assert (
        dists["Human", "Rhesus"] < dists["Human", "Dugong"]
    )  # rhesus closer than dugong

    assert (
        dists["Chimpanzee", "Rhesus"] < dists["Chimpanzee", "Manatee"]
    )  # rhesus closer than manatee
    assert (
        dists["Chimpanzee", "Rhesus"] < dists["Chimpanzee", "Dugong"]
    )  # rhesus closer than dugong

    assert (
        dists["Manatee", "Dugong"] < dists["Manatee", "Rhesus"]
    )  # dugong closer than rhesus
