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
        freq_type: Optional[FreqType] = None,
        rate_type: Optional[RateType] = None,
    ) -> None:
        """Constructor for the model.

        Parameters
        ----------
        substitution_model : SubstitutionModel
            The substitution model to use
        freq_type : Optional[FreqType], optional
            Base frequency specification, by default None. (defaults
            to empirical base frequencies if not specified by model).
        rate_type : Optional[FreqType], optional
            Rate heterogeneity across sites model, by default
            no invariable sites, no Gamma, and no FreeRate.
        """
        self.substitution_model = substitution_model
        self.freq_type = freq_type
        self.rate_type = rate_type

    def __str__(self) -> str:
        """Convert the model into the IQ-TREE representation.

        Returns
        -------
        str
            The IQ-TREE representation of the mode.
        """
        freq_str = "" if self.freq_type is None else "+" + self.freq_type.value
        rate_str = "" if self.rate_type is None else self.rate_type.iqtree_str()
        return self.substitution_model.value + freq_str + rate_str
