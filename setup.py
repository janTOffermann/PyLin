#from distutils.core import setup

import setuptools

setuptools.setup(
    name='PyLin',
    version='0.2.4',
    author='Jan Offermann',
    author_email='jano@uchicago.edu',
    packages=setuptools.find_packages(),
    url='http://pypi.python.org/pypi/PyLin/',
    license='LICENSE.txt',
    description='Lin Engineering step motor driver software.',
    long_description=open('README.md').read(),
    install_requires=[
	'pyserial'
    ],
)
