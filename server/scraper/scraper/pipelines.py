# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from api.models import Session, WebsitePage

class ScraperPipeline(object):
    def process_item(self, item, spider):

        print("PIPELINING......................")
        if 'session_item' in item:
            session_item = item['session_item']
            session, created = Session.objects.update_or_create(
                task_id=session_item['task_id'],
                defaults=session_item
            )
            return session_item

        if 'webpage_item' in item:
            session = Session.objects.get(task_id=item['task_id'])

            webpage_item = item['webpage_item']
            
            # Process webpage html content
            # ----------------------------

            
            # ----------------------------

            # Save webpage to database
            WebsitePage.objects.update_or_create(
                url=webpage_item['url'],
                defaults={
                    **webpage_item,
                    'session': session
                }
            )

            return webpage_item
