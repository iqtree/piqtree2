import pytest

from piqtree2.model import AaModel, DnaModel


@pytest.mark.parametrize("model_class", [DnaModel, AaModel])
def test_number_of_descriptions(
    model_class: type[DnaModel] | type[AaModel],
) -> None:
    assert len(model_class) == len(model_class._descriptions())


@pytest.mark.parametrize("model_class", [DnaModel, AaModel])
def test_descriptions_exist(model_class: type[DnaModel] | type[AaModel]) -> None:
    for model in model_class:
        # Raises an error if description not present
        _ = model.description


@pytest.mark.parametrize(
    ("model_class", "model_type"),
    [(DnaModel, "nucleotide"), (AaModel, "protein")],
)
def test_model_type(
    model_class: type[DnaModel] | type[AaModel],
    model_type: str,
) -> None:
    assert model_class.model_type() == model_type

    for model in model_class:
        assert model.model_type() == model_type
