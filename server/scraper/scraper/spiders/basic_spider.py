import scrapy
from scraper.items import ScraperItem

class BasicSpider(scrapy.Spider):
    name = 'basic'
    
    def __init__(self, *args, **kwargs):
        self.url = kwargs.get('url')
        self.domain = kwargs.get('domain')
        self.start_urls = [self.url] if self.url else self.start_urls
        self.allowed_domains = [self.domain] if self.domain else self.allowed_domains

    def parse(self, response):
        yield response.text
