""" lambdata - a collection of Data Science helper functions
"""
from setuptools import find_packages, setup

REQUIRED = [
    "numpy",
    "pandas"
]
with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
setup(
    name="lambdata-sean-2",
    version="0.1.4",
    author="Sean",
    description="A collection of Data Science helper functions",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/ssbyrne89/lambdata-sean-2",
    packages=["lambdata_sean"],
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)