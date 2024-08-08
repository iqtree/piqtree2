from typing import Optional

from piqtree2.model._freq_type import FreqType
from piqtree2.model._rate_type import RateType
from piqtree2.model._substitution_model import SubstitutionModel


class Model:
    """Specification for substitution models.

    Stores the substitution model with base frequency settings.
    """

    def __init__(
        self,
        substitution_model: SubstitutionModel,
        freq_type: Optional[FreqType] = FreqType.F,
        rate_type: Optional[RateType] = None,
    ) -> None:
        """Constructor for the model.

        Parameters
        ----------
        substitution_model : SubstitutionModel
            The substitution model to use
        freq_type : Optional[FreqType], optional
            Base frequency specification, by default FreqType.F
        rate_type : Optional[FreqType], optional
            Rate heterogeneity across sites model, by default
            no invariable sites, no Gamma, and no FreeRate
        """
        self.substitution_model = substitution_model
        self.freq_type = FreqType.F if freq_type is None else freq_type
        self.rate_type = (
            RateType(invariable_sites=False, model=None)
            if rate_type is None
            else rate_type
        )

    def __str__(self) -> str:
        """Convert the model into the IQ-TREE representation.

        Returns
        -------
        str
            The IQ-TREE representation of the mode.
        """
        return (
            self.substitution_model.value
            + "+"
            + self.freq_type.value
            + self.rate_type.iqtree_str()
        )
