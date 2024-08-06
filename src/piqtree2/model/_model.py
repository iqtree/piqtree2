import functools
from abc import abstractmethod
from enum import Enum, unique

from typing_extensions import Self


class SubstitutionModel(Enum):
    """Base class for models."""

    @staticmethod
    @abstractmethod
    def model_type() -> str:
        """Get the type of the model.

        Returns
        -------
        str
            The type of the model.

        """

    @staticmethod
    @abstractmethod
    def _descriptions() -> dict[Self, str]:
        """Get the description of each model.

        Returns
        -------
        dict[Self, str]
            A mapping of models to their description.

        """

    @property
    def description(self) -> str:
        """The model's description.

        Returns
        -------
        str
            The model's description.

        """
        return self._descriptions()[self]


@unique
class DnaModel(SubstitutionModel):
    """DNA substitution models."""

    JC = "JC"
    F81 = "F81"
    K80 = "K80"
    HKY = "HKY"
    TN = "TN"
    TNe = "TNe"
    K81 = "K81"
    K81u = "K81u"
    TPM2 = "TPM2"
    TPM2u = "TPM2u"
    TPM3 = "TPM3"
    TPM3u = "TPM3u"
    TIM = "TIM"
    TIMe = "TIMe"
    TIM2 = "TIM2"
    TIM2e = "TIM2e"
    TIM3 = "TIM3"
    TIM3e = "TIM3e"
    TVM = "TVM"
    TVMe = "TVMe"
    SYM = "SYM"
    GTR = "GTR"

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


@unique
class AaModel(SubstitutionModel):
    """Protein substitution models."""

    Blosum62 = "Blosum62"
    cpREV = "cpREV"
    Dayhoff = "Dayhoff"
    DCMut = "DCMut"
    EAL = "EAL"
    ELM = "ELM"
    FLAVI = "FLAVI"
    FLU = "FLU"
    GTR20 = "GTR20"
    HIVb = "HIVb"
    HIVw = "HIVw"
    JTT = "JTT"
    JTTDCMut = "JTTDCMut"
    LG = "LG"
    mtART = "mtART"
    mtMAM = "mtMAM"
    mtREV = "mtREV"
    mtZOA = "mtZOA"
    mtMet = "mtMet"
    mtVer = "mtVer"
    mtInv = "mtInv"
    NQ_bird = "NQ.bird"
    NQ_insect = "NQ.insect"
    NQ_mammal = "NQ.mammal"
    NQ_pfam = "NQ.pfam"
    NQ_plant = "NQ.plant"
    NQ_yeast = "NQ.yeast"
    Poisson = "Poisson"
    PMB = "PMB"
    Q_bird = "Q.bird"
    Q_insect = "Q.insect"
    Q_mammal = "Q.mammal"
    Q_pfam = "Q.pfam"
    Q_plant = "Q.plant"
    Q_yeast = "Q.yeast"
    rtREV = "rtREV"
    VT = "VT"
    WAG = "WAG"

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


ALL_MODELS_CLASSES: list[type[SubstitutionModel]] = [DnaModel, AaModel]
