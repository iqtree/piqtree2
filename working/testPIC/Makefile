# Makefile

# Compiler
CXX = g++

# Compiler flags
CXXFLAGS = -Wall -Wextra

# Targets
WRAP_EXE = wrap
STATIC_LIB1 = test.a
STATIC_LIB2 = withoutpic.a

# Object files
TEST_OBJS = test.o
WITHOUTPIC_OBJS = withoutpic.o
WRAP_OBJS = wrap.o

# All target
all: $(STATIC_LIB1) $(WRAP_EXE)

# Build test.a
$(STATIC_LIB1): $(TEST_OBJS) $(STATIC_LIB2)
	ar rcs $@ $^

# Build withoutpic.a
$(STATIC_LIB2): $(WITHOUTPIC_OBJS)
	ar rcs $@ $^

# Build the PIE executable
$(WRAP_EXE): $(WRAP_OBJS) $(STATIC_LIB1)
	$(CXX) $(CXXFLAGS) -pie -o $@ $(WRAP_OBJS) $(STATIC_LIB1) $(STATIC_LIB2)

# Compile source files into object files
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Clean up build files
clean:
	rm -f *.o *.a $(WRAP_EXE)

.PHONY: all clean
