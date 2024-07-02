from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

LIBRARY_DIR = "src/piqtree2/libiqtree"

ext_modules = [
    Pybind11Extension(
        "_piqtree2",
        ["src/piqtree2/_piqtree2.cpp"],
        library_dirs=[LIBRARY_DIR],
        libraries=["iqtree2", "z"],
    ),
]

setup(
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    entry_points={
        "cogent3.app": [
            "piqtree_phylo = piqtree2._app:piqtree_phylo",
            "piqtree_fit = piqtree2._app:piqtree_fit",
            "piqtree_random_trees = piqtree2._app:piqtree_random_trees",
        ]
    },
)
