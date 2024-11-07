import pytest
from piqtree2.model import FreqType, get_freq_type


def test_number_of_descriptions() -> None:
    assert len(FreqType) == len(FreqType._descriptions())


def test_descriptions_exist() -> None:
    for freq_type in FreqType:
        # Raises an error if description not present
        _ = freq_type.description


@pytest.mark.parametrize(
    ("freq_type", "iqtree_str"),
    [
        (FreqType.F, "F"),
        (FreqType.FO, "FO"),
        (FreqType.F, "FQ"),
        ("F", "F"),
        ("FO", "FO"),
        ("FQ", "FQ"),
        ("+F", "F"),
        ("+FO", "FO"),
        ("+FQ", "FQ"),
    ],
)
def test_get_freq_type(freq_type: FreqType | str, iqtree_str: str) -> None:
    out = get_freq_type(freq_type)
    assert isinstance(out, FreqType)
    assert out.iqtree_str() == iqtree_str


@pytest.mark.parametrize(
    "freq_type",
    ["F0", "+F0", "+G", "+R9"],
)
def test_get_freq_type_name(freq_type: str) -> None:
    with pytest.raises(
        ValueError,
        match=f"Unknown state frequency type: {freq_type!r}",
    ):
        _ = get_freq_type(freq_type)
