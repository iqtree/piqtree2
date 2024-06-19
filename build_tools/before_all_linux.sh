if command -v apt-get &> /dev/null; then
apt-get update -y && apt-get install -y libeigen3-dev libboost-all-dev
elif command -v yum &> /dev/null; then
yum update -y && yum install -y eigen3-devel boost-devel
else
echo "Unsupported package manager";
exit 1;
fi

cd iqtree2
git apply ../fpic-iqtree.patch
mkdir build && cd build
cmake -DIQTREE_FLAGS="single" -DBUILD_LIB=ON ..
make -j
cd ../..
mv iqtree2/build/libiqtree2.a pyiqtree/libiqtree/