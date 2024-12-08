"""Python wrapper for model finder in the IQ-TREE library."""

import dataclasses
import re
from collections.abc import Iterable
from typing import Any

import yaml
from _piqtree2 import iq_model_finder
from cogent3.app import typing as c3_types
from cogent3.util.misc import get_object_provenance

from piqtree2 import model
from piqtree2.iqtree._decorator import iqtree_func

iq_model_finder = iqtree_func(iq_model_finder, hide_files=True)

_rate_het = re.compile(r"[GR]\d*")
_freq = re.compile("F[^+]")


def _get_model(raw_data: dict[str, Any], key: str) -> model.Model:
    model_class, components = raw_data[key].split("+", maxsplit=1)
    model_class = model.get_substitution_model(model_class)
    invariant_sites = "I" in components
    if rate_model := _rate_het.search(components):
        rates_het = rate_model.group()
    else:
        rates_het = None

    freq_type_match = _freq.search(components)
    freq_type = freq_type_match.group() if freq_type_match else "F"

    return model.Model(
        submod_type=model_class,
        rate_model=rates_het,
        freq_type=freq_type,
        invariant_sites=invariant_sites,
    )


@dataclasses.dataclass(slots=True, frozen=True)
class ModelResultValue:
    """Model statistics from IQ-TREE model_finder.

    Parameters
    ----------
    lnL
        Log likelihood of the model.
    nfp
        Number of free parameters in the model.
    tree_length
        Length of the tree (sum of branch lengths).
    """

    lnL: float # noqa: N815
    nfp: int
    tree_length: float

    @classmethod
    def from_string(cls, val: str) -> "ModelResultValue":
        """Parse the string produced by IQ-TREE model_finder for a given model."""
        try:
            lnL, nfp, tree_length = val.split() # noqa: N806
            return cls(lnL=float(lnL), nfp=int(nfp), tree_length=float(tree_length))
        except ValueError as e:
            msg = f"Error parsing string '{val}'"
            raise ValueError(msg) from e


@dataclasses.dataclass(slots=True)
class ModelFinderResult:
    source: str
    raw_data: dataclasses.InitVar[dict[str, Any]]
    best_aic: model.Model = dataclasses.field(init=False)
    best_aicc: model.Model = dataclasses.field(init=False)
    best_bic: model.Model = dataclasses.field(init=False)
    model_stats: dict[model.Model | str, ModelResultValue] = dataclasses.field(
        init=False, repr=False, default_factory=dict,
    )

    def __post_init__(self, raw_data: dict[str, Any]) -> None:
        self.model_stats = {
            key: ModelResultValue.from_string(val)
            for key, val in raw_data.items()
            if not key.startswith(("best_", "initTree")) and isinstance(val, str)
        }
        self.best_aic = _get_model(raw_data, "best_model_AIC")
        self.best_aicc = _get_model(raw_data, "best_model_AICc")
        self.best_bic = _get_model(raw_data, "best_model_BIC")

        self.model_stats[self.best_aic] = ModelResultValue.from_string(
            raw_data[str(self.best_aic)],
        )
        self.model_stats[self.best_aicc] = ModelResultValue.from_string(
            raw_data[str(self.best_aicc)],
        )
        self.model_stats[self.best_bic] = ModelResultValue.from_string(
            raw_data[str(self.best_bic)],
        )

    def to_rich_dict(self) -> dict[str, Any]:
        import piqtree2

        result = {"version": piqtree2.__version__, "type": get_object_provenance(self)}

        raw_data = {
            str(model_): f"{stats.lnL} {stats.nfp} {stats.tree_length}"
            for model_, stats in self.model_stats.items()
        }
        for attr in ("best_model_AIC", "best_model_AICc", "best_model_BIC"):
            raw_data[attr] = str(getattr(self, attr.replace("_model", "").lower()))
        result["init_kwargs"] = {"raw_data": raw_data, "source": self.source}
        return result

    @classmethod
    def from_rich_dict(cls, data: dict[str, Any]) -> "ModelFinderResult":
        return cls(**data["init_kwargs"])


def model_finder(
    aln: c3_types.AlignedSeqsType,
    model_set: Iterable[str] | None = None,
    freq_set: Iterable[str] | None = None,
    rate_set: Iterable[str] | None = None,
    rand_seed: int | None = None,
    num_threads: int | None = None,
) -> ModelFinderResult | c3_types.SerialisableType:
    source = aln.info.source
    if rand_seed is None:
        rand_seed = 0  # The default rand_seed in IQ-TREE

    if num_threads is None:
        num_threads = 1

    if model_set is None:
        model_set = set()
    if freq_set is None:
        freq_set = set()
    if rate_set is None:
        rate_set = set()

    names = aln.names
    seqs = [str(seq) for seq in aln.iter_seqs(names)]

    raw = yaml.safe_load(
        iq_model_finder(
            names,
            seqs,
            rand_seed,
            ",".join(model_set),
            ",".join(freq_set),
            ",".join(rate_set),
            num_threads,
        ),
    )
    return ModelFinderResult(raw_data=raw, source=source)
