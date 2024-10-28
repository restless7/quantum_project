from setuptools import setup, find_packages

setup(
    name="quantum_project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'complextensor',
        'torch',
        'numpy',
        'matplotlib'
    ]
)