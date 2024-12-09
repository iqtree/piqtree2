import pytest

from piqtree2.iqtree._model_finder import ModelFinderResult, ModelResultValue


def test_model_result_value_from_string():
    val = "123.45 10 0.678"
    result = ModelResultValue.from_string(val)
    assert result.lnL == 123.45
    assert result.nfp == 10
    assert result.tree_length == 0.678


@pytest.mark.parametrize(
    "bad_val",
    [
        "123.45.00 10 0.678",  # invalid float
        "123.45 10 10 0.678",  # too many values
        "123.45 10",  # too few values
    ],
)
def test_model_result_value_from_bad_string(bad_val):
    with pytest.raises(ValueError):
        _ = ModelResultValue.from_string(bad_val)


@pytest.mark.parametrize("model", ["GTR+F", "GTR+F+G"])
def test_model_finder_result(model):
    raw_data = {
        model: "123.45 10 0.678",
        "best_model_AIC": model,
        "best_model_AICc": model,
        "best_model_BIC": model,
    }

    result = ModelFinderResult("test", raw_data)

    assert isinstance(result.model_stats[model], ModelResultValue)
    assert result.model_stats[model].lnL == 123.45
    assert result.model_stats[model].nfp == 10
    assert result.model_stats[model].tree_length == 0.678
