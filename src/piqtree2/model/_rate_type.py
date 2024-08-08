from abc import ABC, abstractmethod
from typing import Optional


class RateModel(ABC):
    """Base class for rate models."""

    @abstractmethod
    def iqtree_str(self) -> str:
        """Convert to an iqtree settings string.

        Returns
        -------
        str
            String parsable by IQ-TREE for the rate heterogeneity model.
        """


class RateType:
    def __init__(
        self,
        *,
        invariable_sites: bool = False,
        model: Optional[RateModel],
    ) -> None:
        """Rate heterogeneity across sites model.

        Parameters
        ----------
        model : Optional[RateModel]
            Discrete Gamma Model or FreeRate Model.
        invariable_sites : bool, optional
            Invariable Sites Model.
        """
        self.invariable_sites = invariable_sites
        self.model = model

    def iqtree_str(self) -> str:
        """Convert to an iqtree settings string.

        Returns
        -------
        str
            String parsable by IQ-TREE for the rate heterogeneity model.
        """
        rate_type_str = "+I" if self.invariable_sites else ""
        if self.model is None:
            return rate_type_str
        return rate_type_str + self.model.iqtree_str()


class DiscreteGammaModel(RateModel):
    def __init__(self, rate_categories: int = 4) -> None:
        """Discrete Gamma Model.

        Parameters
        ----------
        rate_categories : int, optional
            The number of rate categories, by default 4

        References
        ----------
        .. [1] Yang, Ziheng. "Maximum likelihood phylogenetic estimation from
           DNA sequences with variable rates over sites: approximate methods."
           Journal of Molecular evolution 39 (1994): 306-314.
        """
        self.rate_categories = rate_categories

    def iqtree_str(self) -> str:
        return f"+G{self.rate_categories}"


class FreeRateModel(RateModel):
    def __init__(self, rate_categories: int = 4) -> None:
        """FreeRate Model.

        Parameters
        ----------
        rate_categories : int, optional
            The number of rate categories, by default 4

        References
        ----------
        .. [1] Yang, Ziheng. "A space-time process model for the evolution of
           DNA sequences." Genetics 139.2 (1995): 993-1005.
        .. [2] Soubrier, Julien, et al. "The influence of rate heterogeneity
           among sites on the time dependence of molecular rates." Molecular
           biology and evolution 29.11 (2012): 3345-3358.
        """
        self.rate_categories = rate_categories

    def iqtree_str(self) -> str:
        return f"+R{self.rate_categories}"
