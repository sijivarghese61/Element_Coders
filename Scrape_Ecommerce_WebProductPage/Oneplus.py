# Importing 'requests' to get the content from given url and 'BeautifulSoup' from 'bs4' to parse the html content of the requested url.
import requests

from bs4 import BeautifulSoup

# url of the web product(oneplus 12r mobile) page.
url = 'https://www.flipkart.com/oneplus-12r-cool-blue-256-gb/p/itm347349f7db2f2?pid=MOBGXGT7HKG8JFGU&lid=LSTMOBGXGT7HKG8JFGUDKPDMZ&marketplace=FLIPKART&sattr[]=color&sattr[]=storage&sattr[]=ram&st=color'

# For fake a browser visit by using Python's Requests so that default IP does not get blocked.
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# Sending a get request to the given url with the above headers.
r = requests.get(url, headers=headers)

# For parsing the html content of the url page.
soup = BeautifulSoup(r.content,'html.parser')

# Getting the product name, price, rating, reviews, and description of the product using soup object, find and find_all method. 
name = soup.find('span',class_='VU-ZEz').get_text(strip=True)
price = soup.find('div',class_='Nx9bqj CxhGGd').get_text(strip=True)
rating = soup.find('div',class_='XQDdHH').get_text(strip=True)
description = soup.find('div',class_='yN+eNk').get_text(strip=True)

rev = soup.find('span',class_='Wphh3N').find_all('span')
i = 0
for element in rev:
    if i==3:
        review = element.get_text(strip=True)
    i = i + 1

# Printing the product name, price, rating, reviews, and description of the product.
print('Product Name: ',name,end='\n\n')
print('Product Price: ',price,end='\n\n')
print('Product Rating: ',rating,end='\n\n')
print('Product Review: ',review,end='\n\n')
print('Product Description: ',description)
