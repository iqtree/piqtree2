# Calculate pairwise Robinson-Foulds distances between trees

A pairwise Robinson-Foulds distance matrix can be constructed from a sequence of cogent3 tree objects using [`robinson_foulds`](../api/tree_distance/robinson_foulds.md).

## Usage

### Basic Usage

Construct a collection of cogent3 tree objects, then use [`robinson_foulds`](../api/tree_distance/robinson_foulds.md) to find the pairwise distances.

```python
from cogent3 import make_tree
from piqtree2 import robinson_foulds

tree1 = make_tree("(a,b,(c,(d,e)));")
tree2 = make_tree("(e,b,(c,(d,a)));")
tree3 = make_tree("(a,b,(d,(c,e)));")

rf_distances = robinson_foulds([tree1, tree2, tree3])
```

## See also

- For constructing a maximum likelihood tree, see ["Construct a maximum likelihood phylogenetic tree"](construct_ml_tree.md).
- For making a collection of random trees, see ["Make a collection of randomly generated trees"](make_random_trees.md).