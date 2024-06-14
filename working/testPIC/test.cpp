// test.cpp
#include "test.h"
#include <string>

int test_function(const char* input) {
    std::string str(input);
    return str.length();
}
