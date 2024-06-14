# Makefile

# Compiler
CXX = g++

# Compiler flags
CXXFLAGS = -fPIC -Wall -Wextra

# Targets
TARGET_LIB = test.a
WRAP_LIB = wrap.so

# Object files
OBJS = test.o wrap.o

# All target
all: $(WRAP_LIB)

# Build static library
$(TARGET_LIB): test.o
	ar rcs $@ $^

# Build shared library
$(WRAP_LIB): wrap.o $(TARGET_LIB)
	$(CXX) $(CXXFLAGS) -shared -o $@ wrap.o test.o

# Compile source files into object files
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Clean up build files
clean:
	rm -f *.o *.a *.so

.PHONY: all clean
