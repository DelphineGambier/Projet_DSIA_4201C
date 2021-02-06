# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from amazonSpider.items import AmazonspiderItem
from scrapy.exporters import JsonItemExporter
from scrapy.utils.project import get_project_settings
settings = get_project_settings()
from urllib import request
import os

class AmazonspiderPipeline:

    def __init__(self):
        # self.file = open('json/produits_exporter.json', 'wb')
        # self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        # self.exporter.start_exporting()
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
        self.collection.delete_many({})

    def close_spider(self, spider):
        # self.exporter.finish_exporting()
        # self.file.close()
        pass


    def process_item(self, item, spider):
        item['classement'] = self.clean_string(item['classement'])
        if item['produit'] != None:
            item['produit'] = self.clean_string(item['produit'])
        else:
            item['produit'] = "Cet article n'est plus disponible"
        if item['evaluations'] != None:
            item['evaluations'] = self.clean_string(item['evaluations'])
        if item['prix'] != None:
            item['prix'] = self.clean_string(item['prix'])
        # self.exporter.export_item(item)
        result = self.collection.find_one({"$and":[{"classement":item['classement'], "departement":item['departement']}]})
        if result is None:
            self.collection.insert(dict(item))
        return item

    def clean_string(self,string):
        return string.replace('\n','').replace('\xa0','').strip()


class departPipeline:

    def __init__(self):
        # self.file = open('json/departementDetails.json', 'wb')
        # self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        # self.exporter.start_exporting()
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION2']]
        self.collection.delete_many({})


    def close_spider(self, spider):
        # self.exporter.finish_exporting()
        # self.file.close()
        pass

    def process_item(self, item, spider):
        item['classement'] = self.clean_string(item['classement'])
        if item['produit'] != None:
            item['produit'] = self.clean_string(item['produit'])
        else:
            item['produit'] = "Cet article n'est plus disponible"
        if item['evaluations'] != None:
            item['evaluations'] = self.clean_string(item['evaluations'])
        if item['prix'] != None:
            item['prix'] = self.clean_string(item['prix'])
        # self.exporter.export_item(item)
        self.collection.insert(dict(item))
        img_path = 'static/img/'+item['departement']
        if not os.path.exists(img_path):
            os.makedirs(img_path)
        if item['img_url'] != None:
            request.urlretrieve(item['img_url'], img_path+'/'+ item['classement'] + '.jpg')
        return item

    def clean_string(self,string):
        return string.replace('\n','').replace('\xa0','').strip()

