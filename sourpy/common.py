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
import logging

log = logging.getLogger(__name__)

class SourPyException(Exception):
	def __init__(self, msg):
		self.msg = msg
		log.error(self.__str__())

	def __str__(self):
		return ("SourPyException:: {}".format(self.msg))

def get_topic_soup(url, list_tag):
	try:
		page = urllib2.urlopen(url).read()
	except Exception as e:
		log.error(e)
		raise SourPyException("Invalid URL: {}".format(url))

	soup = BeautifulSoup(page)
	topic_soup = soup.find('section', attrs={'id':'content-body'}).find(list_tag, attrs={'class':'topic-list'})

	return topic_soup

def __get_entry_dict_from_entry_soup(entry_soup):
	entry = {}
	entry["commentText"] = entry_soup.find("div", attrs={"class":"content", "itemprop":"commentText"}).get_text()
	entry["creator"] = entry_soup.footer["data-author"]
	entry["id"] = entry_soup.footer["data-id"]
	info = entry_soup.footer.find('div', attrs={'class':'info'})
	entry["creation-time"] = info.find('time', attrs={'class':'creation-time'})["datetime"]
	try:
		entry["last-update-time"] = info.find('time', attrs={'class':'last-update-time'})["datetime"]
	except:
		#Entry not modified
		entry["last-update-time"] = entry["creation-time"]
	entry["creator-url"] = info.find('address', attrs={'itemprop':'creator'}).a["href"]
	log.debug(entry)
	return entry

def __transliterate(txt):
	txt = txt.strip()
	txt = txt.lower()

	txt = txt.replace("ş", "s")
	txt = txt.replace("ğ", "g")
	txt = txt.replace("ı", "i")
	txt = txt.replace("ü", "u")
	txt = txt.replace("ö", "o")
	txt = txt.replace("ç", "c")

	txt = re.sub(r'[\s]+','+', txt)
	txt = re.sub(r'[^a-zA-Z0-9\+]','', txt)

	return txt

def __fetch_entry(url):
	log.debug("Entry URL: {}".format(url))

	try:
		page = urllib2.urlopen(url).read()
	except Exception as e:
		log.error(e)
		raise e

	soup = BeautifulSoup(page)
	entry_soup = soup.find('ol', attrs={'id':'entry-list'}).find('li').article

	entry = __get_entry_dict_from_entry_soup(entry_soup)
	entry["title"] = soup.find('h1', attrs={'id':'title'})["data-title"]
	return entry
