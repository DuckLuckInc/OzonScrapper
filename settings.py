# -*- coding: utf-8 -*-

# Scrapy settings for jobparser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'OzonScrapper'

SPIDER_MODULES = ['OzonScrapper.spiders']
NEWSPIDER_MODULE = 'OzonScrapper.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

LOG_ENABLED = True
LOG_LEVEL = 'DEBUG' # DEBUG INFO ERROR
# LOG_FILE = 'logs.txt'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.75
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'OzonScrapper.middlewares.OzonScrapperSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'OzonScrapper.middlewares.OzonScrapperDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'OzonScrapper.pipelines.OzonPipeline': 30,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Max items from category
MAX_ITEMS = 5

# Ozon categories
CATEGORIES = [
   {'deeplink': '',
     'id': 15500,
     'image': 'https://cdn1.ozone.ru/s3/cms/02/t58/1-3x.png',
     'sliceTrackingInfo': {'id': '15500',
                           'index': 1,
                           'title': 'Электроника',
                           'type': 'category'},
     'title': 'Электроника',
     'url': '/category/elektronika-15500/'},
    {'deeplink': '',
     'id': 7500,
     'image': 'https://cdn1.ozone.ru/graphics/cms/odezhda_new.png',
     'sliceTrackingInfo': {'id': '7500',
                           'index': 2,
                           'title': 'Одежда',
                           'type': 'category'},
     'title': 'Одежда',
     'url': '/category/odezhda-obuv-i-aksessuary-7500/'},
    {'deeplink': '',
     'id': 17777,
     'image': 'https://cdn1.ozone.ru/graphics/cms/obuv_new.png',
     'sliceTrackingInfo': {'id': '17777',
                           'index': 3,
                           'title': 'Обувь',
                           'type': 'category'},
     'title': 'Обувь',
     'url': '/category/obuv-17777/'},
    {'deeplink': '',
     'id': 14500,
     'image': 'https://cdn1.ozone.ru/graphics/main-category-logos/HD.png',
     'sliceTrackingInfo': {'id': '14500',
                           'index': 4,
                           'title': 'Дом и сад',
                           'type': 'category'},
     'title': 'Дом и сад',
     'url': '/category/dom-i-sad-14500/'},
    {'deeplink': '',
     'id': 7000,
     'image': 'https://cdn1.ozone.ru/graphics/categories_icons/7000.png',
     'sliceTrackingInfo': {'id': '7000',
                           'index': 5,
                           'title': 'Детские товары',
                           'type': 'category'},
     'title': 'Детские товары',
     'url': '/category/detskie-tovary-7000/'},
    {'deeplink': '',
     'id': 6500,
     'image': 'https://cdn1.ozone.ru/s3/cms/46/tc7/beauty1.png',
     'sliceTrackingInfo': {'id': '6500',
                           'index': 6,
                           'title': 'Красота и здоровье',
                           'type': 'category'},
     'title': 'Красота и здоровье',
     'url': '/category/krasota-i-zdorove-6500/'},
    {'deeplink': '',
     'id': 10500,
     'image': 'https://cdn1.ozone.ru/graphics/cms/bt1.png',
     'sliceTrackingInfo': {'id': '10500',
                           'index': 7,
                           'title': 'Бытовая техника',
                           'type': 'category'},
     'title': 'Бытовая техника',
     'url': '/category/bytovaya-tehnika-10500/'},
    {'deeplink': '',
     'id': 11000,
     'image': 'https://cdn1.ozone.ru/graphics/cms/sport1.png',
     'sliceTrackingInfo': {'id': '11000',
                           'index': 8,
                           'title': 'Спорт и отдых',
                           'type': 'category'},
     'title': 'Спорт и отдых',
     'url': '/category/sport-i-otdyh-11000/'},
    {'deeplink': '',
     'id': 9700,
     'image': 'https://cdn1.ozone.ru/graphics/main-category-logos/constructions_and_repair.png',
     'sliceTrackingInfo': {'id': '9700',
                           'index': 9,
                           'title': 'Строительство и ремонт',
                           'type': 'category'},
     'title': 'Строительство и ремонт',
     'url': '/category/stroitelstvo-i-remont-9700/'},
    {'deeplink': '',
     'id': 9200,
     'image': 'https://cdn1.ozone.ru/s3/cms/e4/t8c/image3x.jpg',
     'sliceTrackingInfo': {'id': '9200',
                           'index': 10,
                           'title': 'Продукты питания',
                           'type': 'category'},
     'title': 'Продукты питания',
     'url': '/category/produkty-pitaniya-9200/'},
    {'deeplink': '',
     'id': 6000,
     'image': 'https://cdn1.ozone.ru/s3/cms/c0/tfc/pharmacy1.png',
     'sliceTrackingInfo': {'id': '6000',
                           'index': 11,
                           'title': 'Аптека',
                           'type': 'category'},
     'title': 'Аптека',
     'url': '/category/apteka-6000/'},
    {'deeplink': '',
     'id': 12300,
     'image': 'https://cdn1.ozone.ru/s3/cms/e9/tcd/image3x.png',
     'sliceTrackingInfo': {'id': '12300',
                           'index': 12,
                           'title': 'Товары для животных',
                           'type': 'category'},
     'title': 'Товары для животных',
     'url': '/category/tovary-dlya-zhivotnyh-12300/'},
    {'deeplink': '',
     'id': 16500,
     'image': 'https://cdn1.ozone.ru/graphics/main-category-logos/books.png',
     'sliceTrackingInfo': {'id': '16500',
                           'index': 13,
                           'title': 'Книги',
                           'type': 'category'},
     'title': 'Книги',
     'url': '/category/knigi-16500/'},
    {'deeplink': '',
     'id': 33332,
     'image': 'https://cdn1.ozone.ru/graphics/cms/tourism1.png',
     'sliceTrackingInfo': {'id': '33332',
                           'index': 14,
                           'title': 'Туризм, рыбалка, охота',
                           'type': 'category'},
     'title': 'Туризм, рыбалка, охота',
     'url': '/category/ohota-rybalka-turizm-33332/'},
    {'deeplink': '',
     'id': 8500,
     'image': 'https://cdn1.ozone.ru/graphics/main-category-logos/autogoods.png',
     'sliceTrackingInfo': {'id': '8500',
                           'index': 15,
                           'title': 'Автотовары',
                           'type': 'category'},
     'title': 'Автотовары',
     'url': '/category/avtotovary-8500/'},
    {'deeplink': '',
     'id': 15000,
     'image': 'https://cdn1.ozone.ru/graphics/main-category-logos/furniture.png',
     'sliceTrackingInfo': {'id': '15000',
                           'index': 16,
                           'title': 'Мебель',
                           'type': 'category'},
     'title': 'Мебель',
     'url': '/category/mebel-15000/'},
    {'deeplink': '',
     'id': 13500,
     'image': 'https://cdn1.ozone.ru/s3/cms/4a/tcb/image3x.png',
     'sliceTrackingInfo': {'id': '13500',
                           'index': 17,
                           'title': 'Хобби и творчество',
                           'type': 'category'},
     'title': 'Хобби и творчество',
     'url': '/category/hobbi-i-tvorchestvo-13500/'},
    {'deeplink': '',
     'id': 50001,
     'image': 'https://cdn1.ozone.ru/s3/cms/e7/t66/jewelry1.png',
     'sliceTrackingInfo': {'id': '50001',
                           'index': 18,
                           'title': 'Ювелирные украшения',
                           'type': 'category'},
     'title': 'Ювелирные украшения',
     'url': '/category/yuvelirnye-ukrasheniya-50001/'},
    {'deeplink': '',
     'id': 7697,
     'image': 'https://cdn1.ozone.ru/graphics/cms/aksy_new.png',
     'sliceTrackingInfo': {'id': '7697',
                           'index': 19,
                           'title': 'Аксессуары',
                           'type': 'category'},
     'title': 'Аксессуары',
     'url': '/category/aksessuary-7697/'},
    {'deeplink': '',
     'id': 13300,
     'image': 'https://cdn1.ozone.ru/graphics/cms/games1.png',
     'sliceTrackingInfo': {'id': '13300',
                           'index': 20,
                           'title': 'Игры и консоли',
                           'type': 'category'},
     'title': 'Игры и консоли',
     'url': '/category/igry-i-soft-13300/'},
    {'deeplink': '',
     'id': 18000,
     'image': 'https://cdn1.ozone.ru/s3/cms/81/t18/image3x.png',
     'sliceTrackingInfo': {'id': '18000',
                           'index': 21,
                           'title': 'Канцелярские товары',
                           'type': 'category'},
     'title': 'Канцелярские товары',
     'url': '/category/kantselyarskie-tovary-18000/'},
    {'deeplink': '',
     'id': 9000,
     'image': 'https://cdn1.ozone.ru/s3/cms/89/tda/adult.png',
     'isAdult': True,
     'sliceTrackingInfo': {'id': '9000',
                           'index': 22,
                           'title': 'Товары для взрослых',
                           'type': 'category'},
     'title': 'Товары для взрослых',
     'url': '/category/tovary-dlya-vzroslyh-9000/'},
    {'deeplink': '',
     'id': 8000,
     'image': 'https://cdn1.ozone.ru/graphics/main-category-logos/vintage.png',
     'sliceTrackingInfo': {'id': '8000',
                           'index': 23,
                           'title': 'Антиквариат и коллекционирование',
                           'type': 'category'},
     'title': 'Антиквариат и коллекционирование',
     'url': '/category/antikvariat-vintazh-iskusstvo-8000/'},
    {'deeplink': '',
     'id': 32056,
     'image': 'https://cdn1.ozone.ru/graphics/ozon/digital/1@2x.png',
     'sliceTrackingInfo': {'id': '32056',
                           'index': 24,
                           'title': 'Цифровые товары',
                           'type': 'category'},
     'title': 'Цифровые товары',
     'url': '/category/tsifrovye-tovary-32056/'},
    {'deeplink': '',
     'id': 14572,
     'image': 'https://cdn1.ozone.ru/graphics/main-category-logos/bh.png',
     'sliceTrackingInfo': {'id': '14572',
                           'index': 25,
                           'title': 'Бытовая химия и гигиена',
                           'type': 'category'},
     'title': 'Бытовая химия и гигиена',
     'url': '/category/bytovaya-himiya-14572/'},
    {'deeplink': '',
     'id': 25000,
     'image': 'https://cdn1.ozone.ru/s3/cms/2c/te7/icon_m_-_express_tabbar_-_active3x.png',
     'sliceTrackingInfo': {'id': '25000',
                           'index': 26,
                           'title': 'Ozon Express',
                           'type': 'category'},
     'title': 'Ozon Express',
     'url': '/category/supermarket-25000/'},
    {'deeplink': '',
     'id': 13100,
     'image': 'https://cdn1.ozone.ru/s3/cms/12/t16/music-cinema.png',
     'sliceTrackingInfo': {'id': '13100',
                           'index': 27,
                           'title': 'Музыка и видео',
                           'type': 'category'},
     'title': 'Музыка и видео',
     'url': '/category/muzyka-i-video-13100/'},
    {'deeplink': '',
     'id': 34452,
     'image': 'https://cdn1.ozone.ru/s3/cms/1e/t4b/automoto.png',
     'sliceTrackingInfo': {'id': '34452',
                           'index': 28,
                           'title': 'Автомобили и мототехника',
                           'type': 'category'},
     'title': 'Автомобили и мототехника',
     'url': '/category/avtomobili-i-mototsikly-34452/'},
    {'deeplink': '',
     'id': 21000,
     'image': 'https://cdn1.ozone.ru/s3/cms/ab/t1f/168x168-icon.png',
     'sliceTrackingInfo': {'id': '21000',
                           'index': 29,
                           'title': 'Ozon Услуги',
                           'type': 'category'},
     'title': 'Ozon Услуги',
     'url': '/category/uslugi-21000/'},
    {'deeplink': '',
     'id': 35659,
     'image': 'https://cdn1.ozone.ru/s3/cms/e3/tfc/sigi_icon.png',
     'isAdult': True,
     'sliceTrackingInfo': {'id': '35659',
                           'index': 30,
                           'title': 'Электронные сигареты и товары для курения',
                           'type': 'category'},
     'title': 'Электронные сигареты и товары для курения',
     'url': '/category/elektronnye-sigarety-i-tovary-dlya-kureniya-35659/'}
]