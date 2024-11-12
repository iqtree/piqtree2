import os
import pathlib

os.environ["COGENT3_ALIGNMENT_REPR_POLICY"] = "num_pos=30"

_data_files = {
    "mammal-orths.zip": "https://github.com/user-attachments/files/17403119/mammal-orths.zip",
    "brca1.fasta.gz": "https://github.com/user-attachments/files/17404687/brca1.fasta.gz",
    "example.phy.gz": "https://github.com/user-attachments/files/17551543/example.phy.gz"
}


def download_data(url: str, dest_dir: str, dest_name: str) -> pathlib.Path:
    import requests
    from rich.progress import Progress

    outpath = pathlib.Path(dest_dir) / dest_name
    outpath.parent.mkdir(parents=True, exist_ok=True)
    if outpath.exists():
        return outpath

    response = requests.get(url, stream=True, timeout=20)
    # Sizes in bytes.
    total_size = int(response.headers.get("content-length", 0))
    block_size = 4096
    with Progress() as progress:
        task = progress.add_task("Downloading", total=total_size)
        with outpath.open("wb") as out:
            for data in response.iter_content(block_size):
                progress.update(task, advance=len(data))
                out.write(data)
        progress.update(task, completed=total_size, refresh=True)
    return outpath


def data_path(name: str) -> pathlib.Path:
    if name not in _data_files:
        raise ValueError(f"Unknown data file: {name}")

    return download_data(_data_files[name], "data", name)
