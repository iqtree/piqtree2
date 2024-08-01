from enum import Enum, auto
from typing import ClassVar

from typing_extensions import Self


class Model(Enum):
    _descriptions: ClassVar[dict[Self, str]] = {}

    @property
    def description(self) -> str:
        return self._descriptions[self]


class DnaModel(Model):
    JC = auto()
    F81 = auto()
    K80 = auto()
    HKY = auto()
    TN = auto()
    TNe = auto()
    K81 = auto()
    K81u = auto()
    TPM2 = auto()
    TPM2u = auto()
    TPM3 = auto()
    TPM3u = auto()
    TIM = auto()
    TIMe = auto()
    TIM2 = auto()
    TIM2e = auto()
    TIM3 = auto()
    TIM3e = auto()
    TVM = auto()
    TVMe = auto()
    SYM = auto()
    GTR = auto()

    _descriptions: ClassVar[dict[Self, str]] = {
        JC: "Equal substitution rates and equal base frequencies (Jukes and Cantor, 1969).",
        F81: "Equal rates but unequal base freq. (Felsenstein, 1981).",
        K80: "Unequal transition/transversion rates and equal base freq. (Kimura, 1980).",
        HKY: "Unequal transition/transversion rates and unequal base freq. (Hasegawa, Kishino and Yano, 1985).",
        TN: "Like HKY but unequal purine/pyrimidine rates (Tamura and Nei, 1993).",
        TNe: "Like TN but equal base freq.",
        K81: "Three substitution types model and equal base freq. (Kimura, 1981).",
        K81u: "Like K81 but unequal base freq.",
        TPM2: "AC=AT, AG=CT, CG=GT and equal base freq.",
        TPM2u: "Like TPM2 but unequal base freq.",
        TPM3: "AC=CG, AG=CT, AT=GT and equal base freq.",
        TPM3u: "Like TPM3 but unequal base freq.",
        TIM: "Transition model, AC=GT, AT=CG and unequal base freq.",
        TIMe: "Like TIM but equal base freq.",
        TIM2: "AC=AT, CG=GT and unequal base freq.",
        TIM2e: "Like TIM2 but equal base freq.",
        TIM3: "AC=CG, AT=GT and unequal base freq.",
        TIM3e: "Like TIM3 but equal base freq.",
        TVM: "Transversion model, AG=CT and unequal base freq.",
        TVMe: "Like TVM but equal base freq.",
        SYM: "Symmetric model with unequal rates but equal base freq. (Zharkikh, 1994).",
        GTR: "General time reversible model with unequal rates and unequal base freq. (Tavare, 1986).",
    }


class AaModel(Model):
    Blosum62 = auto()
    cpREV = auto()
    Dayhoff = auto()
    DCMut = auto()
    EAL = auto()
    ELM = auto()
    FLAVI = auto()
    FLU = auto()
    GTR20 = auto()
    HIVb = auto()
    HIVw = auto()
    JTT = auto()
    JTTDCMut = auto()
    LG = auto()
    mtART = auto()
    mtMAM = auto()
    mtREV = auto()
    mtZOA = auto()
    mtMet = auto()
    mtVer = auto()
    mtInv = auto()
    NQ_bird = auto()
    NQ_insect = auto()
    NQ_mammal = auto()
    NQ_pfam = auto()
    NQ_plant = auto()
    NQ_yeast = auto()
    Poisson = auto()
    PMB = auto()
    Q_bird = auto()
    Q_insect = auto()
    Q_mammal = auto()
    Q_pfam = auto()
    Q_plant = auto()
    Q_yeast = auto()
    rtREV = auto()
    VT = auto()
    WAG = auto()

    _descriptions: ClassVar[dict[Self, str]] = {
        Blosum62: "BLOcks SUbstitution Matrix (Henikoff and Henikoff, 1992). Note that BLOSUM62 is not recommended for phylogenetic analysis as it was designed mainly for sequence alignments.",
        cpREV: "chloroplast matrix (Adachi et al., 2000).",
        Dayhoff: "General matrix (Dayhoff et al., 1978).",
        DCMut: "Revised Dayhoff matrix (Kosiol and Goldman, 2005).",
        EAL: "General matrix. To be used with profile mixture models (for eg. EAL+C60) for reconstructing relationships between eukaryotes and Archaea (Banos et al., 2024).",
        ELM: "General matrix. To be used with profile mixture models (for eg. ELM+C60) for phylogenetic analysis of proteins encoded by nuclear genomes of eukaryotes (Banos et al., 2024).",
        FLAVI: "Flavivirus (Le and Vinh, 2020).",
        FLU: "Influenza virus (Dang et al., 2010).",
        GTR20: "General time reversible models with 190 rate parameters.",
        HIVb: "HIV between-patient matrix HIV-Bm (Nickle et al., 2007).",
        HIVw: "HIV within-patient matrix HIV-Wm (Nickle et al., 2007).",
        JTT: "General matrix (Jones et al., 1992).",
        JTTDCMut: "Revised JTT matrix (Kosiol and Goldman, 2005).",
        LG: "General matrix (Le and Gascuel, 2008).",
        mtART: "Mitochondrial Arthropoda (Abascal et al., 2007).",
        mtMAM: "Mitochondrial Mammalia (Yang et al., 1998).",
        mtREV: "Mitochondrial Vertebrate (Adachi and Hasegawa, 1996).",
        mtZOA: "Mitochondrial Metazoa (Animals) (Rota-Stabelli et al., 2009).",
        mtMet: "Mitochondrial Metazoa (Vinh et al., 2017).",
        mtVer: "Mitochondrial Vertebrate (Vinh et al., 2017).",
        mtInv: "Mitochondrial Inverterbrate (Vinh et al., 2017).",
        NQ_bird: "Non-reversible Q matrix (Dang et al., 2022) estimated for birds (Jarvis et al., 2015).",
        NQ_insect: "Non-reversible Q matrix (Dang et al., 2022) estimated for insects (Misof et al., 2014).",
        NQ_mammal: "Non-reversible Q matrix (Dang et al., 2022) estimated for mammals (Wu et al., 2018).",
        NQ_pfam: "General non-reversible Q matrix (Dang et al., 2022) estimated from Pfam version 31 database (El-Gebali et al., 2018).",
        NQ_plant: "Non-reversible Q matrix (Dang et al., 2022) estimated for plants (Ran et al., 2018).",
        NQ_yeast: "Non-reversible Q matrix (Dang et al., 2022) estimated for yeasts (Shen et al., 2018).",
        Poisson: "Equal amino-acid exchange rates and frequencies.",
        PMB: "Probability Matrix from Blocks, revised BLOSUM matrix (Veerassamy et al., 2004).",
        Q_bird: "Q matrix (Minh et al., 2021) estimated for birds (Jarvis et al., 2015).",
        Q_insect: "Q matrix (Minh et al., 2021) estimated for insects (Misof et al., 2014).",
        Q_mammal: "Q matrix (Minh et al., 2021) estimated for mammals (Wu et al., 2018).",
        Q_pfam: "General Q matrix (Minh et al., 2021) estimated from Pfam version 31 database (El-Gebali et al., 2018).",
        Q_plant: "Q matrix (Minh et al., 2021) estimated for plants (Ran et al., 2018).",
        Q_yeast: "Q matrix (Minh et al., 2021) estimated for yeasts (Shen et al., 2018).",
        rtREV: "Retrovirus (Dimmic et al., 2002).",
        VT: "General 'Variable Time' matrix (Mueller and Vingron, 2000).",
        WAG: "General matrix (Whelan and Goldman, 2001).",
    }
