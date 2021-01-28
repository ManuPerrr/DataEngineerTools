import scrapy
from scrapy import Request
from ..items import ArticleItem



class AllocineSpider(scrapy.Spider):
    name = "besttitlev1"
    allowed_domains = ["www.allocine.fr"]
    start_urls = ["https://www.allocine.fr/film/meilleurs/?page="+str(i) for i in range (1, 31)]

    def parse(self, response):
        all_titlelinks = {
            name:response.urljoin(url) for name, url in zip(
                response.css("#content-layout .meta-title").css("a::text").extract(),
                response.css("#content-layout .meta-title").css("a::attr(href)").extract()
            )
        }
        yield {
            "all_titlelinks":all_titlelinks,
        }
    
    