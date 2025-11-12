from setuptools import setup,find_packages

setup(
    name="document_portal",
    author="Rahul Giri",
    packages=find_packages(),
    version="0.1",
    desqription="A portal to manage documents efficiently",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)