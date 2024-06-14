#include "test.h"
#include "withoutpic.h"
#include <string>

int test_function(const char* input) {
    std::string str(input);
    int length = str.length();
    int additional_length = non_pic_function(input);
    return length + additional_length;
}
