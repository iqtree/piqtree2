#ifndef WRAP_H
#define WRAP_H

#ifdef __cplusplus
extern "C" {
#endif

__attribute__((visibility("default"))) int wrap_test_function(const char* input);
__attribute__((visibility("default"))) int wrap_non_pic_function(const char* input);

#ifdef __cplusplus
}
#endif

#endif // WRAP_H
