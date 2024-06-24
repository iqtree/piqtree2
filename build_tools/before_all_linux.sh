if command -v apt-get &> /dev/null; then
apt-get update -y && apt-get install -y libeigen3-dev libboost-all-dev
apt install llvm
elif command -v yum &> /dev/null; then
yum update -y && yum install -y eigen3-devel boost-devel llvm-toolset-7
elif command -v apk &> /dev/null; then
apk update && apk add eigen-dev boost-dev llvm15
else
echo "Unsupported package manager";
exit 1;
fi

bash build_tools/build_iqtree.sh