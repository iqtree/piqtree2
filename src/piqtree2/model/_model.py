from piqtree2.model._freq_type import get_freq_type
from piqtree2.model._rate_type import get_rate_type
from piqtree2.model._substitution_model import get_model


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

        self.freq_type = get_freq_type(freq_type) if freq_type else None
        # self.rate_type = get_rate_type(rate_type) if rate_type else None
        # self.invariant_sites = (
        #     get_rate_type(rate_type, invariant_sites)
        #     if invariant_sites or rate_type is not None
        #     else None
        # )

    def __str__(self) -> str:
        """Convert the model into the IQ-TREE representation.

        Returns
        -------
        str
            The IQ-TREE representation of the mode.
        """
        iqtree_extra_args = filter(
            lambda x: x is not None,
            (self.freq_type,),  # self.rate_type, self.invariant_sites),
        )
        return "+".join(
            x.iqtree_str() for x in [self.substitution_model, *iqtree_extra_args]
        )
