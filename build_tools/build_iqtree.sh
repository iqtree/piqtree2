cd iqtree2
rm -rf build
mkdir build && cd build
cmake -DIQTREE_FLAGS="single" -DBUILD_LIB=ON ..
make -j
cd ../..
mv iqtree2/build/libiqtree2.a src/piqtree2/_libiqtree/