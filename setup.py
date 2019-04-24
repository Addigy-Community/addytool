import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="addytool",
    version="0.0.3",
    author="Benjamin Morales",
    author_email="bmorales@gocirrus.com",
    description="A package for managing Addigy more intelligently.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Addigy-Community/addytool",
    packages=setuptools.find_packages(),
    classifiers=[
        "Operating System :: MacOS :: MacOS X",
    ],
    install_requires=[
        'requests',
        'keyring',
    ],
)
