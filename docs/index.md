# piqtree2 documentation

## Overview

`piqtree2` is a Python package that exposes selected [IQ-TREE 2](http://www.iqtree.org) capabilities within Python, using the [cogent3](https://cogent3.org) library as the interface.

`piqtree2` is implemented with the goals of:

- making the individual high-performance components of IQ-TREE 2 available within Python, enabling the community to take advantage of these routines.
- facilitating exploratory analyses by leveraging cogent3's capabilities to provide a rich user experience in interactive Jupyter notebooks, e.g. trivial parallelisation across collections of alignments.
- code using piqtree2 apps should be easy to understand.

In addition to the functions provided, `piqtree2` provides mini-applications in the form of [cogent3 apps](https://cogent3.org/doc/app/index.html). These can interplay with other such apps, e.g. the [cogent3-ete3](https://pypi.org/project/cogent3-ete3/) tree conversion plugin, the [diverse-seqs](https://pypi.org/project/diverse-seq/) sequence subsampling plugin.

> **Note**
> `piqtree2` does not implement all of the capabilities of IQ-TREE 2!

## Installation

You get the vanilla version of `piqtree2` by running the following command.

```bash
pip install piqtree2
```

To get visualisation support with plotly, use the `[extra]` option.

```bash
pip install "piqtree2[extra]"
```

## Supported platforms

At present we do not provide native binaries for Windows. Windows users can run `piqtree2` using the Windows Subsystem for Linux (WSL) which can installed via the Windows Store.
