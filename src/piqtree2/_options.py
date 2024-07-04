# convenience functions for showing user facing options and their descriptions
import functools
from typing import Optional

from cogent3 import _Table, make_table

_dna_models = {
    "Abbreviation": [
        "JC",
        "F81",
        "K80",
        "HKY",
        "TN",
        "TNe",
        "K81",
        "K81u",
        "TPM2",
        "TPM2u",
        "TPM3",
        "TPM3u",
        "TIM",
        "TIMe",
        "TIM2",
        "TIM2e",
        "TIM3",
        "TIM3e",
        "TVM",
        "TVMe",
        "SYM",
        "GTR",
    ],
    "Description": [
        "Equal substitution rates and equal base frequencies (Jukes and Cantor, 1969).",
        "Equal rates but unequal base freq. (Felsenstein, 1981).",
        "Unequal transition/transversion rates and equal base freq. (Kimura, 1980).",
        "Unequal transition/transversion rates and unequal base freq. (Hasegawa, Kishino and Yano, 1985).",
        "Like HKY but unequal purine/pyrimidine rates (Tamura and Nei, 1993).",
        "Like TN but equal base freq.",
        "Three substitution types model and equal base freq. (Kimura, 1981).",
        "Like K81 but unequal base freq.",
        "AC=AT, AG=CT, CG=GT and equal base freq.",
        "Like TPM2 but unequal base freq.",
        "AC=CG, AG=CT, AT=GT and equal base freq.",
        "Like TPM3 but unequal base freq.",
        "Transition model, AC=GT, AT=CG and unequal base freq.",
        "Like TIM but equal base freq.",
        "AC=AT, CG=GT and unequal base freq.",
        "Like TIM2 but equal base freq.",
        "AC=CG, AT=GT and unequal base freq.",
        "Like TIM3 but equal base freq.",
        "Transversion model, AG=CT and unequal base freq.",
        "Like TVM but equal base freq.",
        "Symmetric model with unequal rates but equal base freq. (Zharkikh, 1994).",
        "General time reversible model with unequal rates and unequal base freq. (Tavare, 1986).",
    ],
}
_aa_models = {
    "Abbreviation": [
        "Blosum62",
        "cpREV",
        "Dayhoff",
        "DCMut",
        "EAL",
        "ELM",
        "FLAVI",
        "FLU",
        "GTR20",
        "HIVb",
        "HIVw",
        "JTT",
        "JTTDCMut",
        "LG",
        "mtART",
        "mtMAM",
        "mtREV",
        "mtZOA",
        "mtMet",
        "mtVer",
        "mtInv",
        "NQ.bird",
        "NQ.insect",
        "NQ.mammal",
        "NQ.pfam",
        "NQ.plant",
        "NQ.yeast",
        "Poisson",
        "PMB",
        "Q.bird",
        "Q.insect",
        "Q.mammal",
        "Q.pfam",
        "Q.plant",
        "Q.yeast",
        "rtREV",
        "VT",
        "WAG",
    ],
    "Description": [
        "BLOcks SUbstitution Matrix (Henikoff and Henikoff, 1992). Note that BLOSUM62 is not recommended for phylogenetic analysis as it was designed mainly for sequence alignments.",
        "chloroplast matrix (Adachi et al., 2000).",
        "General matrix (Dayhoff et al., 1978).",
        "Revised Dayhoff matrix (Kosiol and Goldman, 2005).",
        "General matrix. To be used with profile mixture models (for eg. EAL+C60) for reconstructing relationships between eukaryotes and Archaea (Banos et al., 2024).",
        "General matrix. To be used with profile mixture models (for eg. ELM+C60) for phylogenetic analysis of proteins encoded by nuclear genomes of eukaryotes (Banos et al., 2024).",
        "Flavivirus (Le and Vinh, 2020).",
        "Influenza virus (Dang et al., 2010).",
        "General time reversible models with 190 rate parameters.",
        "HIV between-patient matrix HIV-Bm (Nickle et al., 2007).",
        "HIV within-patient matrix HIV-Wm (Nickle et al., 2007).",
        "General matrix (Jones et al., 1992).",
        "Revised JTT matrix (Kosiol and Goldman, 2005).",
        "General matrix (Le and Gascuel, 2008).",
        "Mitochondrial Arthropoda (Abascal et al., 2007).",
        "Mitochondrial Mammalia (Yang et al., 1998).",
        "Mitochondrial Vertebrate (Adachi and Hasegawa, 1996).",
        "Mitochondrial Metazoa (Animals) (Rota-Stabelli et al., 2009).",
        "Mitochondrial Metazoa (Vinh et al., 2017).",
        "Mitochondrial Vertebrate (Vinh et al., 2017).",
        "Mitochondrial Inverterbrate (Vinh et al., 2017).",
        "Non-reversible Q matrix (Dang et al., 2022) estimated for birds (Jarvis et al., 2015).",
        "Non-reversible Q matrix (Dang et al., 2022) estimated for insects (Misof et al., 2014).",
        "Non-reversible Q matrix (Dang et al., 2022) estimated for mammals (Wu et al., 2018).",
        "General non-reversible Q matrix (Dang et al., 2022) estimated from Pfam version 31 database (El-Gebali et al., 2018).",
        "Non-reversible Q matrix (Dang et al., 2022) estimated for plants (Ran et al., 2018).",
        "Non-reversible Q matrix (Dang et al., 2022) estimated for yeasts (Shen et al., 2018).",
        "Equal amino-acid exchange rates and frequencies.",
        "Probability Matrix from Blocks, revised BLOSUM matrix (Veerassamy et al., 2004).",
        "Q matrix (Minh et al., 2021) estimated for birds (Jarvis et al., 2015).",
        "Q matrix (Minh et al., 2021) estimated for insects (Misof et al., 2014).",
        "Q matrix (Minh et al., 2021) estimated for mammals (Wu et al., 2018).",
        "General Q matrix (Minh et al., 2021) estimated from Pfam version 31 database (El-Gebali et al., 2018).",
        "Q matrix (Minh et al., 2021) estimated for plants (Ran et al., 2018).",
        "Q matrix (Minh et al., 2021) estimated for yeasts (Shen et al., 2018).",
        "Retrovirus (Dimmic et al., 2002).",
        "General 'Variable Time' matrix (Mueller and Vingron, 2000).",
        "General matrix (Whelan and Goldman, 2001).",
    ],
}


@functools.cache
def _make_all_models():
    _all_models = {"Model Type": [], "Abbreviation": [], "Description": []}
    for model_type, models in zip(["nucleotide", "protein"], [_dna_models, _aa_models]):
        mtype = [model_type] * len(models["Abbreviation"])
        _all_models["Model Type"].extend(mtype)
        _all_models["Abbreviation"].extend(models["Abbreviation"])
        _all_models["Description"].extend(models["Description"])
    return _all_models


def available_models(model_type: Optional[str] = None) -> _Table:
    """returns a table of showing available substitution models

    Parameters
    ----------
    model_type
        either "nucleotide", "protein" or None. If None, all models are returned.
    """
    if model_type == "dna":
        table = make_table(data=_dna_models)
    elif model_type == "protein":
        table = make_table(data=_aa_models)
    else:
        table = make_table(data=_make_all_models())

    return table
