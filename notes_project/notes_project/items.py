import scrapy
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass


@dataclass
class ProductsScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name: str | None = None
    guest_name = scrapy.Field()  
    episode_date = scrapy.Field()
    product_name = scrapy.Field()
    product_brand = scrapy.Field()
    main_category = scrapy.Field()
    sub_category = scrapy.Field()
    price_tier = scrapy.Field()
    product_link = scrapy.Field()
    guest_insights = scrapy.Field()
    source_url = scrapy.Field()
