import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for container in response.xpath('//div[@class="quote"]'):
            yield {
                'quote': container.xpath('.//span[@class="text"]/text()').get(), 
                'author': container.xpath('.//small[@class="author"]/text()').get()
            }