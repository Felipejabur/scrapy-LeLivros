import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import urllib
import json

class LeLivros(scrapy.Spider):
    name = 'lelivros'

    base_url = 'https://lelivros.love/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'

    }

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'lelivros.csv'
    }

    def start_requests (self):
        for page in range(1,684):
            next_page = self.base_url + 'page' + '/' + str(page)

            yield scrapy.Request(url=next_page, headers=self.headers, callback=self.parse)


    def parse(self,res):

        '''
        with open('res.html', 'w') as f:
            f.write(res.text)
        '''
        '''
        content = ''

        with open('res.html', 'r') as f:
            for line in f.read():
                content += line

        res = Selector(text=content)
        '''
        for card in res.css('li[class="post-17105 product type-product status-publish has-post-thumbnail hentry first instock"]'):

            features = {
                'Livro': card.css('h3::text')
                             .get()
                             .split('\u2013 ')[0],


                'Autor': card.css('h3::text')
                             .get()
                             .split('\u2013 ')[-1],

                'Link': card.css('a::attr(href)')
                            .get()

            }

            yield features







# main driver
if __name__ == '__main__':
    # run scraper
    process = CrawlerProcess()
    process.crawl(LeLivros)
    process.start()


    #debug
    #LeLivros.parse(LeLivros, '')
