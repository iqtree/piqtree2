"""Models available in IQ-TREE."""

from ._freq_type import FreqType
from ._model import Model
from ._options import available_freq_type, available_models, available_rate_type
from ._rate_type import DiscreteGammaModel, FreeRateModel, RateModel, RateType
from ._substitution_model import (
    AaModel,
    DnaModel,
    SubstitutionModel,
    get_model,
)

__all__ = [
    "available_freq_type",
    "available_models",
    "available_rate_type",
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
