#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

namespace py = pybind11;

/*
 * Calculates the robinson fould distance between two trees
 */
extern int robinson_fould(const string& tree1, const string& tree2);

/*
 * Generates a set of random phylogenetic trees
 * tree_gen_mode allows:"YULE_HARDING", "UNIFORM", "CATERPILLAR", "BALANCED",
 * "BIRTH_DEATH", "STAR_TREE" output: a newick tree (in string format)
 */
extern string random_tree(int num_taxa,
                          string tree_gen_mode,
                          int num_trees,
                          int rand_seed = 0);

/*
 * Perform phylogenetic analysis on the input alignment
 * With estimation of the best topology
 * output: results in YAML format with the tree and the details of parameters
 */
extern string build_tree(vector<string>& names,
                         vector<string>& seqs,
                         string model,
                         int rand_seed = 0,
                         int bootstrap_rep = 0,
                         int num_thres = 1);

/*
 * Perform phylogenetic analysis on the input alignment
 * With restriction to the input toplogy
 * output: results in YAML format with the details of parameters
 */
extern string fit_tree(vector<string>& names,
                       vector<string>& seqs,
                       string model,
                       string intree,
                       int rand_seed = 0,
                       int num_thres = 1);

/*
 * Perform phylogenetic analysis with ModelFinder
 * on the input alignment (in string format)
 * model_set -- a set of models to consider
 * freq_set -- a set of frequency types
 * rate_set -- a set of RHAS models
 * rand_seed -- random seed, if 0, then will generate a new random seed
 * output: modelfinder results in YAML format
 */
extern string modelfinder(vector<string>& names,
                          vector<string>& seqs,
                          int rand_seed = 0,
                          string model_set = "",
                          string freq_set = "",
                          string rate_set = "",
                          int num_thres = 1);

/*
 * Build pairwise JC distance matrix
 * output: set of distances
 * (n * i + j)-th element of the list represents the distance between i-th and
 * j-th sequence, where n is the number of sequences
 */
extern vector<double> build_distmatrix(vector<string>& names,
                                       vector<string>& seqs,
                                       int num_thres);

/*
 * Using Rapid-NJ to build tree from a distance matrix
 * output: a newick tree (in string format)
 */
extern string build_njtree(vector<string>& names, vector<double>& distances);

/*
 * verion number
 */
extern string version();

int mine() {
  return 42;
}

PYBIND11_MODULE(_piqtree2, m) {
  m.doc() = "piqtree2 - Unlock the Power of IQ-TREE2 with Python!";

  m.attr("__iqtree_version__") = version();

  m.def("iq_robinson_fould", &robinson_fould,
        "Calculates the robinson fould distance between two trees");
  m.def("iq_random_tree", &random_tree,
        "Generates a set of random phylogenetic trees. tree_gen_mode "
        "allows:\"YULE_HARDING\", \"UNIFORM\", \"CATERPILLAR\", \"BALANCED\", "
        "\"BIRTH_DEATH\", \"STAR_TREE\".");
  m.def("iq_build_tree", &build_tree,
        "Perform phylogenetic analysis on the input alignment (in string "
        "format). With estimation of the best topology.");
  m.def("iq_fit_tree", &fit_tree,
        "Perform phylogenetic analysis on the input alignment (in string "
        "format). With restriction to the input toplogy.");
  m.def("iq_model_finder", &modelfinder,
        "Find optimal model for an alignment.");
  m.def("iq_jc_distances", &build_distmatrix,
        "Construct pairwise distance matrix for alignment.");
  m.def("iq_nj_tree", &build_njtree,
        "Build neighbour-joining tree from distance matrix.");
  m.def("mine", &mine, "The meaning of life, the universe (and everything)!");
}
