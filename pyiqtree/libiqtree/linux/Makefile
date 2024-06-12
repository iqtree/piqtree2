# Define the compiler and flags
CXX = g++
CXXFLAGS = -fPIC

# Define the directories and file names
LIB_DIR = .
TARGET_DIR = /workspaces/pyiqtree2/pyiqtree
STATIC_LIB = $(LIB_DIR)/libiqtree2.a
WRAPPER_SRC = $(LIB_DIR)/wrapper.cpp
SHARED_LIB = $(TARGET_DIR)/libiqtree.so

# Build the shared library
$(SHARED_LIB): $(WRAPPER_SRC) $(STATIC_LIB)
	$(CXX) -shared -o $@ $(CXXFLAGS) $(WRAPPER_SRC) -L$(LIB_DIR) -liqtree2

# Clean up
clean:
	rm -f $(SHARED_LIB)
