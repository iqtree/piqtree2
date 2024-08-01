# testing the display of functions
import pytest
from piqtree2 import available_models
from piqtree2.model import AaModel, DnaModel


@pytest.mark.parametrize(
    ("model_class", "model_type"),
    [(None, None), (DnaModel, "dna"), (AaModel, "protein")],
)
def test_num_available_models(model_class, model_type):
    table = available_models(model_type)
    total_models = (
        len(DnaModel) + len(AaModel) if model_class is None else len(model_class)
    )
    assert total_models > 0
    assert table.shape[0] == total_models


@pytest.mark.parametrize(
    ("model_fetch", "model_type"),
    [(None, None), ("dna", "nucleotide"), ("protein", "protein")],
)
def test_available_models_types(model_fetch, model_type):
    table = available_models(model_fetch)

    if model_type is None:
        for check_model_type in table[:, 0]:
            assert check_model_type[0] in ["nucleotide", "protein"]
    else:
        for check_model_type in table[:, 0]:
            assert check_model_type[0] == model_type
