import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
    name = "xmlsoccer",
    version = "0.2",
    description = "Parse xmlsoccer feed",
    author = "Martin Eastwood, bmcculley",
    author_email = "admin@stattaca.com",
    url = "https://github.com/bmcculley/xmlsoccer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests >= 2.19.1",
    ],
)