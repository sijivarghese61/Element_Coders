# E-Commerce Product Scraper
This Python script scrapes product details from a Flipkart product page. It fetches information such as the product name, price, rating, reviews, and description of a Oneplus Mobile product.

### Features
* Fetches product name, price, rating, and description.
* Extracts the review.
* Uses BeautifulSoup for HTML parsing and Requests for HTTP requests.
  
### Requirements
* Python 3.x
* 'requests' library
* 'beautifulsoup4' library

### Code Explanation
* Imports:

- 'requests' : Used to send HTTP requests to the product page.
- 'BeautifulSoup' from 'bs4' : Used to parse HTML content.

* URL: The URL of the Flipkart product page to scrape.

* Headers: A User-Agent is used to simulate a browser visit and avoid getting blocked.

* HTTP Request: Sends a GET request to the product URL.

* HTML Parsing: Parses the HTML content using BeautifulSoup.

* Data Extraction: Retrieves product details such as name, price, rating, reviews, and description using 'find' and 'find_all' methods.

* Printing Results: Outputs the extracted product details to the console.
