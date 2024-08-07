from piqtree2.model._freq_type import FreqType
from piqtree2.model._substitution_model import SubstitutionModel


class Model:
    """Specification for substitution models.

    Stores the substitution model with base frequency settings.
    """

    def __init__(
        self,
        substitution_model: SubstitutionModel,
        freq_type: FreqType = FreqType.F,
    ) -> None:
        """Constructor for the model.

        Parameters
        ----------
        substitution_model : SubstitutionModel
            The substitution model to use
        freq_type : FreqType, optional
            Base frequency specification, by default FreqType.F
        """
        self.substitution_model = substitution_model
        self.freq_type = freq_type

    def __str__(self) -> str:
        """Convert the model into the IQ-TREE representation.

        Returns
        -------
        str
            The IQ-TREE representation of the mode.
        """
        return self.substitution_model.value + "+" + self.freq_type.value
