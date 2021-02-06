import scrapy
import json
import os
import numpy as np
import pandas as pd
from scrapy import Request
from ..items import ArticleItem


class AllocineSpider4(scrapy.Spider):
    name = "besttitlev4"
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'
    allowed_domains = ["www.allocine.fr"]
    start_urls = ["https://www.allocine.fr/film/meilleurs/?page="+str(i) for i in range (1, 31)]

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
        title = response.css("#content-layout .titlebar-title.titlebar-title-lg::text").extract()[0]
        titleint = response.css(".ovw-synopsis-info .that::text")[0].extract() 
        catinfo1 = response.css(".ovw-synopsis-info .what.light::text")[0].extract()
        synop = " ".join(response.css("#synopsis-details .content-txt::text").extract()).strip()
        date = response.css(".meta-body").css("span::text").extract_first().strip()
        duree = response.css(".meta-body-item.meta-body-info::text").extract()[3].strip()
        genre = response.css(".meta-body-item.meta-body-info").css("span::text")[3:].extract()
        cast = response.css(".section.ovw").css(".card.person-card").css("a::text").extract()
        real = response.css(".meta-body-item.meta-body-direction").css("span::text").extract()[1]
        nbrnote = response.css(".stareval").css(".stareval-review::text")[1].extract().split(" ")[1]
        nbrcrit = response.css(".stareval").css(".stareval-review::text")[1].extract().split(" ")[4]
        notepub = response.css(".stareval").css(".stareval-note::text")[1].extract()
        notepre = response.css(".stareval-note::text")[0].extract()
        
        yield {
            "title":title,
            "titleint":titleint,
            "catinfo1":catinfo1,
            "synop":synop,
            "date":date,
            "duree":duree,
            "genre":genre,
            "cast":cast,
            "real":real,
            "nbrnote":nbrnote,
            "nbrcrit":nbrcrit,
            "notepub":notepub,
            "notepre":notepre
        }
 
        
    

    
        
        
