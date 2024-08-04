__version__ = "1.1.1"

from setuptools import setup

setup(
    name="skytemple-3rdparty-typestubs",
    version=__version__,
    packages=["ndspy", "igraph"],
    package_data={"igraph": ["py.typed", "*.pyi"], "ndspy": ["py.typed", "*.pyi"]},
    description="(Minimal) PEP 561 type stubs for libraries SkyTemple uses",
    url="https://github.com/SkyTemple/3rdparty-typestubs/",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
    ],
)
