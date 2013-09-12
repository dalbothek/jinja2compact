#!/usr/bin/env python
# -*- coding: utf8 -*-
import setuptools


setuptools.setup(
    name="jinja2compact",
    version="1.0",
    packages=setuptools.find_packages(),
    zip_safe=True,
    author="Simon Marti",
    author_email="simon.marti@ceilingcat.ch",
    install_requires=("jinja2",)
)
