"""Apps must be pickleable to be able to be run with parallel=True"""

import pickle

from cogent3 import get_app

from piqtree2._app import _ALL_APP_NAMES


def test_pickle() -> None:
    for app_name in _ALL_APP_NAMES:
        app = (
            get_app(app_name)
            if app_name != "piqtree_phylo"
            else get_app(app_name, "JC")
        )
        assert len(pickle.dumps(app)) > 0
