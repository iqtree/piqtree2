# %% [markdown]
# ## Building phylogenies using `piqtree_phylo`
# For this simple case, we will build a single phylogeny using the GTR model on one alignment.
# We have a utility script for this documentation that provides the local path to that data. We will then load that data and, as it contains quite a few sequences, we will use a subset of it. We use methods on the cogent3 object to do that.

# %%
import cogent3

import doc_rsrc

aln_path = doc_rsrc.data_path("example.phy.gz")
aln = cogent3.load_aligned_seqs(aln_path, moltype="dna", format="phylip")
aln

# %% [markdown]
# We use a tree corresponding to the data in the `example.phy` file.

# %%
tree = cogent3.make_tree("(LngfishAu,(LngfishSA,LngfishAf),(Frog,((Turtle,((Sphenodon,Lizard),(Crocodile,Bird))),(((Human,(Seal,(Cow,Whale))),(Mouse,Rat)),(Platypus,Opossum)))));")

# %% [markdown]
# We now take a look at the help for the `piqtree_fit` app.

# %%

from cogent3 import app_help

app_help("piqtree_fit")

# %% [markdown]
# We fit a GTR model and estimate the nucleotide frequencies by maximum likelihood.

# %%
from cogent3 import get_app

fit_gtr = get_app("piqtree_fit", tree, substitution_model="GTR", freq_type="FO")
fit_gtr

# %% [markdown]
# ## Fit the model

# %%
fit = fit_gtr(aln)

# %% [markdown]
# The `fit` object is a cogent3 tree (`PhyloNode`) and the maximum likelihood estimated parameters are stored in the `params` attribute.
#
# > **Note**
# > "lnL" is short for log likelihood and is the log likelihood of the model.
# > "mprobs" is short for motif probabilities and are the estimated equilibrium frequencies of the nucleotides.

# %%
fit.params
