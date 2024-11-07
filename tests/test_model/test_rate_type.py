import pytest

from piqtree2.model import (
    DiscreteGammaModel,
    FreeRateModel,
    RateModel,
    RateType,
    get_rate_type,
)


def test_rate_model_uninstantiable() -> None:
    with pytest.raises(TypeError):
        _ = RateModel()


@pytest.mark.parametrize(
    ("invariant_sites", "rate_model", "iqtree_str"),
    [
        (False, None, ""),
        (True, None, "I"),
        (False, DiscreteGammaModel(), "G"),
        (True, DiscreteGammaModel(), "I+G"),
        (False, FreeRateModel(), "R"),
        (True, FreeRateModel(), "I+R"),
        (False, DiscreteGammaModel(8), "G8"),
        (True, DiscreteGammaModel(8), "I+G8"),
        (False, FreeRateModel(8), "R8"),
        (True, FreeRateModel(8), "I+R8"),
        (False, DiscreteGammaModel(42), "G42"),
        (True, DiscreteGammaModel(42), "I+G42"),
        (False, FreeRateModel(42), "R42"),
        (True, FreeRateModel(42), "I+R42"),
    ],
)
def test_invariant_sites(
    invariant_sites: bool,
    rate_model: RateModel | None,
    iqtree_str: str,
) -> None:
    model = get_rate_type(invariant_sites=invariant_sites, rate_model=rate_model)
    assert model.iqtree_str() == iqtree_str

    if rate_model is None:
        model = get_rate_type(invariant_sites=invariant_sites)
        assert model.iqtree_str() == iqtree_str

    if not invariant_sites:
        model = get_rate_type(rate_model=rate_model)
        assert model.iqtree_str() == iqtree_str
