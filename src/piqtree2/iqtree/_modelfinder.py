"""Python wrapper for model finder in the IQ-TREE library."""

from typing import Optional, Union

import cogent3
import yaml
from _piqtree2 import iq_model_finder

from piqtree2.iqtree._decorator import iqtree_func

iq_model_finder = iqtree_func(iq_model_finder, hide_files=True)


def model_finder(
    aln: Union[cogent3.Alignment, cogent3.ArrayAlignment],
    rand_seed: Optional[int] = None,
) -> None:  # TODO: decide type
    if rand_seed is None:
        rand_seed = 0  # The default rand_seed in IQ-TREE

    names = aln.names
    seqs = [str(seq) for seq in aln.iter_seqs(names)]

    print(type(names), type(seqs))
    yaml_result = yaml.safe_load(iq_model_finder(names, seqs, rand_seed, "", "", ""))
    print(yaml_result)
    return yaml_result
