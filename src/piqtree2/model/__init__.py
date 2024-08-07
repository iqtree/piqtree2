"""Models available in IQ-TREE."""

from ._freq_type import FreqType
from ._model import AaModel, DnaModel, SubstitutionModel
from ._options import available_models

__all__ = ["available_models", "AaModel", "DnaModel", "FreqType", "SubstitutionModel"]
