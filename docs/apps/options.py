# %% [markdown]
# ## Site-heterogeneity model types


# %%
from piqtree import available_rate_type

available_rate_type()

# %% [markdown]
# ## State frequency types

# %% tags=hide_code

from piqtree import available_freq_type

available_freq_type()

# %% [markdown]
# ## Substitution model types
# Assign the value in the "Abbreviation" column as a string to the `submod_type` parameter, e.g.
# ```python
# submod_type="GTR"
# ```


# %%
from piqtree import available_models

available_models()
