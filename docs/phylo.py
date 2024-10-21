# %% [markdown]
# ## Building phylogenies using `piqtree_phylo`
# For this simple case, we will build a single phylogeny using the GTR model on one alignment.
# We have a utility script for this documentation that provides the local path to that data. We will then load that data and, as it contains quite a few sequences, we will use a subset of it. We use methods on the cogent3 object to do that.

# %%
import cogent3

import doc_rsrc

# todo put this data selection code in the doc_rsrc.py file
aln_path = doc_rsrc.data_path("brca1.fasta.gz")
aln = cogent3.load_aligned_seqs(aln_path, moltype="dna")
primates = [
    "FlyingLem",
    "Galago",
    "HowlerMon",
    "Rhesus",
    "Orangutan",
    "Gorilla",
    "Human",
    "Chimpanzee",
]
aln = aln.take_seqs(primates)
aln = aln.omit_gap_pos(allowed_gap_frac=1 / len(primates))
aln


# %% [markdown]
# We now take a look at the help for the `piqtree_phylo` app.

# %%

from cogent3 import app_help

app_help("piqtree_phylo")

# %% [markdown]
# We build an app for estimating phylogenies with a GTR model

# %%
from cogent3 import get_app

phylo_gtr = get_app("piqtree_phylo", "GTR")
phylo_gtr

# %% [markdown]
# ## Run the phylogeny estimation!

# %%
result = phylo_gtr(aln)
dnd = result.get_figure()
dnd.show(width=600, height=600)
