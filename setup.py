from setuptools import setup, find_packages

setup(
    name="j2735_202409",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["pycrate>=0.7.11"],
    python_requires=">=3.8",
    description="SAE J2735 2024-09 ASN.1 definitions for V2X communication",
    author="Will Martin",
    license="Apache-2.0",
)
