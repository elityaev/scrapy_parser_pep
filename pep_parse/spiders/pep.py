import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        section = response.xpath('//*[@id="numerical-index"]')
        pep_links = section.css(
            'a[class="pep reference internal"]::attr(href)').getall()
        for pep_link in pep_links:
            yield response.follow(f'{pep_link}/', callback=self.parse_pep)

    def parse_pep(self, response):
        pep_title = response.css('h1.page-title *::text').getall()
        str_pep_title = ''.join(pep_title)
        search_string = re.search(
            r'PEP (?P<number>\d+)\s–\s(?P<name>.*)', str_pep_title
        )
        data = {
            'number': search_string.group('number'),
            'name': search_string.group('name'),
            'status': response.css('dt:contains("Status") + dd::text') .get()

        }
        yield PepParseItem(data)
