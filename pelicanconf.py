#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#THEME='pelican-themes/pelican-bootstrap3'
#JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
#agora acho que os plugins são instalados com pip3
#PLUGIN_PATHS = ['pelican-plugins']

# Descrição dos plugins
# - global_license - Cria a opção LICENSE que pode ser usada dentro do tema.
#PLUGINS = ['permalinks','i18n_subsites','sitemap','pdf','minchin.pelican.plugins.nojekyll']

AUTHOR = 'Marcos Alano'
SITENAME = "Trust me! I'm a (DevOps) Engineer!"
#SITEURL = "https://mhalano.io"
SITEURL = ""
PATH = "content"

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en_US'

# Feed generation is usually not desired when developing
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'


FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_ATOM = 'feeds/{slug}.atom.xml'
AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml'
RSS_FEED_SUMMARY_ONLY = False




STATIC_PATHS = [
    'images',
    'static/CNAME',
    'static/robots.txt',
    'static/security.txt',
]

EXTRA_PATH_METADATA = {
    'static/CNAME': {'path': 'CNAME'},
    'static/robots.txt': {'path': 'robots.txt'},
    'static/security.txt': {'path': 'security.txt'},
}

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
#SOCIAL = (
#    ("You can add links in your config file", "#"),
#    ("Another social link", "#"),
#)

SOCIAL = (('GitHub', 'https://github.com/mhalano'),
          ('Instagram', 'https://instagram.com/marcoshalano'),)



DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}



#AVATAR = "https://0.gravatar.com/avatar/42d18016aae2b40cc761f58eda8b3e17?s=180"
AVATAR = "images/photo.jpg"



#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
