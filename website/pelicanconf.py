#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'EachOfUs'
SITENAME = "Sam & Max Board"
SITESUBTITLE = "Toute l'actu de la communauté"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Sam&Max', 'http://sametmax.com/'),
         ('Planete Sam&Max', 'http://sametmax.com/planet-python-fr/'),
         ('IndexError', 'http://indexerror.net/'),
         ('Reddit', 'http://reddit.com/r/sametmax/'),
        )

# Social widget
SOCIAL = (('@sametmax', 'https://twitter.com/sam_et_max'),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

FEEDS_USER_AGENT = 'SMBoard/1.0'
FEEDS_FOLDER = PATH + "/news/"
