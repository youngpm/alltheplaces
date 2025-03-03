# -*- coding: utf-8 -*-
from scrapy.spiders import SitemapSpider
from locations.items import GeojsonPointItem
from locations.hours import OpeningHours


class DollarGeneralSpider(SitemapSpider):
    name = "dollar_general"
    item_attributes = {"brand": "Dollar General", "brand_wikidata": "Q145168"}
    allowed_domains = ["dollargeneral.com"]
    sitemap_urls = ["https://www.dollargeneral.com/sitemap-main.xml"]
    sitemap_rules = [
        (
            r"https:\/\/www\.dollargeneral\.com\/store-directory\/.*\/\d+\.html$",
            "parse",
        ),
    ]

    def parse(self, response):
        properties = {
            "street_address": response.xpath(
                "//div[@data-address]/@data-address"
            ).extract_first(),
            "city": response.xpath("//div[@data-city]/@data-city").extract_first(),
            "state": response.xpath("//div[@data-state]/@data-state").extract_first(),
            "postcode": response.xpath("//div[@data-zip]/@data-zip").extract_first(),
            "lat": response.xpath(
                "//div[@data-latitude]/@data-latitude"
            ).extract_first(),
            "lon": response.xpath(
                "//div[@data-longitude]/@data-longitude"
            ).extract_first(),
            "phone": response.xpath("//div[@data-phone]/@data-phone").extract_first(),
            "website": response.url,
            "ref": response.url.rsplit("/", 1)[-1].rsplit(".")[0],
        }

        o = OpeningHours()
        for d in [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
        ]:
            hours = response.xpath(f"//div[@data-{d}]/@data-{d}").extract_first()
            from_time, to_time = hours.split(":")
            o.add_range(d.title()[:2], from_time, to_time, "%H%M")

        properties["opening_hours"] = o.as_opening_hours()

        yield GeojsonPointItem(**properties)
