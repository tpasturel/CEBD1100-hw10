import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CEBD1100hw8ThibaultPasturel_pkg_tpasturel",
    version="0.0.3",
    author="Thibault Pasturel",
    author_email="thibault.pasturel@gmail.com",
    description="This script allows to plot and compare sklearn wine dataset's column by pairs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tpasturel/CEBD1100-hw8",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
