#!/usr/bin/env python
# -*- coding: utf8 -*-
import setuptools


setuptools.setup(
    name="jinja2compact",
    description="Reduce whitespace in jinja2 templates at compile time",
    url="https://github.com/sadimusi/jinja2compact",
    version="1.1",
    packages=setuptools.find_packages(),
    zip_safe=True,
    author="Simon Marti",
    author_email="simon.marti@ceilingcat.ch",
    install_requires=("jinja2",),
    license="WTFPL",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: HTML'
    ],
)
