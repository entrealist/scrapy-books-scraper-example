# -*- coding: utf-8 -*-

BOT_NAME = 'books'

SPIDER_MODULES = ['books_toscrape_com.spiders']
NEWSPIDER_MODULE = 'books_toscrape_com.spiders'

ROBOTSTXT_OBEY = True
HTTPCACHE_ENABLED = True

FEED_EXPORT_ENCODING: 'utf-8'
