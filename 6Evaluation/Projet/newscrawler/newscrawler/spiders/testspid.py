import scrapy
import json
import os
import numpy as np
import pandas as pd
from scrapy import Request
from ..items import ArticleItem



class AllocineSpider(scrapy.Spider):
    name = "testspid"
    allowed_domains = ["www.allocine.fr"]
    start_urls = [
        "https://www.allocine.fr/film/fichefilm_gen_cfilm=56714.html"
    ]

    def parse(self, response):
        date = response.css(".meta-body").css("span::text").extract_first().strip()
        info = json.loads(response.css("script::text")[-2].extract())
        notepre = response.css(".stareval-note::text")[0].extract()
        recomp = response.css(".item").css("span::text").extract()[13].strip()
        budget = response.css(".item").css("span::text").extract()[29].strip()
        
        yield {
            "date":date,
            "info":info,
            "notepre":notepre,
            "recomp":recomp,
            "budget":budget
        }
    
    
  






 