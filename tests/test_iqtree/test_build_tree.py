import piqtree2
import pytest
from cogent3 import load_aligned_seqs, make_tree
from piqtree2.model import (
    DiscreteGammaModel,
    DnaModel,
    FreeRateModel,
    FreqType,
    Model,
    RateType,
)


@pytest.fixture()
def four_otu(DATA_DIR):
    aln = load_aligned_seqs(DATA_DIR / "example.fasta", moltype="dna")
    aln = aln.take_seqs(["Human", "Chimpanzee", "Rhesus", "Mouse"])
    return aln.omit_gap_pos(allowed_gap_frac=0)


@pytest.mark.parametrize("dna_model", list(DnaModel))
@pytest.mark.parametrize("freq_type", list(FreqType))
@pytest.mark.parametrize("invariable_sites", [False, True])
@pytest.mark.parametrize(
    "rate_model",
    [
        None,
        DiscreteGammaModel(),
        FreeRateModel(),
        DiscreteGammaModel(6),
        FreeRateModel(6),
    ],
)
def test_build_tree(four_otu, dna_model, freq_type, invariable_sites, rate_model):
    expected = make_tree("(Human,Chimpanzee,(Rhesus,Mouse));")

    model = Model(
        dna_model,
        freq_type,
        RateType(invariable_sites=invariable_sites, model=rate_model),
    )

    got1 = piqtree2.build_tree(four_otu, model, rand_seed=1)
    got1 = got1.unrooted()
    assert expected.same_topology(got1.unrooted())

    # Should be similar for any seed
    got2 = piqtree2.build_tree(four_otu, model, rand_seed=None)
    got2 = got2.unrooted()
    assert expected.same_topology(got2)
