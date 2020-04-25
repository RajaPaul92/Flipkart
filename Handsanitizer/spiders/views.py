import scrapy
from ..items import HandsanitizerItem


class HandSanitizer(scrapy.Spider):
    name = "handSanitizer"
    page_number = 2
    start_urls = [
        'https://www.flipkart.com/search?q=hand+sanitizer&sid=g9b%2Cema%2Crhm%2Cjrn&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=hand+sanitizer%7CHand+Sanitizer&requestId=5ef3ab81-9efa-42d4-94e5-7c0d3bc4a9d8&as-searchtext=hand'
    ]

    def parse(self, response):
        items = HandsanitizerItem()
        sanitizer = response.css('div._3liAhj')
        for san in sanitizer:
            sanitizer_name = sanitizer.css('a._2cLu-l::text').extract()
            sanitizer_rating = sanitizer.css('div.hGSR34::text').extract()
            sanitizer_price = sanitizer.css('div._1vC4OE::text').extract()

            items['sanitizer_name'] = sanitizer_name
            items['sanitizer_rating'] = sanitizer_rating
            items['sanitizer_price'] = sanitizer_price

        yield items

        next_page = 'https://www.flipkart.com/search?q=hand+sanitizer&sid=g9b%2Cema%2Crhm%2Cjrn&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=hand+sanitizer%7CHand+Sanitizer&requestId=5ef3ab81-9efa-42d4-94e5-7c0d3bc4a9d8&as-searchtext=hand&page=2'
        if HandSanitizer.page_number <= 6:
            HandSanitizer.page_number += 1
            yield response.follow(next_page, callback=self.parse)