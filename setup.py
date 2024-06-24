from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup, find_packages

__version__ = "0.1"

LIBRARY_DIR = "src/piqtree2/libiqtree"

ext_modules = [
    Pybind11Extension(
        "_piqtree2",
        ["src/piqtree2/_piqtree2.cpp"],
        library_dirs=[LIBRARY_DIR],
        libraries=["iqtree2", "z"],
        define_macros=[("VERSION_INFO", __version__)],
    ),
]
print(find_packages())
setup(
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False
)
