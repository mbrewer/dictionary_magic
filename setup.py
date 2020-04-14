import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dictionaries-maloret", # Replace with your own username
    version="1.0.0",
    author="Mallory Brewer",
    author_email="maloret@gmail.com",
    description="A small dictionary program",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mbrewer/dictionary_magic",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)