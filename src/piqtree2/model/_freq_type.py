from enum import Enum, unique
from typing import ClassVar


@unique
class FreqType(Enum):
    F = "F"
    FO = "FO"
    FQ = "FQ"

    _descriptions: ClassVar[dict["FreqType", str]] = {
        F: "Empirical state frequency observed from the data.",
        FO: "State frequency optimized by maximum-likelihood from the data. Note that this is with letter-O and not digit-0.",
        FQ: "Equal state frequency.",
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
