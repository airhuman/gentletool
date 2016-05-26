#!/usr/bin/env python
#! coding: utf-8

try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

extra_compile_args = ['-g', '-fPIC', '-Wall', '-O2']

setup(
    name='gentle_rm',
    version='1.4.1',
    maintainer='Michael Lee',
    maintainer_email='liyong19861014@gmail.com',
    url='https://github.com/airhuman/gentle_rm',
    description='慢慢删除大文件',
    # packages=['mmh'],
    entry_points={
        'console_scripts': [
            'gentle_rm = ',
        ],
    }
)
