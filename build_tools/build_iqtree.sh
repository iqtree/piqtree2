cd iqtree2
git apply ../fpic-iqtree.patch
mkdir build && cd build
cmake -DIQTREE_FLAGS="single" -DBUILD_LIB=ON ..
make -j
cd ../..
mv iqtree2/build/libiqtree2.a piqtree2/libiqtree/