"""cogent3 apps for piqtree2."""

from cogent3.app.composable import define_app

from piqtree2 import _iq_wrappers as iqtree

piqtree_phylo = define_app(iqtree.build_tree)
piqtree_fit = define_app(iqtree.fit_tree)
piqtree_random_trees = define_app(iqtree.random_trees)
