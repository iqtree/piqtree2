// test.h
#ifndef TEST_H
#define TEST_H

#ifdef __cplusplus
extern "C" {
#endif

__attribute__((visibility("default"))) int test_function(const char* input);

#ifdef __cplusplus
}
#endif

#endif // TEST_H
