import pathlib

import piqtree


def test_dataset_names() -> None:
    names = piqtree.dataset_names()
    assert len(names) > 0


def test_download_dataset(tmp_path: pathlib.Path) -> None:
    path = piqtree.download_dataset("example.tree.gz", dest_dir=tmp_path)
    assert pathlib.Path(path).exists()
