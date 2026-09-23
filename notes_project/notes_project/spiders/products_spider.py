import scrapy

data = '/content/drive/MyDrive/notes_project\notes_project/items'

from data import ProductsScraperItem #made in the previous step  
class QuotesSpider(scrapy.Spider):  
            name = "quotes"  
            start\_urls = \[  
                'http://quotes.toscrape.com/page/1/',  
            \]  
            def parse(self, response):  
                for quote in response.css('div.quote'):  
                    item = QuotesScraperItem()  
                    item\['text'\] = ''.join(quote.css('span.text::text').get())  
                    item\['author'\] = ''.join(quote.css('span small::text').get())  
                    yield item  
                next\_page = response.css('li.next a::attr(href)').get()  
                if next\_page is not None:  
                    yield response.follow(next\_page, self.parse)