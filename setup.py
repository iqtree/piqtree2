"""setup for piqtree2."""

import os
import platform
import subprocess

from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

LIBRARY_DIR = "src/piqtree2/_libiqtree"

# ext_modules = [
#     Pybind11Extension(
#         "_piqtree2",
#         ["src/piqtree2/_libiqtree/_piqtree2.cpp"],
#         library_dirs=[LIBRARY_DIR],
#         libraries=["iqtree2", "z"],
#         extra_compile_args=(["-Xpreprocessor"] if platform.system() == "Darwin" else [])
#         + ["-fopenmp"],
#         extra_link_args=["-lgomp"],
#     ),
# ]


def get_brew_prefix(package):
    """Get the prefix path for a specific Homebrew package"""
    return (
        subprocess.check_output(["brew", "--prefix", package]).strip().decode("utf-8")
    )


# Ensure we get Homebrew's paths for clang and libomp
if platform.system() == "Darwin":
    # Get Homebrew's prefix for llvm and libomp
    brew_prefix_llvm = get_brew_prefix("llvm")
    brew_prefix_libomp = get_brew_prefix("libomp")

    # Set CC and CXX to use Homebrew's clang and clang++
    os.environ["CC"] = os.path.join(brew_prefix_llvm, "bin", "clang")
    os.environ["CXX"] = os.path.join(brew_prefix_llvm, "bin", "clang++")

    # Define OpenMP flags and libraries for macOS
    openmp_flags = ["-Xpreprocessor", "-fopenmp"]
    openmp_libs = ["-lomp"]

    # Use the paths from Homebrew for libomp
    openmp_include = os.path.join(brew_prefix_libomp, "include")
    library_dirs = [
        os.path.join(brew_prefix_libomp, "lib"),
        os.path.join(brew_prefix_llvm, "lib"),
    ]
else:
    # On Linux, use the standard OpenMP flags
    openmp_flags = ["-fopenmp"]
    openmp_libs = ["-lgomp"]
    openmp_include = None
    library_dirs = []

ext_modules = [
    Pybind11Extension(
        "_piqtree2",
        ["src/piqtree2/_libiqtree/_piqtree2.cpp"],
        library_dirs=[
            *library_dirs,
            LIBRARY_DIR,
        ],  # Ensure other dirs like LIBRARY_DIR are still included
        libraries=["iqtree2", "z", *openmp_libs],  # Add OpenMP libraries if needed
        extra_compile_args=openmp_flags,  # Add OpenMP compile flags
        extra_link_args=openmp_libs,  # Link OpenMP library
        include_dirs=[openmp_include]
        if openmp_include
        else [],  # Include OpenMP headers
    ),
]

setup(
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
)
