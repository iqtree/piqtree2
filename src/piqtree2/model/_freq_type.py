import functools
from enum import Enum, unique

from typing_extensions import Self


@unique
class FreqType(Enum):
    F = "F"
    FO = "FO"
    FQ = "FQ"

    @staticmethod
    @functools.cache
    def _descriptions() -> dict[Self, str]:
        return {
            FreqType.F: "Empirical state frequency observed from the data.",
            FreqType.FO: "State frequency optimized by maximum-likelihood from the data. Note that this is with letter-O and not digit-0.",
            FreqType.FQ: "Equal state frequency.",
        }

    @property
    def description(self) -> str:
        """The model's description.

        Returns
        -------
        str
            The model's description.

        """
        return self._descriptions()[self]
