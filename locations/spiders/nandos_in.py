# -*- coding: utf-8 -*-
import json
import re

import scrapy

from locations.items import GeojsonPointItem


class NandosINSpider(scrapy.Spider):
    name = "nandos_in"
    item_attributes = {"brand": "Nando's", "brand_wikidata": "Q3472954"}
    allowed_domains = ["www.nandosindia.com"]
    start_urls = [
        "https://www.nandosindia.com/eat/restaurants-all",
    ]
    download_delay = 0.3

    def parse(self, response):
        urls = response.xpath(
            '//ul[@class="row row-fixed-cols list-unstyled restaurant-list"]/li/a/@href'
        ).extract()

        for url in urls:
            yield scrapy.Request(
                url=response.urljoin(url.strip()), callback=self.parse_store
            )

    def parse_store(self, response):
        data = response.xpath(
            '//script[@type="application/ld+json" and contains(text(), "address")]/text()'
        ).extract_first()

        if data:
            store_data = json.loads(data)
            ref = re.search(r".+/(.+?)/?(?:\.html|$)", response.url).group(1)

            properties = {
                "name": store_data["name"],
                "ref": ref,
                "addr_full": store_data["address"]["streetAddress"],
                "city": store_data["address"]["addressLocality"],
                "state": store_data["address"]["addressRegion"],
                "postcode": store_data["address"]["postalCode"],
                "phone": store_data["contactPoint"][0].get("telephone"),
                "website": response.url,
                "country": "IN",
                "lat": store_data["geo"]["latitude"],
                "lon": store_data["geo"]["longitude"],
            }

            yield GeojsonPointItem(**properties)
