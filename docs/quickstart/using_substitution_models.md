# Use different kinds of substitution models

piqtree currently supports all named IQ-TREE DNA models including Lie Markov models, empirical amino-acid exchange rate matrices,
as well as specification for base frequencies and rate heterogeneity across sites.

We use the [`Model`](../api/model/Model.md) class to represent the substitution model which can be constructed from strings, or
using enums. Substitution models can be combined with specification for base frequencies, and rate heterogeneity across sites models.

## Usage

### DNA Models

DNA models may be specified using the [`DnaModel`](../api/model/SubstitutionModel.md#piqtree.model.DnaModel) enum, or by using
the IQ-TREE string representation. A full list of supported DNA models is available [here](../api/model/SubstitutionModel.md#piqtree.model.DnaModel).

```python
from piqtree import Model
from piqtree.model import DnaModel

hky_model_1 = Model("HKY")
hky_model_2 = Model(DnaModel.HKY)

lie_6_6_model_1 = Model("6.6")
lie_6_6_model_2 = Model(DnaModel.LIE_6_6)
```

### Amino-acid Models

Amino-acid models may be specified using the [`AaModel`](../api/model/SubstitutionModel.md#piqtree.model.AaModel) enum, or by using
the IQ-TREE string representation. A full list of supported amino-acid models is available [here](../api/model/SubstitutionModel.md#piqtree.model.AaModel).

```python
from piqtree import Model
from piqtree.model import AaModel

dayhoff_model_1 = Model("Dayhoff")
dayhoff_model_2 = Model(AaModel.Dayhoff)

nq_yeast_model_1 = Model("NQ.yeast")
nq_yeast_model_2 = Model(AaModel.NQ_yeast)
```

### Base Frequencies

Three types of base frequencies can be specified using either the [`FreqType`](../api/model/FreqType.md), or strings.
If not specified, it uses the chosen model's default.

- [`F`](../api/model/FreqType.md#piqtree.model.FreqType.F): Empirical base frequencies.
- [`FQ`](../api/model/FreqType.md#piqtree.model.FreqType.FQ): Equal base frequencies.
- [`FO`](../api/model/FreqType.md#piqtree.model.FreqType.FO): Optimised base frequencies by maximum-likelihood.

```python
from piqtree import Model
from piqtree.model import FreqType

# Default for the GTR model
empirical_freqs_1 = Model("GTR", freq_type="F")
empirical_freqs_2 = Model("GTR", freq_type=FreqType.F)

equal_freqs_1 = Model("GTR", freq_type="FQ")
equal_freqs_2 = Model("GTR", freq_type=FreqType.FQ)

opt_freqs_1 = Model("GTR", freq_type="FO")
opt_freqs_2 = Model("GTR", freq_type=FreqType.FO)
```

### Rate Heterogeneity

#### Invariable Sites

A boolean flag can be specified when constructing the [`Model`](../api/model/Model.md) class to allow for a proportion of invariable sites.

```python
from piqtree import Model

without_invar_sites = Model("TIM", invariant_sites=False) # Default
with_invar_sites = Model("TIM", invariant_sites=True)
```

#### Discrete Gamma Model

We support the [`DiscreteGammaModel`](../api/model/RateModel.md#piqtree.model.DiscreteGammaModel) allowing for a variable number of rate categories (by default 4).

```python
from piqtree import Model
from piqtree.model import DiscreteGammaModel

# 4 rate categories, no invariable sites
k81_discrete_gamma_4 = Model("K81", rate_model=DiscreteGammaModel())

# 8 rate categories, with invariable sites
k81_invar_discrete_gamma_8 = Model("K81", rate_model=DiscreteGammaModel(8), invariant_sites=True)
```

#### FreeRate Model

We support the [`FreeRateModel`](../api/model/RateModel.md#piqtree.model.FreeRateModel) allowing for a variable number of rate categories (by default 4).

```python
from piqtree import Model
from piqtree.model import FreeRateModel

# 4 rate categories, no invariable sites
sym_discrete_gamma_4 = Model("SYM", rate_model=FreeRateModel())

# 8 rate categories, with invariable sites
sym_invar_discrete_gamma_8 = Model("SYM", rate_model=FreeRateModel(8), invariant_sites=True)
```

## See also

- Use a [`Model`](../api/model/Model.md) to construct a maximum likelihood tree: ["Construct a maximum likelihood phylogenetic tree"](construct_ml_tree.md).
- Use a [`Model`](../api/model/Model.md) to fit branch lengths to a tree topology: ["Fit branch lengths to a tree topology from an alignment"](fit_tree_topology.md).
