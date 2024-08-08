from abc import ABC, abstractmethod
from typing import Optional


class RateModel(ABC):
    @abstractmethod
    def iqtree_str(self) -> str: ...


class RateType:
    def __init__(
        self,
        *,
        invariable_sites: bool = False,
        model: Optional[RateModel],
    ) -> None:
        self.invariable_sites = invariable_sites
        self.model = model

    def iqtree_str(self) -> str:
        rate_type_str = "+I" if self.invariable_sites else ""
        if self.model is None:
            return rate_type_str
        return rate_type_str + self.model.iqtree_str()


class DiscreteGammaModel(RateModel):
    def __init__(self, rate_categories: int = 4) -> None:
        self.rate_categories = rate_categories

    def iqtree_str(self) -> str:
        return f"+G{self.rate_categories}"


class FreeRateModel(RateModel):
    def __init__(self, rate_categories: int = 4) -> None:
        self.rate_categories = rate_categories

    def iqtree_str(self) -> str:
        return f"+R{self.rate_categories}"
