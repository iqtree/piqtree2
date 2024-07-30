"""cogent3 apps for piqtree2."""

from cogent3.app.composable import define_app

from piqtree2.iqtree import build_tree, fit_tree, random_trees

piqtree_phylo = define_app(build_tree)
piqtree_fit = define_app(fit_tree)
piqtree_random_trees = define_app(random_trees)
