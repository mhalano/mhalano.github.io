#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Marcos Alano'
SITENAME = "Trust Me, I'm a Linux Engineer!"
#SITEURL = 'http://mhalano.github.io'

# Nada de temas usando Bootstrap
THEME='pelican-themes/pelican-bootstrap3'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Logo esse submódulo será descontinuado e a instalação dos plugins será feita com o pip3
PLUGIN_PATHS = ['pelican-plugins']


PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

STATIC_PATHS = [
    'images',
    'static/robots.txt',
    'static/security.txt'
]

EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'static/security.txt': {'path': 'security.txt'}
}

# Descrição dos plugins
# - global_license - Cria a opção LICENSE que pode ser usada dentro do tema.
PLUGINS = ['permalinks','i18n_subsites','sitemap','pdf','minchin.pelican.plugins.nojekyll']


# Precisa iniciar o dicionário vazio antes de setar a chave-valor
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    }
}

ABOUT_ME = "Working with IT since 2004"
#AVATAR = "https://0.gravatar.com/avatar/42d18016aae2b40cc761f58eda8b3e17?s=180"
AVATAR = "images/photo.jpg"

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en_us'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_ATOM = 'feeds/{slug}.atom.xml'
AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml'
RSS_FEED_SUMMARY_ONLY = False


# If your site is available via HTTPS, make sure SITEURL begins with https://
RELATIVE_URLS = False


DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""




# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/mhalano'),
          ('Twitter', 'https://twitter.com/mhalano1'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
