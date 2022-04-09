#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import setuptools


with open('README.md', 'r') as fin:
    long_description = fin.read()
with open('LICENSE', 'r') as fin:
    license = fin.read()

setuptools.setup(
    name='vimlib',
    version='0.0.1',
    license='MIT',
    author='Kyle L. Davis',
    author_email='AceofSpades5757.github@gmail.com',
    url='https://github.com/AceofSpades5757/vimlib',
    description='Friendly Python interface for interacting with Vim.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    packages=setuptools.find_packages('src'),
    package_dir={
        '': 'src',
        'pyvim': 'src/pyvim',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)