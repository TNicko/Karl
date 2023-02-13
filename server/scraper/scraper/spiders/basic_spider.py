import scrapy
from scraper.items import SessionItem, WebsitePageItem
import os
import re
# from selenium import webdriver

# Xpath for the search items on Google
SEARCH_ITEM_XPATH = "//div[@class='egMi0 kCrYT']/a"

class BasicSpider(scrapy.Spider):
    name = 'google_search'
    
    def __init__(self, *args, **kwargs):
        print(kwargs)
        self.url = kwargs.get('url')
        self.domain = kwargs.get('domain')
        self.start_urls = [self.url] if self.url else self.start_urls
        self.allowed_domains = [self.domain] if self.domain else self.allowed_domains
        self.task_id = kwargs.get('_job')

    def get_google_url(self, response_url):
        match = re.search(r'q=(.*?)&sa', response_url)
        return match.group(1)

    def get_urls(self, response, num_items=1):
        urls = []
        for item in response.xpath(SEARCH_ITEM_XPATH):
            if len(urls) >= num_items:
                break
            url = self.get_google_url(item.xpath('@href').extract()[0])
            urls.append(url)
        return urls
    

    def parse(self, response):
        urls = self.get_urls(response=response, num_items=2)
        print('URLS = ', urls)
        session_item = SessionItem()
        session_item['task_id'] = self.task_id
        # item['title'] = next(iter(filter(bool,[e.strip() for e in response.xpath('//title//text()').extract()])),'No Title')
        session_item['search_url'] = self.url
        session_item['content'] = urls

            
        yield {'session_item': session_item}

        for result in urls:
            self.allowed_domains.append(result)
            item = WebsitePageItem()
            item['url'] = result
            yield scrapy.Request(result, callback=self.parse_result, dont_filter=True, cb_kwargs={'item': item})

        # result_dict = {'items': items, 'session_item': session_item}

        # return result_dict

    def parse_result(self, response, item):
        item['content'] = response.text
        yield {'webpage_item': item, 'task_id': self.task_id}

