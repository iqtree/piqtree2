import ctypes

# Load the shared library
wrap = ctypes.CDLL('./wrap.so')

# Define the argument and return types for the function
wrap.wrap_test_function.argtypes = [ctypes.c_char_p]
wrap.wrap_test_function.restype = ctypes.c_int

# Call the function
result = wrap.wrap_test_function(b"Hello, World!")
print("Result:", result)
