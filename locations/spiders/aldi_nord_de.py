# -*- coding: utf-8 -*-
import re

import scrapy

from locations.items import GeojsonPointItem


class AldiNordDESpider(scrapy.Spider):
    name = "aldi_nord_de"
    item_attributes = {"brand": "ALDI Nord", "brand_wikidata": "Q41171373"}
    allowed_domains = ["www.aldi-nord.de"]
    start_urls = [
        "https://www.aldi-nord.de/tools/filialen-und-oeffnungszeiten.html",
    ]

    def parse(self, response):
        urls = response.xpath(
            '//div[@class="mod-stores__multicolumn"]/p/a/@href'
        ).extract()
        is_store_list = response.xpath(
            '//div[@class="mod mod-stores"]//div[@class="mod-stores__overview-company-tools"]/a/@href'
        ).extract()

        if not urls and is_store_list:
            for store_url in is_store_list:
                yield scrapy.Request(
                    response.urljoin(store_url), callback=self.parse_store
                )
        else:
            for url in urls:
                yield scrapy.Request(response.urljoin(url))

    def parse_store(self, response):
        ref = re.search(r".+/(.+?)/?(?:\.html|$)", response.url).group(1)
        country = re.search(r"aldi-nord\.(\w{2}?)\/", response.url).group(1)

        properties = {
            "ref": ref,
            "name": response.xpath(
                '//div[@class="mod-overview-intro__content"]/h1/text()'
            ).extract_first(),
            "addr_full": response.xpath(
                'normalize-space(//span[@itemprop="streetAddress"]//text())'
            ).extract_first(),
            "city": response.xpath(
                'normalize-space(//span[@itemprop="addressLocality"]//text())'
            ).extract_first(),
            "postcode": response.xpath(
                'normalize-space(//span[@itemprop="postalCode"]//text())'
            ).extract_first(),
            "country": country,
            "website": response.url,
        }

        yield GeojsonPointItem(**properties)
