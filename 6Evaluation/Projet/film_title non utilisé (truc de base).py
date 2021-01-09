import scrapy

class TitleSpider (scrapy.Spider):
    name = "Titre de film"
    start_urls = ["https://www.allocine.fr/film/meilleurs/",]

    def parse(self, response):
        for titre in response.xpath('//h2[@class="meta-title"]'):
            text_value = titre.xpath('a/text()').extract_first()
            yield { 'Titre' : text_value }