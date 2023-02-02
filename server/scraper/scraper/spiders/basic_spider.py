import scrapy
from scraper.items import SessionItem
import os

class BasicSpider(scrapy.Spider):
    name = 'google_search'
    
    def __init__(self, *args, **kwargs):
        self.url = kwargs.get('url')
        self.domain = kwargs.get('domain')
        self.start_urls = [self.url] if self.url else self.start_urls
        self.allowed_domains = [self.domain] if self.domain else self.allowed_domains
        self.task_id = os.environ['SCRAPY_JOB']

    def parse(self, response):
        item = SessionItem()
        item['task_id'] = self.task_id
        # item['title'] = next(iter(filter(bool,[e.strip() for e in response.xpath('//title//text()').extract()])),'No Title')
        item['search_url'] = self.url
        item['content'] = response.text
        return item

