#!/usr/bin/env python

from setuptools import setup

setup(name='target-rakam',
      version='1.7.0',
      description='Singer.io target for the Rakam API',
      author='Rakam',
      url='https://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['target_rakam'],
      install_requires=[
          'jsonschema==2.6.0',
          'mock==2.0.0',
          'requests==2.18.4',
          'singer-python==5.0.0',
          'psutil==5.3.1'
      ],
      entry_points='''
          [console_scripts]
          target-rakam=target_rakam:main
      ''',
      packages=['target_rakam'],
)
