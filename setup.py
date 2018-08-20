from setuptools import setup, find_packages

requires = open('requirements.txt', 'r').read().splitlines()

setup(
    name='cmc',
    version='0.0.1',
    description='threadsafe coinmarketcap pro api library for use in high performance environments with support '
                'for webscraping as well as the pro api',
    packages=find_packages(),
    license='MIT',
    author='sharath',
    author_email='sharathramku@umass.edu',
    install_requires=requires,
)
