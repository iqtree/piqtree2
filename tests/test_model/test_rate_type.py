import pytest

from piqtree2.model import DiscreteGammaModel, FreeRateModel, RateModel, RateType, InvariantSitesModel


def test_rate_model_uninstantiable() -> None:
    with pytest.raises(TypeError):
        _ = RateModel()

@pytest.mark.xfail(reason="need to rewrite for purpose of building full model string")
@pytest.mark.parametrize(
    ("invariable_sites", "rate_model", "iqtree_str"),
    [
        (False, None, ""),
        (True, None, "+I"),
        (False, DiscreteGammaModel(), "+G"),
        (True, DiscreteGammaModel(), "+I+G"),
        (False, FreeRateModel(), "+R"),
        (True, FreeRateModel(), "+I+R"),
        (False, DiscreteGammaModel(8), "+G8"),
        (True, DiscreteGammaModel(8), "+I+G8"),
        (False, FreeRateModel(8), "+R8"),
        (True, FreeRateModel(8), "+I+R8"),
        (False, DiscreteGammaModel(42), "+G42"),
        (True, DiscreteGammaModel(42), "+I+G42"),
        (False, FreeRateModel(42), "+R42"),
        (True, FreeRateModel(42), "+I+R42"),
    ],
)
def test_invariable_sites(
    invariable_sites: bool,
    rate_model: RateModel | None,
    iqtree_str: str,
) -> None:
    model = RateType(model=rate_model)
    invariant = InvariantSitesModel().iqtree_str() if invariable_sites else ""
    got = invariant + model.iqtree_str()
    assert got == iqtree_str

    if rate_model is None:
        model = RateType(invariable_sites=invariable_sites)
        assert model.iqtree_str() == iqtree_str

    if not invariable_sites:
        model = RateType(model=rate_model)
        assert model.iqtree_str() == iqtree_str
