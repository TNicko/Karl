# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from api.models import Session

class ScraperPipeline(object):
    def process_item(self, item, spider):
        Session.objects.update_or_create(
            task_id=item['task_id'],
            defaults=item
        )

        return item
