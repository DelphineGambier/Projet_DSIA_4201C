import scrapy
from amazonSpider.items import AmazonspiderItem

class departementSpider(scrapy.Spider):
    name = 'departement'
    def __init__(self, category=None, *args, **kwargs):
        super(departementSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://www.amazon.fr/gp/bestsellers/%s' % category]

    def parse(self, response):
        category = response.xpath('//*[@id="zg-right-col"]/h1/span/text()').extract_first()
        for p in response.xpath('//*[@id="zg-ordered-list"]/li'):
            item = AmazonspiderItem()
            item['departement'] = category
            item['classement'] = p.xpath('span/div/div/span[1]/span/text()').extract_first()
            item['produit'] = p.xpath('span/div/span/a/div/text()').extract_first()
            item['img_url'] = p.xpath('span/div/span/a/span/div/img/@src').extract_first()
            item['evaluations'] = p.xpath('span/div/span/div[@class="a-icon-row a-spacing-none"]/a[2]/text()').extract_first()
            petit_prix = p.xpath('span/div/span/div[@class="a-row"]/a/span/span[1]/text()').extract_first()
            grand_prix = p.xpath('span/div/span/div[@class="a-row"]/a/span/span[2]/text()').extract_first()
            prix = p.xpath('span/div/span/div[@class="a-row"]/a/span/span/text()').extract_first()
            if prix == None and petit_prix == None and grand_prix == None:
                text = p.xpath('span/div/span/a[@class="a-link-normal a-text-normal"]/span/text()').extract_first()
                pr = p.xpath('span/div/span/a[@class="a-link-normal a-text-normal"]/span/span/span/text()').extract_first()
                if text != None:
                    item['prix'] = text+' '+pr
                else:
                    item['prix'] = None
            else:
                if len(p.xpath('span/div/span/div[@class="a-row"]/a/span/span'))>1:
                    item['prix'] = petit_prix+'-'+grand_prix
                else:
                    item['prix'] = prix
            yield item

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.fr/']
    start_urls = ['https://www.amazon.fr/gp/bestsellers/electronics', 'https://www.amazon.fr/gp/bestsellers/beauty',
                  'https://www.amazon.fr/gp/bestsellers/jewelry', 'https://www.amazon.fr/gp/bestsellers/videogames',
                  'https://www.amazon.fr/gp/bestsellers/software', 'https://www.amazon.fr/gp/bestsellers/books',
                  'https://www.amazon.fr/gp/bestsellers/english-books', 'https://www.amazon.fr/gp/bestsellers/audible',
                  'https://www.amazon.fr/gp/bestsellers/toys', 'https://www.amazon.fr/gp/bestsellers/boost',
                  'https://www.amazon.fr/gp/bestsellers/pet-supplies', 'https://www.amazon.fr/gp/bestsellers/amazon-devices',
                  'https://www.amazon.fr/gp/bestsellers/mobile-apps', 'https://www.amazon.fr/gp/bestsellers/automotive',
                  'https://www.amazon.fr/gp/bestsellers/luggage', 'https://www.amazon.fr/gp/bestsellers/hi',
                  'https://www.amazon.fr/gp/bestsellers/gift-cards', 'https://www.amazon.fr/gp/bestsellers/baby',
                  'https://www.amazon.fr/gp/bestsellers/music', 'https://www.amazon.fr/gp/bestsellers/shoes',
                  'https://www.amazon.fr/gp/bestsellers/industrial', 'https://www.amazon.fr/gp/bestsellers/kitchen',
                  'https://www.amazon.fr/gp/bestsellers/dvd', 'https://www.amazon.fr/gp/bestsellers/grocery',
                  'https://www.amazon.fr/gp/bestsellers/officeproduct', 'https://www.amazon.fr/gp/bestsellers/appliances',
                  'https://www.amazon.fr/gp/bestsellers/hpc', 'https://www.amazon.fr/gp/bestsellers/computers',
                  'https://www.amazon.fr/gp/bestsellers/musical-instruments', 'https://www.amazon.fr/gp/bestsellers/lawn-garden',
                  'https://www.amazon.fr/gp/bestsellers/lighting', 'https://www.amazon.fr/gp/bestsellers/watch',
                  'https://www.amazon.fr/gp/bestsellers/handmade', 'https://www.amazon.fr/gp/bestsellers/sports',
                  'https://www.amazon.fr/gp/bestsellers/apparel']

    def parse(self, response):
        category = response.xpath('//*[@id="zg-right-col"]/h1/span/text()').extract_first()
        for p in response.xpath('//*[@id="zg-ordered-list"]/li'):
            if p.xpath('span/div/div/span[1]/span/text()').extract_first() == '#4':
                break
            item = AmazonspiderItem()
            item['departement'] = category
            item['classement'] = p.xpath('span/div/div/span[1]/span/text()').extract_first()
            item['produit'] = p.xpath('span/div/span/a/div/text()').extract_first()
            item['img_url'] = p.xpath('span/div/span/a/span/div/img/@src').extract_first()
            item['evaluations'] = p.xpath('span/div/span/div[@class="a-icon-row a-spacing-none"]/a[2]/text()').extract_first()
            petit_prix = p.xpath('span/div/span/div[@class="a-row"]/a/span/span[1]/text()').extract_first()
            grand_prix = p.xpath('span/div/span/div[@class="a-row"]/a/span/span[2]/text()').extract_first()
            prix = p.xpath('span/div/span/div[@class="a-row"]/a/span/span/text()').extract_first()
            if prix == None and petit_prix == None and grand_prix == None:
                text = p.xpath('span/div/span/a[@class="a-link-normal a-text-normal"]/span/text()').extract_first()
                pr = p.xpath('span/div/span/a[@class="a-link-normal a-text-normal"]/span/span/span/text()').extract_first()
                if text != None:
                    item['prix'] = text+' '+pr
                else:
                    item['prix'] = None
            else:
                if len(p.xpath('span/div/span/div[@class="a-row"]/a/span/span'))>1:
                    item['prix'] = petit_prix+'-'+grand_prix
                else:
                    item['prix'] = prix
            yield item