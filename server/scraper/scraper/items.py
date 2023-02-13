# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from api.models import Session, WebsitePage

class SessionItem(DjangoItem):
    django_model = Session

class WebsitePageItem(DjangoItem):
    django_model = WebsitePage

