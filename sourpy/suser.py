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

import logging

log = logging.getLogger(__name__)

import common

class Suser:
	def __init__(self, user_id):
		self.user_id = user_id
		self.__check_user_validity()

	def __check_user_validity(self):
		url = "https://eksisozluk.com/biri/" + self.user_id
		log.debug("Checking user validity: {}.".format(self.user_id))
		try:
			page = urllib2.urlopen(url).read()
		except Exception as e:
			log.error(e)
			raise common.SourPyException("Invalid user ID: {}".format(self.user_id))

	def __get_entry_list_from_url(self, url):
		topic_soup = common.get_topic_soup(url, "ul")
		if topic_soup:
			return self.__get_entry_list_from_topic_soup(topic_soup)
		else:
			log.debug("Topic list is empty...")
			return None

	def __get_entry_list_from_topic_soup(self, topic_soup):
		entry_list = []

		for t in topic_soup.find_all('li'):
			entry = {}
			entry["id"] = t.find("span").get_text().strip("#")
			spans = t.find_all("span")
			[span.extract() for span in spans]
			entry["title"] = t.a.get_text()
			entry["creator"] = self.user_id
			entry_list.append(entry)

		return entry_list

	def get_most_recent_entries(self):
		# son entry'leri
		url = "https://eksisozluk.com/basliklar/istatistik/" + self.user_id + "/son-entryleri"
		log.debug("Most recent etries of {} scrapped from {}".format(self.user_id, url))

		return self.__get_entry_list_from_url(url)

	def get_top_entries(self):
		# en beğenilenleri
		url = "https://eksisozluk.com/basliklar/istatistik/" + self.user_id + "/en-begenilenleri"
		log.debug("Suser top entries URL: {}".format(url))

		return self.__get_entry_list_from_url(url)

	def get_most_favorited_entries(self):
		# en çok favorilenen entry'leri
		url = "https://eksisozluk.com/basliklar/istatistik/" + self.user_id + "/favorilenen-entryleri"
		log.debug("Suser most favorited entries URL: {}".format(url))

		return self.__get_entry_list_from_url(url)

	def get_latest_rated_entries(self):
		# son oylananları
		url = "https://eksisozluk.com/basliklar/istatistik/" + self.user_id + "/son-oylananlari"
		log.debug("Suser latest rated entries URL: {}".format(url))

		return self.__get_entry_list_from_url(url)

	def get_entries_rated_this_week(self):
		# bu hafta dikkat çekenleri
		url = "https://eksisozluk.com/basliklar/istatistik/" + self.user_id + "/bu-hafta-dikkat-cekenleri"
		log.debug("Suser entries rated this week URL: {}".format(url))

		return self.__get_entry_list_from_url(url)

	# Not to be confused with get_most_favorited_entries
	def get_favorite_entries(self):
		# favori entry'leri
		url = "https://eksisozluk.com/basliklar/istatistik/" + self.user_id + "/favori-entryleri"
		log.debug("Suser favorite entries URL: {}".format(url))

		return self.__get_entry_list_from_url(url)
