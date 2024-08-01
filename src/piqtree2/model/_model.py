import functools
from abc import abstractmethod
from enum import Enum, auto

from typing_extensions import Self


class Model(Enum):
    @staticmethod
    @abstractmethod
    def model_type() -> str: ...

    @staticmethod
    @abstractmethod
    def _descriptions() -> dict[Self, str]: ...

    @property
    def description(self) -> str:
        return self._descriptions()[self]


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

    @staticmethod
    def model_type() -> str:
        return "nucleotide"

    @staticmethod
    @functools.cache
    def _descriptions() -> dict[Self, str]:
        return {
            DnaModel.JC: "Equal substitution rates and equal base frequencies (Jukes and Cantor, 1969).",
            DnaModel.F81: "Equal rates but unequal base freq. (Felsenstein, 1981).",
            DnaModel.K80: "Unequal transition/transversion rates and equal base freq. (Kimura, 1980).",
            DnaModel.HKY: "Unequal transition/transversion rates and unequal base freq. (Hasegawa, Kishino and Yano, 1985).",
            DnaModel.TN: "Like HKY but unequal purine/pyrimidine rates (Tamura and Nei, 1993).",
            DnaModel.TNe: "Like TN but equal base freq.",
            DnaModel.K81: "Three substitution types model and equal base freq. (Kimura, 1981).",
            DnaModel.K81u: "Like K81 but unequal base freq.",
            DnaModel.TPM2: "AC=AT, AG=CT, CG=GT and equal base freq.",
            DnaModel.TPM2u: "Like TPM2 but unequal base freq.",
            DnaModel.TPM3: "AC=CG, AG=CT, AT=GT and equal base freq.",
            DnaModel.TPM3u: "Like TPM3 but unequal base freq.",
            DnaModel.TIM: "Transition model, AC=GT, AT=CG and unequal base freq.",
            DnaModel.TIMe: "Like TIM but equal base freq.",
            DnaModel.TIM2: "AC=AT, CG=GT and unequal base freq.",
            DnaModel.TIM2e: "Like TIM2 but equal base freq.",
            DnaModel.TIM3: "AC=CG, AT=GT and unequal base freq.",
            DnaModel.TIM3e: "Like TIM3 but equal base freq.",
            DnaModel.TVM: "Transversion model, AG=CT and unequal base freq.",
            DnaModel.TVMe: "Like TVM but equal base freq.",
            DnaModel.SYM: "Symmetric model with unequal rates but equal base freq. (Zharkikh, 1994).",
            DnaModel.GTR: "General time reversible model with unequal rates and unequal base freq. (Tavare, 1986).",
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

    @staticmethod
    def model_type() -> str:
        return "protein"

    @staticmethod
    @functools.cache
    def _descriptions() -> dict[Self, str]:
        return {
            AaModel.Blosum62: "BLOcks SUbstitution Matrix (Henikoff and Henikoff, 1992). Note that BLOSUM62 is not recommended for phylogenetic analysis as it was designed mainly for sequence alignments.",
            AaModel.cpREV: "chloroplast matrix (Adachi et al., 2000).",
            AaModel.Dayhoff: "General matrix (Dayhoff et al., 1978).",
            AaModel.DCMut: "Revised Dayhoff matrix (Kosiol and Goldman, 2005).",
            AaModel.EAL: "General matrix. To be used with profile mixture models (for eg. EAL+C60) for reconstructing relationships between eukaryotes and Archaea (Banos et al., 2024).",
            AaModel.ELM: "General matrix. To be used with profile mixture models (for eg. ELM+C60) for phylogenetic analysis of proteins encoded by nuclear genomes of eukaryotes (Banos et al., 2024).",
            AaModel.FLAVI: "Flavivirus (Le and Vinh, 2020).",
            AaModel.FLU: "Influenza virus (Dang et al., 2010).",
            AaModel.GTR20: "General time reversible models with 190 rate parameters.",
            AaModel.HIVb: "HIV between-patient matrix HIV-Bm (Nickle et al., 2007).",
            AaModel.HIVw: "HIV within-patient matrix HIV-Wm (Nickle et al., 2007).",
            AaModel.JTT: "General matrix (Jones et al., 1992).",
            AaModel.JTTDCMut: "Revised JTT matrix (Kosiol and Goldman, 2005).",
            AaModel.LG: "General matrix (Le and Gascuel, 2008).",
            AaModel.mtART: "Mitochondrial Arthropoda (Abascal et al., 2007).",
            AaModel.mtMAM: "Mitochondrial Mammalia (Yang et al., 1998).",
            AaModel.mtREV: "Mitochondrial Vertebrate (Adachi and Hasegawa, 1996).",
            AaModel.mtZOA: "Mitochondrial Metazoa (Animals) (Rota-Stabelli et al., 2009).",
            AaModel.mtMet: "Mitochondrial Metazoa (Vinh et al., 2017).",
            AaModel.mtVer: "Mitochondrial Vertebrate (Vinh et al., 2017).",
            AaModel.mtInv: "Mitochondrial Inverterbrate (Vinh et al., 2017).",
            AaModel.NQ_bird: "Non-reversible Q matrix (Dang et al., 2022) estimated for birds (Jarvis et al., 2015).",
            AaModel.NQ_insect: "Non-reversible Q matrix (Dang et al., 2022) estimated for insects (Misof et al., 2014).",
            AaModel.NQ_mammal: "Non-reversible Q matrix (Dang et al., 2022) estimated for mammals (Wu et al., 2018).",
            AaModel.NQ_pfam: "General non-reversible Q matrix (Dang et al., 2022) estimated from Pfam version 31 database (El-Gebali et al., 2018).",
            AaModel.NQ_plant: "Non-reversible Q matrix (Dang et al., 2022) estimated for plants (Ran et al., 2018).",
            AaModel.NQ_yeast: "Non-reversible Q matrix (Dang et al., 2022) estimated for yeasts (Shen et al., 2018).",
            AaModel.Poisson: "Equal amino-acid exchange rates and frequencies.",
            AaModel.PMB: "Probability Matrix from Blocks, revised BLOSUM matrix (Veerassamy et al., 2004).",
            AaModel.Q_bird: "Q matrix (Minh et al., 2021) estimated for birds (Jarvis et al., 2015).",
            AaModel.Q_insect: "Q matrix (Minh et al., 2021) estimated for insects (Misof et al., 2014).",
            AaModel.Q_mammal: "Q matrix (Minh et al., 2021) estimated for mammals (Wu et al., 2018).",
            AaModel.Q_pfam: "General Q matrix (Minh et al., 2021) estimated from Pfam version 31 database (El-Gebali et al., 2018).",
            AaModel.Q_plant: "Q matrix (Minh et al., 2021) estimated for plants (Ran et al., 2018).",
            AaModel.Q_yeast: "Q matrix (Minh et al., 2021) estimated for yeasts (Shen et al., 2018).",
            AaModel.rtREV: "Retrovirus (Dimmic et al., 2002).",
            AaModel.VT: "General 'Variable Time' matrix (Mueller and Vingron, 2000).",
            AaModel.WAG: "General matrix (Whelan and Goldman, 2001).",
        }


ALL_MODELS_CLASSES: list[type[Model]] = [DnaModel, AaModel]
