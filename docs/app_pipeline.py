# %% [markdown]
# ## Building workflows using `piqtree2` apps
# We can combine `piqtree2` apps with other cogent3 apps to develop a pipeline. There are multiple concepts involved here, particularly data stores, composed apps, parallel execution, log files etc... See the cogent3 [app documentation](https://cogent3.org/doc/app/index.html) for more details.
#
# To develop a pipeline efficiently we only need a subset of the sequences in an alignment. We will use the [diverse-seq](https://pypi.org/project/diverse-seq/) plugin for that purpose. This allows selecting a specified subset of sequences that capture the diversity in an alignment.
#
# But first, we need the data.
# %%
from piqtree2 import download_dataset

alns_path = download_dataset("mammal-orths.zip", dest_dir="data", inflate_zip=True)

# %% [markdown]
# We open this directory as a cogent3 data store.

# %%
from cogent3 import open_data_store

dstore = open_data_store(alns_path, suffix="fa")
dstore.describe
