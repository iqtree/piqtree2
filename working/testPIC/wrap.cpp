// wrap.cpp
extern "C" {
    #include "test.h"  // Header file for test.a

    int wrap_test_function(const char* input) {
        return test_function(input);
    }
}
