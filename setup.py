from setuptools import setup, find_packages

requires = open('requirements.txt', 'r').read().splitlines()

setup(
    name='py-coinmarketcap',
    version='0.0.2',
    description='threadsafe coinmarketcap pro api library for use in high performance environments',
    packages=find_packages(),
    license='MIT',
    author='sharath',
    author_email='sharathramku@umass.edu',
    install_requires=requires,
)
