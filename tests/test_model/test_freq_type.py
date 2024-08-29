from piqtree2.model import FreqType


def test_number_of_descriptions() -> None:
    assert len(FreqType) == len(FreqType._descriptions())


def test_descriptions_exist() -> None:
    for freq_type in FreqType:
        # Raises an error if description not present
        _ = freq_type.description
