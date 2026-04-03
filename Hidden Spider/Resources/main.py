import scrapy

# To run, use `scrapy runspider main.py > output.log`
# If you don't have scrapy, install it with `pip install Scrapy`
# Check the path `$HOME/.local/bin/` if unavailable after installing

class HiddenSpider(scrapy.Spider):
    name = "hidden"
    start_urls = ["http://127.0.0.1:8080/.hidden/"]
    custom_settings = {
        "CONCURRENT_REQUESTS": 64,
        "LOG_LEVEL": "ERROR",
    }

    def parse(self, response):
        links = response.css('a::attr(href)').getall()
        
        for href in links:
            if href == "../":
                continue

            if "readme" in href.lower():
                yield response.follow(href, self.parse_readme)

            elif href.endswith("/"):
                yield response.follow(href, self.parse)
    
    def parse_readme(self, response):
        print(response.text, end="")
        if len(response.text) >= 64:
            print("Found in:", response.url)