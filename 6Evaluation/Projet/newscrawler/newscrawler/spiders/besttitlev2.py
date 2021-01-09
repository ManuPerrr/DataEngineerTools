import scrapy
import json
from scrapy import Request
from ..items import ArticleItem


class AllocineSpider(scrapy.Spider):
    name = "besttitlev2"
    allowed_domains = ["www.allocine.fr"]
    start_urls = [
        "https://www.allocine.fr/film/meilleurs",
        "https://www.allocine.fr/film/meilleurs/?page=2",
        "https://www.allocine.fr/film/meilleurs/?page=3",
        "https://www.allocine.fr/film/meilleurs/?page=4",
        "https://www.allocine.fr/film/meilleurs/?page=5"
    ]

    def parse(self, response):
        all_titlelinks = {
            name:response.urljoin(url) for name, url in zip(
                response.css("#content-layout .meta-title").css("a::text").extract(),
                response.css("#content-layout .meta-title").css("a::attr(href)").extract()
            )
        }
        for link in all_titlelinks.values():
            yield Request(link, callback=self.parse_category)
    
    def parse_category(self, response):
        for movie in response.
    
    




    



class AllocineInfoSpider(scrapy.Spider):
    name = "infomovie"
    allowed_domains = ["www.allocine.fr"]
    start_urls = [
        "https://www.allocine.fr/film/fichefilm_gen_cfilm=10568.html"
    ]

    def parse(self, response):
        all_info = {
            name:response.urljoin(url) for name, url, notepress, recomp, budget  in zip(
                response.css(".meta-body").css("span::text").extract_first().strip(),
                json.loads(response.css("script::text")[-2].extract()),
                response.css(".stareval-note::text")[0].extract(),
                response.css(".item").css("span::text").extract()[13].strip(),
                response.css(".item").css("span::text").extract()[29].strip()
            )  
        }
        yield {
            "all_info":all_info,
        }
        
        
