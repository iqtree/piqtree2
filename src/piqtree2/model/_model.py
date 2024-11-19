from piqtree2.model._freq_type import FreqType, get_freq_type
from piqtree2.model._rate_type import RateModel, get_rate_type
from piqtree2.model._substitution_model import SubstitutionModel, get_substitution_model


class Model:
    """Specification for substitution models.

    Stores the substitution model with base frequency settings.
    """

    def __init__(
        self,
        submod_type: str | SubstitutionModel,
        freq_type: str | FreqType | None = None,
        rate_model: str | RateModel | None = None,
        *,
        invariant_sites: bool = False,
    ) -> None:
        """Constructor for the model.

        Parameters
        ----------
        submod_type : str |SubstitutionModel
            The substitution model to use
        freq_type : str | FreqType | None, optional
            State frequency specification, by default None. (defaults
            to empirical base frequencies if not specified by model).
        rate_model : str | RateModel | None, optional
            Rate heterogeneity across sites model, by default
            no Gamma, and no FreeRate.
        invariant_sites : bool, optional
            Invariable sites.
        """
        self.submod_type = get_substitution_model(submod_type)
        self.freq_type = get_freq_type(freq_type) if freq_type else None
        self.rate_type = (
            get_rate_type(rate_model, invariant_sites=invariant_sites)
            if rate_model is not None or invariant_sites
            else None
        )

    def __str__(self) -> str:
        """Convert the model into the IQ-TREE representation.

        Returns
        -------
        str
            The IQ-TREE representation of the mode.
        """
        iqtree_extra_args = (
            x for x in (self.freq_type, self.rate_type) if x is not None
        )
        return "+".join(x.iqtree_str() for x in [self.submod_type, *iqtree_extra_args])

    @property
    def rate_model(self) -> RateModel | None:
        return self.rate_type.rate_model if self.rate_type else None

    @property
    def invariant_sites(self) -> bool:
        return self.rate_type.invariant_sites if self.rate_type else False
