from typing import Any

import pytest
from piqtree2.exceptions import ParseIqTreeError
from piqtree2.iqtree._tree import _process_tree_yaml


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


def test_newick_not_in_candidates(newick_not_in_candidates: dict[str, Any]) -> None:
    with pytest.raises(ParseIqTreeError):
        _ = _process_tree_yaml(newick_not_in_candidates, ["a", "b", "c"])
