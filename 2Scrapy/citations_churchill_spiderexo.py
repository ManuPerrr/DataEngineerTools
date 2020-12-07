import scrapy

class ChurchillQuotesSpider(scrapy.Spider):
    name = "citations de Churchill"
    start_urls = ["http://evene.lefigaro.fr/citations/winston-churchill",]

    def parse(self, response):
        for cit in response.xpath('//div[@class="figsco__quote__text"]'):
            text_value = cit.xpath('a/text()').extract_first()
            #Exercice 3 :
            text_value = text_value.replace("“", "")
            text_value = text_value.replace("”", "")
            #fin exercice 3
            yield { 
                'text' : text_value,
                'author' : None 
            }
        for cit in response.xpath('//div[@class="figsco__fake__col-9]"'):
            text_value = cit.xpath('a/text()').extract_first()
            print(text_value)

        