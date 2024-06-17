#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <iostream>
#include <string>

using namespace std;

namespace py = pybind11;

// Declare the external C++ functions
extern int calculate_RF_distance(const string &tree1, const string &tree2);

int mine(){
    return 42;
}

PYBIND11_MODULE(pyiqtree, m) {
    m.doc() = "PyIQTree - Unlock the Power of IQTree with Python!";

    m.def("calculate_RF_distance", &calculate_RF_distance, "Calculate RF distance between two trees");
    m.def("mine", &mine, "The meaning of life, the universe (and everything)!");
}
