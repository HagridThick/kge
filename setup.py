from setuptools import setup

setup(
    name="libkge",
    version="0.1",
    description="A knowledge graph embedding library",
    url="https://github.com/uma-pi1/kge",
    author="Universität Mannheim",
    author_email="rgemulla@uni-mannheim.de",
    packages=["kge"],
    install_requires=[
        "torch==1.4.0",
        "pyyaml",
        "pandas",
        "argparse",
        "path",
        # please check correct behaviour when updating ax platform version!!
        "ax-platform==0.1.10",
        # ------------------------------------------------------------------
        # botorch and gpytorch are dependencies of ax-platform but are 
        # currently fixed to versions that only require torch 1.4.0, 
        # once issue on our side is resolved these configurations should 
        # be removed 
        "botorch==0.2.2",
        "gpytorch==1.0.1",
        # ------------------------------------------------------------------
        "sqlalchemy",
        "torchviz",
        "dataclasses",
        # LibKGE uses numba typed-dicts which is part of the experimental numba API
        # in version 0.48
        # see http://numba.pydata.org/numba-doc/0.48.0/reference/pysupported.html
        "numba==0.48.0",
    ],
    zip_safe=False,
    entry_points={"console_scripts": ["kge = kge.cli:main",],},
)
