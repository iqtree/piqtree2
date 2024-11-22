## Welcome

`piqtree2` is a Python package that exposes selected [IQ-TREE2](http://www.iqtree.org) capabilities within Python, using the [cogent3](https://cogent3.org) library as the interface.

`piqtree2` is implemented with the goals of:

- make the individual high-performance components of IQ-TREE2 available within Python, enabling the community to take advantage of these routines.
- facilitate exploratory analyses by leveraging cogent3's capabilities to provide a rich user experience in interactive Jupyter notebooks, e.g. trivial parallelisation across collections of alignments
- code using piqtree2 apps should be easy to understand

`piqtree2` provides mini-applications in the form of [cogent3 apps](https://cogent3.org/doc/app/index.html). These can interplay with other such apps, e.g. the [cogent3-ete3](https://pypi.org/project/cogent3-ete3/) tree conversion plugin, the [diverse-seqs](https://pypi.org/project/diverse-seq/) sequence subsampling plugin.

> **Note**
> `piqtree2` does not implement all of the capabilities of IQ-Tree2!

## Installation

You get the vanilla version of `piqtree2` by running the following command.

```
pip install piqtree2
```

To get visualisation support with plotly, use the `[extra]` option.

```
pip install "piqtree2[extra]"
```

## Supported platforms

<<<<<<< HEAD
At present we do not provide native binaries for Windows. Windows users can run `piqtree2` using the Windows Susbsystem for Linux (WSL) which can installed via the Windows Store.
=======
At present we do not provide native binaries for Windows. Windows users can run `piqtree2` using the Windows Subsystem for Linux (WSL) which can installed via the Windows Store.
>>>>>>> 2a36772745f90c958f407e251e623de22a523ea2
