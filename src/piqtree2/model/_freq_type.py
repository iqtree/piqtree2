import functools
from enum import Enum, unique

from typing_extensions import Self


@unique
class FreqType(Enum):
    """Types of base frequencies."""

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
        """The description of the FreqType.

        Returns
        -------
        str
            The description of the FreqType.

        """
        return self._descriptions()[self]
