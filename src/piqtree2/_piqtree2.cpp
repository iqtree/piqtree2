#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <iostream>
#include <string>

using namespace std;

namespace py = pybind11;

// Calculates the RF distance between two trees
extern int calculate_RF_distance(const string &tree1, const string &tree2);

// Generates a random phylogenetic tree
extern void generate_random_tree_file(int numtaxa, int seed, string tree_gen_mode, string outfile);

// perform phylogenetic analysis on the input alignment file
void phylogenetic_analysis(string& align_file, int ncpus = 1);

int mine(){
    return 42;
}

PYBIND11_MODULE(_piqtree2, m) {
    m.doc() = "piqtree2 - Unlock the Power of IQ-TREE2 with Python!";

    m.def("calculate_RF_distance", &calculate_RF_distance, "Calculate RF distance between two trees");
    m.def("generate_random_tree_file", &generate_random_tree_file, "Generate a random tree to a file");
    m.def("phylogenetic_analysis", &phylogenetic_analysis, "Perform phylogenetic analysis on the input alignment file");
    m.def("mine", &mine, "The meaning of life, the universe (and everything)!");
}
