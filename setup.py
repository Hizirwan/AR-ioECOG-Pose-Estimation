from setuptools import setup, find_packages

setup(
    name='MyProject',
    version='0.1',
    packages=find_packages(include=['hl2ss', 'hl2ss.*']),
)
