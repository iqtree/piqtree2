"""Python wrapper for model finder in the IQ-TREE library."""

from collections.abc import Iterable

import cogent3
import yaml
from _piqtree2 import iq_model_finder

from piqtree2.iqtree._decorator import iqtree_func

iq_model_finder = iqtree_func(iq_model_finder, hide_files=True)


def model_finder(
    aln: cogent3.Alignment | cogent3.ArrayAlignment,
    model_set: Iterable[str] | None = None,
    freq_set: Iterable[str] | None = None,
    rate_set: Iterable[str] | None = None,
    rand_seed: int | None = None,
) -> dict:
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

    return yaml.safe_load(
        iq_model_finder(
            names,
            seqs,
            rand_seed,
            ",".join(model_set),
            ",".join(freq_set),
            ",".join(rate_set),
        ),
    )
