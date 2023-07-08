import scrapy


class QuranScraperSpider(scrapy.Spider):
    name = "quran_scraper"
    allowed_domains = ["qurancentral.com"]
    start_urls = ["https://qurancentral.com/fr/"]
    def parse(self, response):       
        pass
