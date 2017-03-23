#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Evgeny Orlov'
SITENAME = 'eorlov'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Moscow'
DEFAULT_LANG = 'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
ARTICLE_LANG_URL = 'posts/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['extras', 'images']
EXTRA_PATH_METADATA = {
    'extras/CNAME': {'path': 'CNAME'},
    'extras/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'extras/android-chrome-256x256.png': {'path': 'android-chrome-256x256.png'},
    'extras/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extras/browserconfig.xml': {'path': 'browserconfig.xml'},
    'extras/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extras/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/manifest.json': {'path': 'manifest.json'},
    'extras/mstile-150x150.png': {'path': 'mstile-150x150.png'},
}

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-bootstrapify']

THEME = 'themes/pelican-alchemy/alchemy'

SITESUBTITLE = 'A magical \u2728 Pelican theme'

SITEIMAGE = '/images/logo.png width=200 height=200'

DESCRIPTION = (
    'A functional, clean, responsive theme for Pelican. Heavily ' +
    'inspired by crowsfoot and clean-blog, powered by Bootstrap.'
)

PYGMENTS_STYLE = 'monokai'  # zenburn monokai manni

HIDE_AUTHORS = True


RFG_FAVICONS = True

# Blogroll
LINKS = (
    ('kaggle', 'https://www.kaggle.com/eorlov'),
)

ICONS = (
    ('github', 'https://github.com/evgenyorlov'),
    ('get-pocket', 'https://getpocket.com/@evgeny_orlov'),
    ('slack', 'https://opendatascience.slack.com/messages/@evgenyorlov/'),
    ('telegram', 'https://t.me/eugeneorlov'),
)

DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'archives', 'sitemap']
SITEMAP_SAVE_AS = 'sitemap.xml'
