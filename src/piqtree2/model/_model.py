from piqtree2.model._freq_type import FreqType
from piqtree2.model._rate_type import RateType, get_rate_type
from piqtree2.model._substitution_model import SubstitutionModel, get_model


class Model:
    """Specification for substitution models.

    Stores the substitution model with base frequency settings.
    """

    def __init__(
        self,
        substitution_model: str,
        freq_type: str | None = None,
        rate_type: str | None = None,
        *,
        invariant_sites: bool = False,
    ) -> None:
        """Constructor for the model.

        Parameters
        ----------
        substitution_model : SubstitutionModel
            The substitution model to use
        freq_type : Optional[FreqType], optional
            State frequency specification, by default None. (defaults
            to empirical base frequencies if not specified by model).
        rate_type : Optional[FreqType], optional
            Rate heterogeneity across sites model, by default
            no invariable sites, no Gamma, and no FreeRate.
        """
        self.substitution_model = get_model(substitution_model)

        self.freq_type = FreqType[freq_type] if freq_type else ""
        self.rate_type = get_rate_type(rate_type) if rate_type else ""
        self.invariant_sites = get_rate_type("I") if invariant_sites else ""

    def __str__(self) -> str:
        """Convert the model into the IQ-TREE representation.

        Returns
        -------
        str
            The IQ-TREE representation of the mode.
        """
        model = self.substitution_model.value
        freq_type = f"+{self.freq_type.value}" if self.freq_type else self.freq_type
        return "".join(
            str(m)
            for m in (model, self.invariant_sites, self.rate_type, freq_type)
            if m
        )
