# testing the display of functions

from typing import Literal

import pytest

from piqtree2 import available_freq_type, available_models, available_rate_type
from piqtree2.model import AaModel, DnaModel, FreqType, SubstitutionModel
from piqtree2.model._rate_type import ALL_BASE_RATE_TYPES


@pytest.mark.parametrize(
    ("model_class", "model_type"),
    [(None, None), (DnaModel, "dna"), (AaModel, "protein")],
)
def test_num_available_models(
    model_class: type[SubstitutionModel] | None,
    model_type: Literal["dna", "protein"] | None,
) -> None:
    table = available_models(model_type)
    total_models = (
        len(DnaModel) + len(AaModel) if model_class is None else len(model_class)
    )
    assert total_models > 0
    assert table.shape[0] == total_models
    assert table._repr_policy["head"] == table.shape[0]


def test_num_available_models_not_show_all() -> None:
    table = available_models(show_all=False)
    assert table._repr_policy["head"] != table.shape[0]


@pytest.mark.parametrize(
    ("model_fetch", "model_type"),
    [(None, None), ("dna", "nucleotide"), ("protein", "protein")],
)
def test_available_models_types(
    model_fetch: Literal["dna", "protein"] | None,
    model_type: str | None,
) -> None:
    table = available_models(model_fetch)

    if model_type is None:
        for check_model_type in table[:, 0]:
            assert check_model_type[0] in ["nucleotide", "protein"]
    else:
        for check_model_type in table[:, 0]:
            assert check_model_type[0] == model_type


def test_num_freq_type() -> None:
    table = available_freq_type()
    total_freq_types = len(FreqType)

    assert total_freq_types > 0
    assert table.shape[0] == total_freq_types


def test_num_rate_type() -> None:
    table = available_rate_type()
    total_rate_types = len(ALL_BASE_RATE_TYPES)

    assert total_rate_types > 0
    assert table.shape[0] == total_rate_types
