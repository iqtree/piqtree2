#include "withoutpic.h"
#include <string>

int non_pic_function(const char* input) {
    std::string str(input);
    return str.length();
}
