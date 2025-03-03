# -*- coding: utf-8 -*-
import re

import scrapy

from locations.hours import DAYS
from locations.linked_data_parser import LinkedDataParser

daysRe = rf"(?:{'|'.join(DAYS)})"


class BatteriesPlusSpider(scrapy.spiders.SitemapSpider):
    name = "batteriesplus"
    # download_delay = 1
    item_attributes = {"brand": "Batteries Plus Bulbs", "brand_wikidata": "Q17005157"}
    allowed_domains = ["batteriesplus.com"]
    sitemap_urls = [
        "https://www.batteriesplus.com/bpb_store-locator_sitemap.xml",
    ]
    sitemap_rules = [
        (r"/batteries-plus-", "parse"),
    ]

    def parse(self, response):
        if 301 in response.request.meta.get("redirect_reasons", []):
            return
        ld = LinkedDataParser.find_linked_data(response, "ElectronicsStore")
        ld["openingHours"] = re.findall(rf"({daysRe}[^A-Z]*) ", ld["openingHours"])
        item = LinkedDataParser.parse_ld(ld)
        item["ref"] = response.url.rsplit("-", 1)[-1]
        yield item
