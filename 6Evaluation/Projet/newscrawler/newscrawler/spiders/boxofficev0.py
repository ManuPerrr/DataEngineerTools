import scrapy
import json
import os
import numpy as np
import pandas as pd
from scrapy import Request
from ..items import ArticleItem


class BoxOfficeSpider0(scrapy.Spider):
    name = "boxofficev0"
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'
    allowed_domains = ["www.boxofficemojo.com"]
    
    def researchlink():
        # path = os.path.dirname(os.path.abspath(__file__))
        # path = path.replace("newscrawler/spiders", "titlelink.csv")
        path = "C:/Users/perei/Desktop/Data Engineering/DataEngineerTools/6Evaluation/Projet/newscrawler/rsltv4.csv"
        df_movies = pd.read_csv(path)
        for i in range (df_movies.shape[0]):
            if (df_movies["catinfo1"][i] != ' Titre original '):
                df_movies["titleint"][i] = df_movies["title"][i]
        df_movies = df_movies.drop(columns=['catinfo1'])
        links = []
        for k in df_movies['titleint']:
            links.append("https://www.boxofficemojo.com/search/?q="+k.replace(" ", "+"))
        return(links)
        
    start_urls = researchlink()

    def parse(self, response):
        links = "https://www.boxofficemojo.com" + response.css(".a-section.mojo-gutter .a-fixed-left-grid")[0].css("a::attr(href)")[1].extract()
        
        yield {
            "links":links
        }
 
        
    
    
    

    
        
        
