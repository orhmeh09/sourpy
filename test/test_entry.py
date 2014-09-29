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

class InvalidEntryID_NonNumeric(unittest.TestCase):
	def runTest(self):
		with self.assertRaises(sourpy.common.SourPyException):
			entry = sourpy.get_entry("ğ")

class InvalidEntryID_NumericString(unittest.TestCase):
	def runTest(self):
		with self.assertRaises(sourpy.common.SourPyException):
			entry = sourpy.get_entry("-1")

class InvalidEntryID_Integer(unittest.TestCase):
	def runTest(self):
		with self.assertRaises(AttributeError):
			entry = sourpy.get_entry(4)


"""
{'commentText': u'gitar calmak icin kullanilan minik plastik garip nesne.',
 'creation-time': u'1999-02-15T00:00:00',
 'creator': u'ssg',
 'creator-url': u'/biri/ssg',
 'id': u'1',
 'last-update-time': u'1999-02-15T00:00:00',
 'title': u'pena'}

"""
class ValidEntryID_Pena(unittest.TestCase):
	def runTest(self):
		entry = sourpy.get_entry("1")
		self.assertEqual(entry["creator"], u"ssg")
		self.assertEqual(entry["creator-url"], u"/biri/ssg")
		self.assertEqual(entry["id"], u"1")
		self.assertEqual(entry["commentText"], u"gitar calmak icin kullanilan minik plastik garip nesne.")
		self.assertEqual(entry["creation-time"], u"1999-02-15T00:00:00")
		self.assertEqual(entry["last-update-time"], u"1999-02-15T00:00:00")
		self.assertEqual(entry["title"], u"pena")

def suite():
	return unittest.TestLoader().loadTestsFromName(__name__)

if __name__ == '__main__':
	unittest.main(defaultTest='suite')
