import scrapy
from amazonSpider.items import AmazonspiderItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.fr/']
    start_urls = ['https://www.amazon.fr/gp/bestsellers/electronics',
                  'https://www.amazon.fr/gp/bestsellers/videogames',
                  'https://www.amazon.fr/gp/bestsellers/software',
                  'https://www.amazon.fr/gp/bestsellers/books']

    def parse(self, response):
        category = response.xpath('//*[@id="zg-right-col"]/h1/span/text()').extract_first()
        for p in response.xpath('//*[@id="zg-ordered-list"]/li'):
            item = AmazonspiderItem()
            item['departement'] = category
            item['classement'] = p.xpath('span/div/div/span[1]/span/text()').extract_first()
            item['produit'] = p.xpath('span/div/span/a/div/text()').extract_first()
            item['evaluations'] = p.xpath('span/div/span/div[@class="a-icon-row a-spacing-none"]/a[2]/text()').extract_first()
            if len(p.xpath('span/div/span/div[@class="a-row"]/a/span/span'))>1:
                petit_prix = p.xpath('span/div/span/div[@class="a-row"]/a/span/span[1]/text()').extract_first()
                t = p.xpath('span/div/span/div[@class="a-row"]/a/span/text()').extract_first()
                grand_prix = p.xpath('span/div/span/div[@class="a-row"]/a/span/span[2]/text()').extract_first()
                item['prix'] = petit_prix+t+grand_prix
            else:
                item['prix'] = p.xpath('span/div/span/div[@class="a-row"]/a/span/span/text()').extract_first()
            yield item