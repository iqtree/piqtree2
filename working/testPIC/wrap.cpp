#include "wrap.h"
#include "test.h"
#include "withoutpic.h"
#include <iostream>
#include <cstring>

extern "C" {
    int wrap_test_function(const char* input) {
        return test_function(input);
    }

    int wrap_non_pic_function(const char* input) {
        return non_pic_function(input);
    }
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " function_name [args...]" << std::endl;
        return 1;
    }

    const char *func_name = argv[1];
    if (std::strcmp(func_name, "test_function") == 0) {
        if (argc != 3) {
            std::cerr << "Usage: " << argv[0] << " test_function input" << std::endl;
            return 1;
        }
        int result = wrap_test_function(argv[2]);
        std::cout << result << std::endl;
    } else if (std::strcmp(func_name, "non_pic_function") == 0) {
        if (argc != 3) {
            std::cerr << "Usage: " << argv[0] << " non_pic_function input" << std::endl;
            return 1;
        }
        int result = wrap_non_pic_function(argv[2]);
        std::cout << result << std::endl;
    } else {
        std::cerr << "Unknown function: " << func_name << std::endl;
        return 1;
    }

    return 0;
}
