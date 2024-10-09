from typing import Union

import cogent3
import numpy as np
from _piqtree2 import iq_jc_distances

from piqtree2.iqtree._decorator import iqtree_func

iq_jc_distances = iqtree_func(iq_jc_distances, hide_files=True)


def jc_distances(
    aln: Union[cogent3.Alignment, cogent3.ArrayAlignment],
) -> np.ndarray:
    names = aln.names
    seqs = [str(seq) for seq in aln.iter_seqs(names)]

    result = iq_jc_distances(names, seqs).strip()
    data = result.split("\n")[1:]

    distances = np.zeros((len(names), len(names)))

    for i, row in enumerate(data):
        distance_part = row.strip().split()[-len(names) :]
        distances[i] = tuple(map(float, distance_part))

    return distances
