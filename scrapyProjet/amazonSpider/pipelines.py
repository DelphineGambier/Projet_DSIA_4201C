# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from amazonSpider.items import AmazonspiderItem
from scrapy.exporters import JsonItemExporter
from urllib import request
import os

class AmazonspiderPipeline:

    def __init__(self):
        self.file = open('json/produits_exporter.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()


    def process_item(self, item, spider):
        item['classement'] = self.clean_string(item['classement'])
        item['produit'] = self.clean_string(item['produit'])
        if item['evaluations'] != None:
            item['evaluations'] = self.clean_string(item['evaluations'])
        if item['prix'] != None:
            item['prix'] = self.clean_string(item['prix'])
        if spider.name == 'amazon':
            self.exporter.export_item(item)
            request.urlretrieve(item['img_url'], 'img/all/'+item['departement']+item['classement']+'.jpg')
        elif spider.name == 'departement':
            json_path = 'json/'+item['departement']
            if not os.path.exists(json_path):
                os.makedirs(json_path)
            file = open(json_path+'/'+'produits_exporter.json', 'wb')
            self.exporter = JsonItemExporter(file, encoding='utf-8', ensure_ascii=False)
            self.exporter.start_exporting()
            self.exporter.export_item(item)
            img_path = 'img/'+item['departement']
            if not os.path.exists(img_path):
                os.makedirs(img_path)
            request.urlretrieve(item['img_url'], img_path+'/'+ item['classement'] + '.jpg')
        return item

    def clean_string(self,string):
        return string.replace('\n','').replace('\xa0','').strip()

