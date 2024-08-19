import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd

class RolodexSpider(scrapy.Spider):
    name = "rolodex"
    start_id = 1
    base_url = "http://www.stealmyrolodex.com/viewPeople/"
    
    def start_requests(self):
        url = self.base_url + str(self.start_id)
        yield scrapy.Request(url=url, callback=self.parse, meta={'start_id': self.start_id})
    
    def parse(self, response):
        start_id = response.meta['start_id']
        person_data = {}
        
        try:
            person_data["Name"] = response.xpath('//input[@id="name"]/@value').get("").strip()
            person_data["Address"] = response.xpath('//input[@id="address"]/@value').get("").strip()
            person_data["Email"] = response.xpath('//input[@id="email"]/@value').get("").strip()
            person_data["Secondary Email"] = response.xpath('//input[@id="secondemail"]/@value').get("").strip()
            person_data["Phone"] = response.xpath('//input[@id="phone"]/@value').get("").strip()
            person_data["Role"] = response.xpath('//input[@id="role"]/@value').get("").strip()

            company_section = response.xpath('//div[@class="card card-secondary"]')
            company_inputs = company_section.xpath('.//input[@class="form-control"]')
            person_data["Company"] = company_inputs[0].xpath('@value').get("").strip() if len(company_inputs) > 0 else ""
            person_data["Category"] = company_inputs[1].xpath('@value').get("").strip() if len(company_inputs) > 1 else ""
            person_data["Company Address"] = company_inputs[2].xpath('@value').get("").strip() if len(company_inputs) > 2 else ""

            person_data["Linkedin Name"] = response.xpath('//input[@class="form-control"]')[7].xpath('@value').get("").strip()
            person_data["Linkedin Connections"] = response.xpath('//input[@class="form-control"]')[8].xpath('@value').get("").strip()
            person_data["Decision Maker"] = response.xpath('//input[@class="form-control"]')[10].xpath('@value').get("").strip()

            unwanted_values = ['<div style=']
            if any(value in person_data.values() for value in unwanted_values):
                raise AttributeError("Unwanted values found.")

            self.save_to_csv(person_data, start_id)

        except AttributeError:
            self.logger.info(f"No data found for ID {start_id}. Moving to the next page.")
        
        next_id = start_id + 1
        if response.status == 200:
            next_url = self.base_url + str(next_id)
            yield scrapy.Request(url=next_url, callback=self.parse, meta={'start_id': next_id})

    def save_to_csv(self, data, start_id):
        df = pd.DataFrame([data])
        if start_id == 1:
            df.to_csv("scraped_data2.csv", index=False, encoding='utf-8-sig')
        else:
            with open("scraped_data2.csv", "a", encoding='utf-8-sig') as f:
                df.to_csv(f, index=False, header=False, encoding='utf-8-sig')

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(RolodexSpider)
    process.start()
