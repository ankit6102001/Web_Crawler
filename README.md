# Web_Crawler

This is a simple web crawler built using Python, which can crawl a website, extract data, and store it in a MongoDB database. The project utilizes the Flask web framework for the UI, BeautifulSoup and Scrapy for crawling, and MongoDB for storage.

Features
Crawl a website recursively to a specified depth.
Extract all links (URLs) from the crawled pages.
Store crawled data in a MongoDB database.
Track the crawl status, showing whether it's ongoing or completed.
User-friendly interface using Flask to control the crawling process.
Option to specify the maximum depth for the crawl.

Tech Stack
Python: Programming language used for the crawler.
Flask: Web framework used to build the user interface.
BeautifulSoup: Used for parsing HTML and extracting links.
Scrapy: (Optional) For advanced crawling and data extraction.
MongoDB: NoSQL database used for storing crawled data.
HTML/CSS: For front-end design.
