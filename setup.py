# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in acustom_addon/__init__.py
from acustom_addon import __version__ as version

setup(
	name='acustom_addon',
	version=version,
	description='Custom Settings',
	author='Beshoy Atef',
	author_email='beshoyatef31@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
