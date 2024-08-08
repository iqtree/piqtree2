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
        """
        self.rate_categories = rate_categories

    def iqtree_str(self) -> str:
        return f"+R{self.rate_categories}"
