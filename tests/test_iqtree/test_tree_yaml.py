from typing import Any

import pytest
from piqtree2.exceptions import ParseIqTreeError
from piqtree2.iqtree._tree import _process_tree_yaml
from piqtree2.model import DnaModel, Model


@pytest.fixture()
def newick_not_in_candidates() -> dict[str, Any]:
    # The newick string does not appear in the CandidateSet
    return {
        "CandidateSet": {
            0: "-6740.63608299 (0:0.0058556288,1:0.0026699620,(2:0.0213509070,3:0.2948603704):0.01524055279);",
            1: "-6771.38674814 (0:0.0058881129,(1:0.0021755411,3:0.3099373687):0.0002171837668,2:0.0365212662);",
            2: "-6771.4094654 (0:0.0058966179,(1:0.0027044780,2:0.0365855065):2.43434433e-06,3:0.3102579188);",
        },
        "ModelDNA": {"rates": "1, 1, 1, 1, 1, 1"},
        "PhyloTree": {
            "newick": "(0:0.0058556289,1:0.0026699620,(2:0.0213509070,3:0.2948603704):0.01524055279);",
        },
        "StopRule": {
            "curIteration": 101,
            "start_real_time": 1722475286,
            "time_vec": None,
        },
        "boot_consense_logl": 0,
        "contree_rfdist": -1,
        "finished": True,
        "finishedCandidateSet": True,
        "finishedModelFinal": True,
        "finishedModelInit": True,
        "initTree": "(0:0.0063001853,1:0.0022115739,(2:0.0203850510,3:0.3497395366):0.01883712169);",
        "iqtree": {
            "seed": 1954151673,
            "start_time": 1722475285,
            "version": "2.3.5.lib",
        },
    }


@pytest.fixture()
def standard_yaml():
    return {
        "CandidateSet": {
            0: "-6736.94578464 (0:0.0063211201,1:0.0029675780,(2:0.0228519739,3:0.3072009029):0.01373649616);",
            1: "-6757.78815651 (0:0.0063607954,(1:0.0030079874,2:0.0365597715):2.296825575e-06,3:0.3208135518);",
            2: "-6758.07765021 (0:0.0063826033,(1:0.0021953253,3:0.3207201830):0.0001145372551,2:0.0365362763);",
        },
        "ModelDNA": {
            "rates": "1, 3.82025079, 1, 1, 3.82025079, 1",
            "state_freq": "0.3628523161, 0.1852938562, 0.2173913044, 0.2344625233",
        },
        "PhyloTree": {
            "newick": "(0:0.0063211201,1:0.0029675780,(2:0.0228519739,3:0.3072009029):0.01373649616);",
        },
        "StopRule": {
            "curIteration": 101,
            "start_real_time": 1724397157,
            "time_vec": None,
        },
        "boot_consense_logl": 0,
        "contree_rfdist": -1,
        "finished": True,
        "finishedCandidateSet": True,
        "finishedModelFinal": True,
        "finishedModelInit": True,
        "initTree": "(0:0.0063680036,1:0.0026681490,(2:0.0183861083,3:0.3034074996):0.01838610827);",
        "iqtree": {"seed": 95633264, "start_time": 1724397157, "version": "2.3.6.lib"},
    }


def test_newick_not_in_candidates(newick_not_in_candidates: dict[str, Any]) -> None:
    with pytest.raises(ParseIqTreeError):
        _ = _process_tree_yaml(
            newick_not_in_candidates, ["a", "b", "c"], Model(DnaModel.JC),
        )


def test_motif_params(standard_yaml):
    params = {
        "mprobs": {
            "A": 0.3628523161,
            "C": 0.1852938562,
            "G": 0.2173913044,
            "T": 0.2344625233,
        },
    }
    tree = _process_tree_yaml(standard_yaml, ["a", "b", "c", "d"], Model(DnaModel.HKY))
    for vector in tree.get_edge_vector():
        for k, v in params.items():
            assert k in vector.params
            assert vector.params[k] == v


def test_rate_params(standard_yaml):
    params = {"kappa": 3.82025079}
    tree = _process_tree_yaml(standard_yaml, ["a", "b", "c", "d"], Model(DnaModel.HKY))
    vectors = tree.get_edge_vector()
    for vector in vectors[:-1]:  # skip the root
        for k, v in params.items():
            assert k in vector.params
            assert vector.params[k] == v
