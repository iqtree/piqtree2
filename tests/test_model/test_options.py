# testing the display of functions
import pytest
from piqtree2 import available_models


@pytest.mark.parametrize("model_type", [None, "dna", "protein"])
def test_available_models(model_type):
    table = available_models(model_type)
    assert table.shape[0] > 0
