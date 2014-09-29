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

class SuserTestCase(unittest.TestCase):
	def setUp(self):
		self.user = sourpy.suser.Suser("vertov")

	def test_get_most_recent_entries(self):
		el = self.user.get_most_recent_entries()

	def test_get_top_entries(self):
		le = self.user.get_top_entries()

	def test_get_most_favorited_entries(self):
		le = self.user.get_most_favorited_entries()

	def test_get_latest_rated_entries(self):
		le = self.user.get_latest_rated_entries()

	def test_get_entries_rated_this_week(self):
		le = self.user.get_entries_rated_this_week()

	def test_get_favorite_entries(self):
		le = self.user.get_favorite_entries()


class InvalidUsername(unittest.TestCase):
	def runTest(self):
		with self.assertRaises(sourpy.common.SourPyException):
			self.user = sourpy.suser.Suser("ğ")

def suite():
	return unittest.TestLoader().loadTestsFromName(__name__)

if __name__ == '__main__':
	unittest.main(defaultTest='suite')
