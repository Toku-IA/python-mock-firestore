import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mock-firestore",
    version="0.11.2",
    author="",
    description="In-memory implementation of Google Cloud Firestore for use in tests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Toku-IA/python-mock-firestore",
    packages=setuptools.find_packages(),
    test_suite="",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
)
