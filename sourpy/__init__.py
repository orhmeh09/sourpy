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

import urllib2
from bs4 import BeautifulSoup
import re
import string

import common
import suser

############ LOGGING ########################
import logging
log = logging.getLogger("sourpy.main")

logging.basicConfig(level=logging.DEBUG,
			format='%(asctime)s %(name)-20s %(levelname)-8s %(message)s',
			datefmt='%m-%d %H:%M',
			filename='sourpy.log',
			filemode='w')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-24s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#############################################

def get_entry(entry_id):
	if not entry_id.isdigit():
		raise common.SourPyException("Entry ID should be a number. Current value: {}.".format(entry_id))

	url = "https://eksisozluk.com/entry/" + entry_id
	return common.__fetch_entry(url)

def get_sukela():
	url = "https://eksisozluk.com"
	return common.__fetch_entry(url)

def get_debe():
	topic_list = []
	topic_soup = common.get_topic_soup("https://eksisozluk.com/debe", "ol")

	for t in topic_soup.find_all('li'):
		entry = {}
		entry["creator"] = t.find('div', attrs={'class':'detail'}).get_text()
		entry["title"] = t.find('span', attrs={'class':'caption'}).get_text()
		href = t.find("a")["href"]
		match = re.search(r"23([0-9]+)$", href)
		entry["id"] = match.groups(1)[0]

		topic_list.append(entry)

	return topic_list

def get_gundem():
	topic_list = []
	topic_soup = common.get_topic_soup("https://eksisozluk.com/basliklar/populer", "ul")

	for t in topic_soup.find_all('li'):
		topic = {}
		topic["url"] = t.find("a")["href"]
		smalls = t.find_all("small")
		[small.extract() for small in smalls]
		topic["title"] = t.find("a").get_text().strip()

		topic_list.append(topic)

	return topic_list

def search(q):
	#TODO: accept a full-fledged "hayvan ara" object and pass that in the URL
	#https://eksisozluk.com/basliklar/ara?searchForm.Keywords=yazar+nick%27lerinin+%C3%B6b%C3%BCr+d%C3%BCnya+versiyonlar%C4%B1&searchForm.Author=&searchForm.When.From=&searchForm.When.To=&searchForm.NiceOnly=false&searchForm.SortOrder=Date
	q = common.__transliterate(q)
	topic_list = []
	url = "https://eksisozluk.com/basliklar/ara?searchForm.Keywords=" + q + "&searchForm.Author=&searchForm.When.From=&searchForm.When.To=&searchForm.NiceOnly=false&searchForm.SortOrder=Date"

	topic_soup = common.get_topic_soup(url, "ul")

	for e in topic_soup.find_all('li'):
		topic_list.append(e.find("a")["href"])

	return topic_list
