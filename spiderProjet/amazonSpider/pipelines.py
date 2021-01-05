# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from amazonSpider.items import AmazonspiderItem
from scrapy.exporters import JsonItemExporter

class AmazonspiderPipeline:

    def __init__(self):
        self.file = open('produits_exporter.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()


    def process_item(self, item, spider):
        item['classement'] = self.clean_string(item['classement'])
        item['produit'] = self.clean_string(item['produit'])
        item['evaluations'] = self.clean_string(item['evaluations'])
        if item['prix'] != None:
            item['prix'] = self.clean_string(item['prix'])
        self.exporter.export_item(item)
        return item

    def clean_string(self,string):
        return string.replace('\n','').replace('\xa0','').strip()

