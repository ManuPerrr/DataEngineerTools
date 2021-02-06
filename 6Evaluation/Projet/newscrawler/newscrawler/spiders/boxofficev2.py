import scrapy
import json
import os
import numpy as np
import pandas as pd
from scrapy import Request
from ..items import ArticleItem
import unicodedata
 
class BoxOfficeSpider2(scrapy.Spider):
    name = "boxofficev2"
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'
    allowed_domains = ["www.boxofficemojo.com"]
    
    def researchlink():
        # path = os.path.dirname(os.path.abspath(__file__))
        # path = path.replace("newscrawler/spiders", "titlelink.csv")
        path = "C:/Users/perei/Desktop/Data Engineering/DataEngineerTools/6Evaluation/Projet/newscrawler/rsltv4.csv"
        df_movies = pd.read_csv(path)
        for i in range (df_movies.shape[0]):
            if (df_movies["catinfo1"][i] != ' Titre original '):
                df_movies["titleint"][i] = unicodedata.normalize('NFD', df_movies["title"][i]).encode('ascii', 'ignore').decode('utf-8')
        df_movies = df_movies.drop(columns=['catinfo1'])
        links = []
        for k in df_movies['titleint']:
            links.append("https://www.boxofficemojo.com/search/?q="+k.replace(" ", "+"))
        return(links)
        
    start_urls = researchlink()

    def checkbudget(self, budget):
        if ("Budget" in budget):
            return (budget[budget.index('Budget')+1])
        else: 
            return (np.NaN)
    
    
    def parse(self, response):
        url = response.url
        movielinks = "https://www.boxofficemojo.com" + response.css(".a-section.mojo-gutter .a-fixed-left-grid")[0].css("a::attr(href)")[1].extract()
        yield Request(movielinks, callback=self.parse_category, meta={'url':url})
        
    def parse_category(self, response):
        url = response.meta['url']
        titleen = response.css(".a-fixed-left-grid-col .a-section .a-size-extra-large::text").extract()[0]
        budget = self.checkbudget((response.css(".mojo-gutter .mojo-hidden-from-mobile .a-section").css("span::text").extract()))
        boxdom = response.css(".a-section .a-size-medium").css("span::text").extract()[-8]  
        boxint = response.css(".a-section .a-size-medium").css("span::text").extract()[-5].strip()  
        boxtot = response.css(".a-section .a-size-medium").css("span::text").extract()[-2]
        
        yield {
            "url":url,
            "titleen":titleen,
            "budget":budget,
            "boxdom":boxdom,
            "boxint":boxint,
            "boxtot":boxtot
        }


    
        
        
