from piqtree2.model import FreqType


def test_number_of_descriptions():
    assert len(FreqType) == len(FreqType._descriptions())


def test_descriptions_exist():
    for freq_type in FreqType:
        # Raises an error if description not present
        _ = freq_type.description
