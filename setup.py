import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="QtSpreadSheet-kevinfol",
    version="0.0.1",
    author="Kevin Foley",
    author_email="kevinfol@umich.edu",
    description="A Spreadsheet widget for PyQt5 applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)