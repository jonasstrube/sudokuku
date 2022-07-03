import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sudokuku",
    version="0.3.0",
    author="Jonas Strube",
    description="A package for solving sudokus",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonasstrube/sudokuku",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"sudokuku": "sudokuku"},
    packages=setuptools.find_packages(),
    python_requires=">=3.9",
)