#!/usr/bin/python
# -*- coding: utf-8 -*-

#--------------------------------------------------------------------
# Copyright (c) 2014 Eren Inan Canpolat
# Author: Eren Inan Canpolat <eren.canpolat@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#--------------------------------------------------------------------

from setuptools import setup
import re

version = "0.2.1"
description = "Ekşi Sözlük scraper"
url = "https://github.com/canpolat/sourpy"
author = "Eren Inan Canpolat"
author_email = "eren.canpolat@gmail.com"

setup(name='sourpy',
	version=version,
	description=description,
	long_description=open('README.rst').read(),
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Environment :: Web Environment',
		'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 2.7',
		'Topic :: Internet',
	],
	url=url,
	author=author,
	author_email=author_email,
	packages=['sourpy'],
	install_requires=[
		"beautifulsoup4>=4.3.2",
	],
	include_package_data=True,
	zip_safe=False)
