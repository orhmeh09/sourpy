SourPy
=======================================================

SourPy is a scraper for Ekşi Sözlük, the popular Turkish social media
site.

Warning
-------------------------------------------------------
This project is not mature enough and requires a lot of testing. Use it
at your own risk.

Installation
-------------------------------------------------------

::

  pip install sourpy


Documentation
-------------------------------------------------------
In progress.

Usage
-------------------------------------------------------

User statistics can be gathered as follows:

::

	import sourpy
	import pprint

	user = sourpy.suser.Suser("ssg")

	# son entry'leri
	pprint.pprint(user.get_most_recent_entries())

	# en beğenilenleri
	pprint.pprint(user.get_top_entries())

	# en çok favorilenen entry'leri
	pprint.pprint(user.get_most_favorited_entries())

	# bu hafta dikkat çekenleri
	pprint.pprint(user.get_entries_rated_this_week())

	#favori entry'leri
	pprint.pprint(user.get_favorite_entries())

Ekşi Sözlük interface can be used as follows:

::

	import sourpy
	import pprint

	debe = sourpy.get_debe()
	pprint.pprint(debe)

	gundem = sourpy.get_gundem()
	pprint.pprint(gundem)

	pena = sourpy.get_entry("1")
	pprint.pprint(pena)

	sukela = sourpy.get_sukela()
	pprint.pprint(sukela)


License
-------------------------------------------------------
Copyright (c) 2014 Eren Inan Canpolat

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
