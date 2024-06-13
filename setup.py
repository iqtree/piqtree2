from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext
import os

ext_modules = [
    Pybind11Extension(
        "pyiqtree.libiqtree",
        ["pyiqtree/bindings.cpp"],
        include_dirs=["/path/to/includes"],  # Adjust this path
        library_dirs=["/workspaces/pyiqtree2/pyiqtree/libiqtree"],  # Path to the directory containing libiqtree.so
        libraries=["iqtree"],  # This is the base name of libiqtree.so on linus, libiqtree.dylib on MacOS, iqtree.dll on Windows
        extra_compile_args=["-std=c++11", "-fopenmp"],
    )
]

setup(
    name="pyiqtree",
    version="0.1",
    author="Richard Morris",
    author_email="richard.morris@anu.edu.au",
    description="Python bindings for IQTree",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    packages=["pyiqtree"],
    entry_points={
        "cogent3.apps": [
            "RF_distance = pyiqtree:RF_distance",
            "generate_random_tree_file = pyiqtree:generate_random_tree_file",
            "phylogenetic_analysis = pyiqtree:phylogenetic_analysis"
        ]
    },
    install_requires=[
        "pybind11"
    ],
    extras_require={
        "dev": ["pytest"]
    },
    zip_safe=False,
)
