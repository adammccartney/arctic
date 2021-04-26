#!/usr/bin/env python
import setuptools


install_requires = ["abjad==3.2", "mypy", "roman", "pytest"]

keywords = [
    "abjad",
    "music composition",
    "music notation",
    "formalized score control",
    "lilypond",
]

if __name__ == "__main__":
    setuptools.setup(
        author="Adam McCartney",
        author_email="adam@mur.at",
        install_requires=install_requires,
        keywords=", ".join(keywords),
        name="arctic",
        packages=["arctic"],
        platforms="Any",
        url="https://github.com/adammccartney/arctic",
    )
