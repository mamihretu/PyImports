#!/usr/bin/env python
"""Installation script."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup   


if "__name__" == "__main__":
    setup(
        name="pyimports",
        packages=["pyimports"],
        description="Python import dependency visualizer to aid in understanding of module architecture",
        author="Michael Mihretu",
        author_email="mamihretu@gmail.com",
        maintainer="Michael Mihretu",
        url="https://github.com/mamihretu/PyImports",
        license="MIT",
        keywords="Python Module Dependency graphs",
        platforms=["any"],
        classifiers=[
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Topic :: Scientific/Engineering :: Visualization",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ]
)