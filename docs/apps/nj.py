# %% [markdown]
# The Neighbour-Joining method uses genetic distances to build a phylogenetic tree. `piqtree2` provides only `piqtree_jc_dists` for this. `cogent3` includes many more methods. The  results of either can be used to build a tree. For divergent sequences we will use Lake's paralinear measure as it accomodates divergent sequence compositions.

# %%
import cogent3

from piqtree2 import download_dataset

aln_path = download_dataset("example.phy.gz", dest_dir="data")
aln = cogent3.load_aligned_seqs(aln_path, moltype="dna", format="phylip")

# %% [markdown]
# ## Getting a paralinear distance matrix
# This can be obtained directly from the alignment object itself.

# %%
dists = aln.distance_matrix(calc="paralinear")
dists

# %% [markdown]
# Get help on the `piqtree_nj` app.

# %%
cogent3.app_help("piqtree_nj")

# %% [markdown]
# Make an app and apply it to the distance matrix.

# %%
nj = cogent3.get_app("piqtree_nj")
tree = nj(dists)

# %% [markdown]
# > **Warning**
# > Branch lengths can be negative in the piqtree2 NJ tree. This manifests as branches going backwards!

# %%
tree.get_figure().show()

# %% [markdown]
# > **Note**
# > To write the tree to a file, use the `write()` method.

# %% [markdown]
# ## Combining the piqtree dist and nj apps
# We can combine the `piqtree_jc_dists` and `piqtree_nj` apps to build a tree from an alignment in one step.

# %%
jc = cogent3.get_app("piqtree_jc_dists")
nj = cogent3.get_app("piqtree_nj")
app = jc + nj
tree = app(aln)
tree.get_figure().show()
