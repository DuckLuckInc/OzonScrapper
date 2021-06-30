from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
import settings
from spiders.ItemsSpider import OzonSpider


if __name__ == '__main__':
    crawlerSettings = Settings()
    crawlerSettings.setmodule(settings)
    process = CrawlerProcess(settings=crawlerSettings)
    process.crawl(OzonSpider)
    process.start()

