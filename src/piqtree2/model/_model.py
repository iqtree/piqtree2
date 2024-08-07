from piqtree2.model._freq_type import FreqType
from piqtree2.model._substitution_model import SubstitutionModel


class Model:
    def __init__(
        self,
        substitution_model: SubstitutionModel,
        freq_type: FreqType = FreqType.F,
    ) -> None:
        self.substitution_model = substitution_model
        self.freq_type = freq_type

    def __str__(self) -> str:
        return self.substitution_model.value + "+" + self.freq_type.value
