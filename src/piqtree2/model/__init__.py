"""Models available in IQ-TREE."""

from ._freq_type import FreqType
from ._model import Model
from ._options import available_models
from ._rate_type import DiscreteGammaModel, FreeRateModel, RateModel, RateType
from ._substitution_model import AaModel, DnaModel, SubstitutionModel

__all__ = [
    "available_models",
    "AaModel",
    "DiscreteGammaModel",
    "DnaModel",
    "FreeRateModel",
    "FreqType",
    "Model",
    "RateModel",
    "RateType",
    "SubstitutionModel",
]
