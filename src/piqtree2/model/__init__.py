"""Models available in IQ-TREE."""

from ._freq_type import FreqType
from ._model import Model
from ._options import available_models
from ._substitution_model import AaModel, DnaModel, SubstitutionModel

__all__ = [
    "available_models",
    "AaModel",
    "DnaModel",
    "FreqType",
    "Model",
    "SubstitutionModel",
]
