"""Models available in IQ-TREE."""

from ._freq_type import FreqType, get_freq_type
from ._model import Model
from ._options import available_freq_type, available_models, available_rate_type
from ._rate_type import (
    DiscreteGammaModel,
    FreeRateModel,
    RateModel,
    RateType,
    get_rate_type,
)
from ._substitution_model import (
    AaModel,
    DnaModel,
    SubstitutionModel,
    get_substitution_model,
)

__all__ = [
    "AaModel",
    "DiscreteGammaModel",
    "DnaModel",
    "FreeRateModel",
    "FreqType",
    "Model",
    "RateModel",
    "RateType",
    "SubstitutionModel",
    "available_freq_type",
    "available_models",
    "available_rate_type",
    "get_freq_type",
    "get_rate_type",
    "get_substitution_model",
]
