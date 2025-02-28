# Import the necessary libraries
from setuptools import setup, find_packages

setup(
    name="datacleaner",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",   # Essential for data handling
        "typer",    # CLI framework
        "rich",     # For coloured CLI output
        "logging",  # For logging the outputs
        "numpy"     # Needed for numerical operations
    ],
    entry_points={
        "console_scripts": [
            "datacleaner=src.cli:app"   # Allows running 'datacleaner' in terminal.
        ]
    },
    author= "David Ahonsu",
    author_email="olivetahonsu@gmail.com",
    description="A tool for data cleaning and missing value handling.",
    url="https://github.com/olivetahonsu/datacleaner",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache 2.0",
        "Operatiing System :: OS Independent",
    ],
    python_requires=">3.7",
)

