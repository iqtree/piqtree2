import pathlib

import pytest


@pytest.fixture(scope="session")
def DATA_DIR():
    return pathlib.Path(__file__).parent / "data"


@pytest.fixture()
def tmp_dir(tmp_path_factory):
    return tmp_path_factory.mktemp("cli")
