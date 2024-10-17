from typing import Optional

import pytest
from cogent3 import ArrayAlignment, make_tree

import piqtree2
from piqtree2.model import (
    DiscreteGammaModel,
    DnaModel,
    FreeRateModel,
    FreqType,
    Model,
    RateModel,
    RateType,
)


def init_model(
    dna_model: DnaModel,
    freq_type: Optional[FreqType] = None,
    invariable_sites: Optional[bool] = None,
    rate_model: Optional[RateModel] = None,
) -> Model:

    return Model(
        dna_model,
        freq_type,
        RateType(invariable_sites=invariable_sites, model=rate_model),
    )


@pytest.mark.parametrize("dna_model", list(DnaModel)[:22])
@pytest.mark.parametrize("freq_type", list(FreqType))
def test_non_lie_build_tree(
    four_otu: ArrayAlignment,
    dna_model: DnaModel,
    freq_type: FreqType,
) -> None:
    expected = make_tree("(Human,Chimpanzee,(Rhesus,Mouse));")
    model = init_model(dna_model, freq_type)

    got1 = piqtree2.build_tree(four_otu, model, rand_seed=1)
    got1 = got1.unrooted()
    # Check topology
    assert expected.same_topology(got1.unrooted())
    # Check if branch lengths exist
    assert all("length" in v.params for v in got1.get_edge_vector())

    # Should be similar for any seed
    got2 = piqtree2.build_tree(four_otu, model, rand_seed=None)
    got2 = got2.unrooted()
    assert expected.same_topology(got2)
    assert all("length" in v.params for v in got2.get_edge_vector())


@pytest.mark.parametrize("dna_model", list(DnaModel)[22:])
def test_lie_build_tree(four_otu: ArrayAlignment, dna_model: DnaModel) -> None:
    expected = make_tree("(Human,Chimpanzee,(Rhesus,Mouse));")
    model = init_model(dna_model)

    got1 = piqtree2.build_tree(four_otu, model, rand_seed=1)
    got1 = got1.unrooted()
    # Check topology
    assert expected.same_topology(got1.unrooted())
    # Check if branch lengths exist
    assert all("length" in v.params for v in got1.get_edge_vector())

    # Should be similar for any seed
    got2 = piqtree2.build_tree(four_otu, model, rand_seed=None)
    got2 = got2.unrooted()
    assert expected.same_topology(got2)
    assert all("length" in v.params for v in got2.get_edge_vector())


@pytest.mark.parametrize("dna_model", list(DnaModel)[:5])
@pytest.mark.parametrize("invariable_sites", [False, True])
@pytest.mark.parametrize(
    "rate_model",
    [
        None,
        DiscreteGammaModel(),
        FreeRateModel(),
        DiscreteGammaModel(6),
        FreeRateModel(6),
    ],
)
def test_rate_model_build_tree(
    four_otu: ArrayAlignment,
    dna_model: DnaModel,
    invariable_sites: Optional[bool],
    rate_model: RateModel,
) -> None:
    expected = make_tree("(Human,Chimpanzee,(Rhesus,Mouse));")
    model = init_model(
        dna_model,
        invariable_sites=invariable_sites,
        rate_model=rate_model,
    )

    got1 = piqtree2.build_tree(four_otu, model, rand_seed=1)
    got1 = got1.unrooted()
    # Check topology
    assert expected.same_topology(got1.unrooted())
    # Check if branch lengths exist
    assert all("length" in v.params for v in got1.get_edge_vector())

    # Should be similar for any seed
    got2 = piqtree2.build_tree(four_otu, model, rand_seed=None)
    got2 = got2.unrooted()
    assert expected.same_topology(got2)
    assert all("length" in v.params for v in got2.get_edge_vector())
