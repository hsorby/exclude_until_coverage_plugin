# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0

"""Code coverage measurement plugin for Python"""

from setuptools import setup


classifiers = """\
Environment :: Console
Intended Audience :: Developers
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: Implementation :: CPython
Programming Language :: Python :: Implementation :: PyPy
Programming Language :: Python :: Implementation :: Jython
Programming Language :: Python :: Implementation :: IronPython
Topic :: Software Development :: Quality Assurance
Topic :: Software Development :: Testing
"""


setup(
    name='ExcludeUntilCoveragePlugin',
    version='0.1.0.dev0',
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
