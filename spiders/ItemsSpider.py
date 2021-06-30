import json
import scrapy
from scrapy.http import HtmlResponse
from items import OzonItem
from settings import CATEGORIES, MAX_ITEMS


class OzonSpider(scrapy.Spider):
    name = 'OzonSpider'
    site_name = 'ozon.ru'
    allowed_domains = ['ozon.ru']
    main_url = 'https://www.ozon.ru/api/composer-api.bx/page/json/v2?'
    page = 1
    categories = [category['url'] + '?' for category in CATEGORIES]
    category_index = 0
    category = categories[category_index]
    start_urls = [main_url + f'url={category.replace("/", "%2F").replace("?", "%3F")}page%3D1']
    current_items_from_category = 0
    status = ''

    def parse(self, response: HtmlResponse):
        if self.status != 'end':
            self.page += 1
            url = f'url={self.category.replace("/", "%2F").replace("?", "%3F")}page%3D{self.page}'
            yield response.follow(self.main_url + url, callback=self.parse)

            data = response.json()
            pages_info = json.loads(data['shared'])['catalog']
            if pages_info['currentPage'] > pages_info['totalPages'] or self.current_items_from_category >= MAX_ITEMS:
                self.status = self.change_category()
                yield

            try:
                items = json.loads(data['widgetStates']['searchResultsV2-252189-default-1'])['items']
                if self.current_items_from_category + len(items) > MAX_ITEMS:
                    items = items[:MAX_ITEMS - self.current_items_from_category]

                for item in items:
                    link = item['link']
                    url = f'url={link.replace("/", "%2F").replace("?", "%3F")}'
                    self.current_items_from_category += 1
                    yield response.follow(self.main_url + url, callback=self.item_parse)
            except:
                pass

    def get_web_keys(self, keys):
        return {
            'brand': [key for key in keys if key.startswith('webBrand')][0],
            'characteristics': [key for key in keys if key.startswith('webCharacteristics')][0],
            'images': [key for key in keys if key.startswith('webGallery')][0],
            'price': [key for key in keys if key.startswith('webPrice')][0],
            'reviews_count': [key for key in keys if key.startswith('webReviewProductScore')][0],
        }

    def item_parse(self, response):
        data = response.json()
        try:
            keys = self.get_web_keys(data['widgetStates'].keys())
            description = json.loads(data['seo']['script'][0]['innerHTML'])
            brand = json.loads(data['widgetStates'][keys['brand']])
            characteristics = json.loads(data['widgetStates'][keys['characteristics']])['characteristics'][0]
            images = json.loads(data['widgetStates'][keys['images']])
            price = json.loads(data['widgetStates'][keys['price']])
            categories = json.loads(data['layoutTrackingInfo'])
            categories_string = categories['hierarchy']
            categories_string = categories_string[:categories_string.find('/')]
            yield OzonItem(
                description=description,
                brand=brand,
                characteristics=characteristics,
                images=images,
                price=price,
                categories=categories,
                collection=categories_string
            )
        except:
            pass

    def change_category(self):
        self.category_index += 1
        if self.category_index >= len(self.categories):
            return 'end'
        self.category = self.categories[self.category_index]
        if 'isAdult' in CATEGORIES[self.category_index].keys():
            self.change_category()
        self.page = 1
        self.current_items_from_category = 0
        return ''
