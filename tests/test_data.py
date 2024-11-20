import pathlib

import piqtree2


def test_dataset_names() -> None:
    names = piqtree2.dataset_names()
    assert len(names) > 0


def test_download_dataset(tmp_path: pathlib.Path) -> None:
    path = piqtree2.download_dataset("example.tree.gz", dest_dir=tmp_path)
    assert pathlib.Path(path).exists()
