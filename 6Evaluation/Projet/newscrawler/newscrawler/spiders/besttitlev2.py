import scrapy
import json
import os
import numpy as np
import pandas as pd
from scrapy import Request
from ..items import ArticleItem


class AllocineSpider(scrapy.Spider):
    name = "besttitlev2"
    allowed_domains = ["www.allocine.fr"]
    start_urls = ["https://www.allocine.fr/film/meilleurs/?page="+str(i) for i in range (1, 31)]
    
    def getlinks(self):
        #path = os.path.dirname(os.path.abspath(__file__))
        #path = path.replace("newscrawler/spiders", "titlelink.csv")
        path = "C:/Users/perei/Desktop/Data Engineering/DataEngineerTools/6Evaluation/Projet/newscrawler/titlelink.csv"
        print(path)
        df = pd.read_csv(path).to_dict()
        #On récupère le dictionnaire de chaque page qui relie titre et lien sous la forme d'une string par page
        l = list(list(df.values())[0].values())
        #On découpe toute la string de manière à isoler tous les liens
        links = [l[i].strip().split("'") for i in range (len(l))]
        #Nous avions une liste de liste pour chacunes de pages, on rassemble tout sous une grande liste
        links = [string for l in links for string in l]
        #On garde uniquement les éléments étant des liens
        links = [ x for x in links if 'https' in x]
        return links    

    def parse(self, response):
        all_titlelinks = {
            name:response.urljoin(url) for name, url in zip(
                response.css("#content-layout .meta-title").css("a::text").extract(),
                response.css("#content-layout .meta-title").css("a::attr(href)").extract()
            )
        }
        for link in self.getlinks():
            yield Request(link, callback=self.parse_category)
    
    def parse_category(self, response):
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
 
        
    

    
        
        
