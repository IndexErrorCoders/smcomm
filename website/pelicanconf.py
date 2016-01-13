#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'EachOfUs'
SITENAME = "Sam & Max Board"
SITESUBTITLE = "Suivez l'actu de la communauté"

SITEURL = 'http://smcomm.trigger-happy.eu'
TIMEZONE = 'Europe/Paris'

THEME = 'pelican-octopress-theme'
DEFAULT_LANG = 'fr'

USE_FOLDER_AS_CATEGORY = True

PATH = 'content'

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
SOCIAL = (('GitHub @IndexErrorCoders', 'https://github.com/IndexErrorCoders'),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

FEEDS_USER_AGENT = 'SMBoard/1.0'
FEEDS_FOLDER = PATH + "/news/"


GITHUB_URL = 'https://github.com/IndexErrorCoders/smcomm'

# utilisé avec le theme notmyidea
TWITTER_WIDGET_ACCOUNT = 'sam_et_max'
TWITTER_WIDGET = '669292804124839936'

DEFAULT_PAGINATION = 15

PLUGIN_PATHS = ['../pelican-plugins/']
PLUGINS = ['pelican-toc', 'related_posts', 'neighbors', 'github_activity' ]


TOC = {
    'TOC_HEADERS' : '^h[1-4]',  # What headers should be included in the generated toc
                                # Expected format is a regular expression
    'TOC_RUN'     : 'true'      # Default value for toc generation, if it does not evaluate
                                # to 'true' no toc will be generated
}


# avec le theme OCTOPRESS on peut utiliser ceci :

SEARCH_BOX = True
TWITTER_USER = 'sam_et_max'
TWITTER_WIDGET_ID = '669292804124839936'
TWITTER_TWEET_COUNT = 3



FEED_DOMAIN = 'http://smcomm.trigger-happy.eu'
FEED_ATOM = 'main.atom.xml'
FEED_RSS = 'main.rss.xml'

# https://github.com/getpelican/pelican-plugins/tree/master/github_activity
GITHUB_ACTIVITY_FEED = 'https://github.com/IndexErrorCoders.atom'
GITHUB_ACTIVITY_MAX_ENTRIES = 10



RELATED_POSTS_MAX = 5
