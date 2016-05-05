#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'kmol'
SITENAME = 'CDW11 網頁 (虎尾科大MDE)'
SITEURL = 'http://cdw11-ag100.rhcloud.com/static/'

# 不要用文章所在目錄作為類別
USE_FOLDER_AS_CATEGORY = False

#PATH = 'content'

#OUTPUT_PATH = 'output'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('pelican-bootstrap3', 'https://github.com/DandyDev/pelican-bootstrap3/'),
         ('pelican-plugins', 'https://github.com/getpelican/pelican-plugins'),
         ('Tipue search', 'https://github.com/Tipue/Tipue-Search'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# 必須絕對目錄或相對於設定檔案所在目錄
PLUGIN_PATHS = ['plugin']
PLUGINS = ['liquid_tags.notebook', 'summary', 'tipue_search', 'sitemap', 'render_math']

# for sitemap plugin
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# search is for Tipue search
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'authors', 'archives', 'search'))

# for pelican-bootstrap3 theme settings
#TAG_CLOUD_MAX_ITEMS = 50
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
TAGS_URL = "tags.html"
CATEGORIES_URL = "categories.html"
#SHOW_ARTICLE_AUTHOR = True

#MENUITEMS = [('Home', '/'), ('Archives', '/archives.html'), ('Search', '/search.html')]
# 希望將部份常用的 Javascript 最新版程式庫放到這裡, 可以透過 http://cadlab.mde.tw/post/js/ 呼叫
STATIC_PATHS = ['js']