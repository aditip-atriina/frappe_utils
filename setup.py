# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in utils/__init__.py
from utils import __version__ as version

setup(
	name='utils',
	version=version,
	description='Frappe & Bench utilities',
	author='Neel Bhanushali',
	author_email='neal.bhanushali@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
