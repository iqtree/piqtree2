import contextlib
import functools
from enum import Enum, unique


@unique
class FreqType(Enum):
    """Types of base frequencies."""

    F = "F"
    FO = "FO"
    FQ = "FQ"

    @staticmethod
    @functools.cache
    def _descriptions() -> dict["FreqType", str]:
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

    def iqtree_str(self) -> str:
        return self.value


def get_freq_type(name: str | FreqType) -> FreqType:
    """Return the FreqType enum for a given name.

    Parameters
    ----------
    name : str | FreqType
        Name of the frequency type.

    Returns
    -------
    FreqType
        The resolved FreqType Enum.

    Raises
    ------
    ValueError
        If the FreqType name cannot be resolved.

    """
    if isinstance(name, FreqType):
        return name

    name = name.lstrip("+")

    with contextlib.suppress(KeyError):
        return FreqType[name]

    msg = f"Unknown state frequency type: {name!r}"
    raise ValueError(msg)
