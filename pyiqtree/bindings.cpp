#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

// Declare the external C++ functions
extern int calculate_RF_distance(const std::string &tree1, const std::string &tree2);
extern void generate_random_tree_file(int numtaxa, int seed, const std::string &gen_mode, const std::string &filename);
extern void phylogenetic_analysis(const std::string &alignment_file, int ncpus);

// Wrapper functions
int RF_distance(const std::string &tree1, const std::string &tree2) {
    return calculate_RF_distance(tree1, tree2);
}

void generate_random_tree_file_wrapper(int numtaxa, int seed, const std::string &gen_mode, const std::string &filename) {
    generate_random_tree_file(numtaxa, seed, gen_mode, filename);
}

void phylogenetic_analysis_wrapper(const std::string &alignment_file, int ncpus) {
    phylogenetic_analysis(alignment_file, ncpus);
}

PYBIND11_MODULE(libiqtree, m) {
    m.def("RF_distance", &RF_distance, "Calculate RF distance between two trees");
    m.def("generate_random_tree_file", &generate_random_tree_file_wrapper, "Generate a random tree file");
    m.def("phylogenetic_analysis", &phylogenetic_analysis_wrapper, "Perform phylogenetic analysis");
}
