# -*- coding: utf-8 -*-
"""Installer for the ploneutfpr.atreferencepatch package."""

from setuptools import find_packages
from setuptools import setup


long_description = (
    open('README.rst').read() +
    '\n' +
    'Contributors\n' +
    '============\n' +
    '\n' +
    open('CONTRIBUTORS.rst').read() +
    '\n' +
    open('CHANGES.rst').read() +
    '\n')


setup(
    name='ploneutfpr.atreferencepatch',
    version='1.0a1',
    description="Patch para consertar: https://community.plone.org/t/problems-editing-existing-page-in-plone-4-3-nonetype-object-errors/768/14",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='Leandro Koiti Sato',
    author_email='lksato@utfpr.edu.br',
    url='https://pypi.python.org/pypi/ploneutfpr.atreferencepatch',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['ploneutfpr'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.api',
        'setuptools',
        'z3c.jbot',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
