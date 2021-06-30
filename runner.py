from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from OzonScrapper import settings
from OzonScrapper.spiders.ItemsSpider import OzonSpider


if __name__ == '__main__':
    crawlerSettings = Settings()
    crawlerSettings.setmodule(settings)
    process = CrawlerProcess(settings=crawlerSettings)
    process.crawl(OzonSpider)
    process.start()

