from typing import Any

import pytest

from piqtree2.exceptions import ParseIqTreeError
from piqtree2.iqtree._tree import _process_tree_yaml


@pytest.fixture
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
            "newick": "(0:0.0068556288,1:0.0026699620,(2:0.0213509070,3:0.2948603704):0.01524055279);",
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


@pytest.fixture
def non_lie_dna_with_rate_model() -> dict[str, Any]:
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
        "RateGammaInvar": {"gamma_shape": 1.698497993, "p_invar": 1.002841144e-06},
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


@pytest.fixture
def lie_dna_model() -> dict[str, Any]:
    return {
        "CandidateSet": {
            0: "-6606.82337571 ((0:0.0058632731,(2:0.0225450645,3:0.3055011501):0.01414755595):2.340509431e-06,1:0.0026433577):0;",
            1: "-6606.82337581 (0:0.0058609304,(1:0.0026456850,(2:0.0225450645,3:0.3055011501):0.01414755618):2.340509431e-06):0;",
            2: "-6606.82337581 ((0:0.0058632731,1:0.0026456850):2.340509431e-06,(2:0.0225450645,3:0.3055011501):0.01414520892):0;",
            3: "-6606.82337594 (((0:0.0058630055,1:0.0026461740):0.01414791335,2:0.0225451031):0.1178978025,3:0.1876035160):0;",
            4: "-6628.65519886 (0:0.0000023102,((1:0.0027556399,3:0.3193110364):2.07651076e-06,2:0.0366286909):0.005770021808):1e-06;",
            5: "-6628.70596445 (0:0.0000022647,((1:0.0027641463,2:0.0366284785):2.43434433e-06,3:0.3193357780):0.005401508376):1e-06;",
        },
        "ModelLieMarkovRY2.2b": {
            "model_parameters": 0.4841804549,
            "state_freq": "0.25, 0.25, 0.25, 0.25",
        },
        "PhyloTree": {
            "newick": "((0:0.0058632731,(2:0.0225450645,3:0.3055011501):0.01414755595):2.340509431e-06,1:0.0026433577):0;",
        },
        "StopRule": {
            "curIteration": 101,
            "start_real_time": 1729226726,
            "time_vec": None,
        },
        "boot_consense_logl": 0,
        "contree_rfdist": -1,
        "finished": True,
        "finishedCandidateSet": True,
        "finishedModelFinal": True,
        "finishedModelInit": True,
        "initTree": "(0:0.0063001853,1:0.0022115739,(2:0.0203850510,3:0.3497395366):0.01883712169);",
        "iqtree": {"seed": 1, "start_time": 1729226725, "version": "2.3.6.lib"},
    }


def test_newick_not_in_candidates(newick_not_in_candidates: dict[str, Any]) -> None:
    with pytest.raises(ParseIqTreeError):
        _ = _process_tree_yaml(
            newick_not_in_candidates,
            ["a", "b", "c"],
        )


def test_non_lie_dna_with_rate_model(
    non_lie_dna_with_rate_model: dict[str, Any],
) -> None:
    # test parsing yaml file containing fits from non-Lie DnaModel and rate heterogeneity model
    edge_params = {
        "rates": {
            "A/C": 1.0,
            "A/G": 3.82025079,
            "A/T": 1.0,
            "C/G": 1.0,
            "C/T": 3.82025079,
            "G/T": 1,
        },
        "mprobs": {
            "A": 0.3628523161,
            "C": 0.1852938562,
            "G": 0.2173913044,
            "T": 0.2344625233,
        },
    }
    rate_params = {"gamma_shape": 1.698497993, "p_invar": 1.002841144e-06}
    tree = _process_tree_yaml(non_lie_dna_with_rate_model, ["a", "b", "c", "d"])
    assert tree.params["edge_pars"] == edge_params
    assert tree.params["RateGammaInvar"] == rate_params


def test_non_lie_dna_model_motif_absent(
    non_lie_dna_with_rate_model: dict[str, Any],
) -> None:
    non_lie_dna_with_rate_model["ModelDNA"].pop("state_freq")
    with pytest.raises(ParseIqTreeError):
        _ = _process_tree_yaml(non_lie_dna_with_rate_model, ["a", "b", "c", "d"])


def test_non_lie_dna_model_rate_absent(
    non_lie_dna_with_rate_model: dict[str, Any],
) -> None:
    non_lie_dna_with_rate_model["ModelDNA"].pop("rates")
    with pytest.raises(ParseIqTreeError):
        _ = _process_tree_yaml(non_lie_dna_with_rate_model, ["a", "b", "c", "d"])


def test_lie_dna_model(
    lie_dna_model: dict[str, Any],
) -> None:
    # test parsing yaml file containing fits from Lie DnaModel
    model_parameters = {
        "model_parameters": 0.4841804549,
        "mprobs": {"A": 0.25, "C": 0.25, "G": 0.25, "T": 0.25},
    }
    tree = _process_tree_yaml(lie_dna_model, ["a", "b", "c", "d"])
    assert tree.params["ModelLieMarkovRY2.2b"] == model_parameters


def test_lie_dna_model_motif_absent(
    lie_dna_model: dict[str, Any],
) -> None:
    lie_dna_model["ModelLieMarkovRY2.2b"].pop("state_freq")
    with pytest.raises(ParseIqTreeError):
        _ = _process_tree_yaml(lie_dna_model, ["a", "b", "c", "d"])
