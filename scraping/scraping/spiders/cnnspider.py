import scrapy
import pandas as pd

class CNNSpider(scrapy.Spider):
    name = 'cnnspider'
    df = pd.read_csv('/Users/teresabui/Downloads/UCLA 2023-24/UCLA W24/STATS 133/Final Project/cnn.csv')
    start_urls = df['Link'].tolist() 

    def parse(self, response):
        yield from self.parse_article(response)

    #def parse_article(self, response):
    #    content = response.css('div.article__content') 
    #    text = content.css('p::text').getall()
    #    yield {'text': ' '.join(text)}
    
    def parse_article(self, response):
        # Find the content container
        content = response.css('div.article__content')
        # Initialize an empty list to hold all text pieces
        all_text = []
        # For each paragraph, extract all text, including that within <a> tags
        for paragraph in content.css('p'):
            text = paragraph.xpath('.//text()').getall()
            all_text.append(' '.join(text).strip())
        # Join all text pieces together and yield the result
        yield {'text': ' '.join(all_text)}