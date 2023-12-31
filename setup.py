import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ezpacket",
    version="0.0.6",
    author="Yunus Gungor",
    author_email="yunusgnr@gmail.com",
    description="A module for writing easy to understand byte packets and byte manipulations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ynsgnr/ez-packet",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)