import json
import pathlib
from datetime import datetime

import scrapy
from loguru import logger
from scrapy.crawler import CrawlerProcess


class SpiderExample(scrapy.Spider):
    name = "movies"
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

    url_main = "http://www.scrapethissite.com/pages/ajax-javascript/"
    url_ajax = url_main + "?ajax=true&year="

    @property
    def path_data(self) -> pathlib.Path:
        """
        So that we can access the data folder
        """
        path = pathlib.Path(__file__).parent
        for i in range(20):
            if (path / "data/").exists():
                return path / f"data/raw/scrapes/{self.name}/{self.timestamp}"
            path = path.parent
        raise FileNotFoundError()

    def start_requests(self):

        # First navigate to the main page to
        # get all years
        yield scrapy.Request(
            url=self.url_main,
            callback=self.parse,
        )

    def parse(self, response):

        # Get all years
        years = response.xpath(
            "//a[contains(@class, 'year-link')]/@id"
        ).getall()
        assert years, "Couldn't find any years"

        # Loop through the years
        for year in years:

            # Use the ajax request to get the data in json format
            logger.info(f"Requesting AJAX json response for year {year}")
            yield scrapy.Request(
                url=self.url_ajax + year,
                callback=self.upload_json,
                headers={"Content-Type": "application/json"},
                meta={"year": year},
            )

    def upload_json(self, response):
        data = response.json()
        assert data, "Data not found"

        # Create path
        year = response.meta["year"]
        upload_dir = self.path_data / year
        upload_dir.mkdir(parents=True, exist_ok=True)
        upload_path = upload_dir / "content.json"

        # Save data
        logger.info(f"Uploading to {upload_path.resolve()}")
        with open(str(upload_path.resolve()), "w") as f:
            json.dump(data, f)


def main():
    process = CrawlerProcess()
    process.crawl(SpiderExample)
    process.start()


if __name__ == "__main__":
    main()
