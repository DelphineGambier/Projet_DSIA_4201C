# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    departement = scrapy.Field()
    classement = scrapy.Field()
    produit = scrapy.Field()
    evaluations = scrapy.Field()
    prix = scrapy.Field()
    img_url = scrapy.Field()