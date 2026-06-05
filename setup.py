#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages, Extension
import os
import sys

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

ext_modules = [
    Extension(
        'pyworld.core._pyworld_core',
        sources=['src/pyworld_core.c'],
        include_dirs=['src'],
        extra_compile_args=['-O2'] if sys.platform != 'win32' else ['/O2'],
    )
]

setup(
    name='pyworld',
    version='0.1.0',
    author='cmyk-code-sudo',
    author_email='your-email@example.com',
    description='A Python library for interactive gaming with Chinese NLP, UI systems, and Android support',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cmyk-code-sudo/pyworld',
    packages=find_packages(),
    ext_modules=ext_modules,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Games/Entertainment',
    ],
    python_requires='>=3.7',
    install_requires=[
        'kivy>=2.1.0',
        'jieba>=0.42.1',
        'numpy>=1.19.0',
    ],
    extras_require={
        'dev': [
            'pytest>=6.0',
            'black>=21.0',
            'pylint>=2.10',
        ],
    },
    entry_points={
        'console_scripts': [
            'pyworld=pyworld.cli:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)