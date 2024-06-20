from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

__version__ = "0.1"


LIBRARY_DIR = "piqtree2/libiqtree"

ext_modules = [
    Pybind11Extension(
        "piqtree2",
        ["piqtree2/wrapper.cpp"],
        library_dirs=[LIBRARY_DIR],
        libraries=["iqtree2", "z"],
        define_macros=[("VERSION_INFO", __version__)],
    ),
]

setup(
    name="piqtree2",
    version=__version__,
    author="Richard Morris, Robert McArthur",
    author_email="richard.morris@anu.edu.au",
    url="https://github.com/cogent3/piqtree2",
    description="Python bindings for IQTree",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    install_requires=["pybind11"],
    extras_require={"dev": ["pytest"]},
    zip_safe=False,
    python_requires=">=3.9",
)
