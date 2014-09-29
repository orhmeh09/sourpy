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

import unittest

import sourpy

class GundemTest(unittest.TestCase):
	def setUp(self):
		self.gundem = sourpy.get_gundem()

	def test_count(self):
		self.assertEqual(len(self.gundem), 50)

	def test_urls_exist(self):
		for e in self.gundem:
			u = e["url"]
			self.assertNotEqual(u, u"")

	def test_titles_exist(self):
		for e in self.gundem:
			t = e["title"]
			self.assertNotEqual(t, u"")

def suite():
	return unittest.TestLoader().loadTestsFromName(__name__)

if __name__ == '__main__':
	unittest.main(defaultTest='suite')
