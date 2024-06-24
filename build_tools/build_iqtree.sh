cd iqtree2
git apply ../fpic-iqtree.patch
rm -rf build
mkdir build && cd build
cmake -DIQTREE_FLAGS="single" -DBUILD_LIB=ON ..
make
cd ../..
mv iqtree2/build/libiqtree2.a piqtree2/libiqtree/