from setuptools import setup, find_packages

with open("Docs/README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="PyDataStructures",  # Replace with your package name
    version="0.0.3",  # Initial version
    author="Sandro Fernandes",
    author_email="Sandro.Fernandes@Softrent.com.br",
    description="Data Structures Class Stack",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SandroFernandes/PyDataStructures",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[],
)
