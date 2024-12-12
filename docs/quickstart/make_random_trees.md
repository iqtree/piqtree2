# Make a collection of randomly generated trees

A sequence of random trees can be generated using [`random_trees`](../api/tree/random_trees.md#piqtree2.random_trees).
Multiple tree generation modes are supported with the [`TreeGenMode`](../api/tree/random_trees.md#piqtree2.TreeGenMode) including
balanced, birth-death, caterpillar, star, uniform, and Yule-Harding trees.

## Usage

### Basic Usage

Specify the number of trees to generate, the number of taxa, and under what mechanism the trees are to be generated.
See the documentation for [`TreeGenMode`](../api/tree/random_trees.md#piqtree2.TreeGenMode) for all available generation options.

> **Note:** if star trees are generated the tree appears bifurcating, but branch lengths are set to zero where appropriate.

```python
from piqtree2 import TreeGenMode, random_trees

num_trees = 5
num_taxa = 100

trees = random_trees(num_trees, num_taxa, TreeGenMode.YULE_HARDING)
```

### Reproducible Results

For reproducible results, a random seed may be specified.
> **Caution:** 0 and None are equivalent to no random seed being specified.

```python
from piqtree2 import TreeGenMode, random_trees

num_trees = 5
num_taxa = 100

trees = random_trees(num_trees, num_taxa, TreeGenMode.UNIFORM, rand_seed=1)
```

## See also

- For constructing a maximum likelihood tree, see ["Construct a maximum likelihood phylogenetic tree"](construct_ml_tree.md).
