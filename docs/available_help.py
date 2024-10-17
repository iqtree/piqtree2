# %% [markdown]
# To see the apps that `piqtree2` makes available, use the cogent3 function `available_apps()` as follows.

# %%
from cogent3 import available_apps

available_apps("piqtree")

# %% [markdown]
# For a particular app, use the cogent3 function `app_help()` to find out what the options are.

# %%
from cogent3 import app_help

app_help("piqtree_phylo")

# %% [markdown]
# ## What substitution models are available
# You can list all the DNA substitution models `piqtree2` supports.

# %%
from cogent3 import get_app

dna_models = get_app("piqtree_list_available", element_type="model")
dna_models("dna").head(3)  # just the first 3 models

# %% [markdown]
# ## What rate heterogeneity models are available

# %%
rate_het = get_app("piqtree_list_available", element_type="rate")
rate_het("")
