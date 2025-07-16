import scrapy
import pandas as pd
class MySpider(scrapy.Spider):
    name = 'myspider'
    df = pd.read_csv('/Users/teresabui/Downloads/UCLA 2023-24/UCLA W24/STATS 133/Final Project/nypost.csv')
    start_urls = df['Link'].tolist() 

    def parse(self, response):
        yield from self.parse_article(response)

    def parse_article(self, response):
        content = response.css('div.entry-content') 
        text = content.css('p::text').getall()
        yield {'text': ' '.join(text)}
