"""Python wrapper for model finder in the IQ-TREE library."""

import dataclasses
import re
from collections.abc import Iterable
from typing import Any

import yaml
from _piqtree2 import iq_model_finder
from cogent3.app import typing as c3_types

from piqtree2 import model
from piqtree2.iqtree._decorator import iqtree_func

iq_model_finder = iqtree_func(iq_model_finder, hide_files=True)

_rate_het = re.compile(r"[GR]\d*")
_freq = re.compile("F[^+]")


def get_model(raw_data: dict[str, Any], key: str) -> model.Model:
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


@dataclasses.dataclass(slots=True)
class ModelFinderResult:
    raw_data: dataclasses.InitVar[dict[str, Any]]
    best_aic: model.Model = dataclasses.field(init=False)
    best_aicc: model.Model = dataclasses.field(init=False)
    best_bic: model.Model = dataclasses.field(init=False)
    model_stats: dict[model.Model, str] = dataclasses.field(init=False, repr=False)

    def __post_init__(self, raw_data):
        model_stats = {}
        for key, val in raw_data.items():
            try:
                new_model = get_model(raw_data, key)
            except (ValueError, AttributeError):
                continue
            model_stats[new_model] = val
        self.model_stats = model_stats
        self.best_aic = get_model(raw_data, "best_model_AIC")
        self.best_aicc = get_model(raw_data, "best_model_AICc")
        self.best_bic = get_model(raw_data, "best_model_BIC")
        model_stats[self.best_aic] = raw_data[str(self.best_aic)]
        model_stats[self.best_aicc] = raw_data[str(self.best_aicc)]
        model_stats[self.best_bic] = raw_data[str(self.best_bic)]


def model_finder(
    aln: c3_types.AlignedSeqsType,
    model_set: Iterable[str] | None = None,
    freq_set: Iterable[str] | None = None,
    rate_set: Iterable[str] | None = None,
    rand_seed: int | None = None,
) -> ModelFinderResult:
    # TODO(rob): discuss return type further
    # 68
    if rand_seed is None:
        rand_seed = 0  # The default rand_seed in IQ-TREE

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
        ),
    )
    return ModelFinderResult(raw_data=raw)
