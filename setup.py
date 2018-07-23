# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0

"""Code coverage measurement plugin for Python"""
import os
import re
import codecs

from setuptools import setup


classifiers = [
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Programming Language :: Python :: Implementation :: Jython",
    "Programming Language :: Python :: Implementation :: IronPython",
    "Topic :: Software Development :: Quality Assurance",
    "Topic :: Software Development :: Testing",
]

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    print(os.path.join(here, *parts))
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='ExcludeUntilCoveragePlugin',
    version=find_version('src', 'coverage_plugin', 'exclude_until.py'),
    author='Hugh Sorby',
    author_email='h.sorby@auckland.ac.nz',
    packages=['coverage_plugin',],
    package_dir={'': 'src'},
    url='https://github.com/hsorby/exclude_until_coverage_plugin/',
    license='Apache Software License',
    description='Plugin for code coverage excluding lines until marker found.',
    long_description=open('README.rst').read(),
    zip_safe=False,
    classifiers=classifiers,
    install_requires=['coverage']
)
