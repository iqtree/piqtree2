"""Convenience functions for showing user facing options and their descriptions."""

import functools
from typing import Optional

from cogent3 import _Table, make_table

from piqtree2.model._substitution_model import (
    ALL_MODELS_CLASSES,
    AaModel,
    DnaModel,
    SubstitutionModel,
)


@functools.cache
def _make_models(model_type: type[SubstitutionModel]) -> dict[str, list[str]]:
    data = {"Model Type": [], "Abbreviation": [], "Description": []}

    model_classes = (
        ALL_MODELS_CLASSES if model_type == SubstitutionModel else [model_type]
    )

    for model_class in model_classes:
        for model in model_class:
            data["Model Type"].append(model.model_type())
            data["Abbreviation"].append(model.name)
            data["Description"].append(model.description)

    return data


def available_models(model_type: Optional[str] = None) -> _Table:
    """Return a table showing available substitution models.

    Parameters
    ----------
    model_type
        either "nucleotide", "protein" or None. If None, all models are returned.

    """
    if model_type == "dna":
        table = make_table(data=_make_models(DnaModel))
    elif model_type == "protein":
        table = make_table(data=_make_models(AaModel))
    else:
        table = make_table(data=_make_models(SubstitutionModel))

    return table
