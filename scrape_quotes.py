import requests
from requests import get
from bs4 import BeautifulSoup
import numpy as np
import time
import random

pages = np.arange(1,11,1)

quotes = ''

for page in pages:
    time.sleep(random.randint(1,10))
    
    url = 'http://quotes.toscrape.com/page/' + str(page) + '/'
    results = requests.get(url)
    soup = BeautifulSoup(results.text, 'html.parser')

    quote_div = soup.find_all('div', class_='quote')

    for container in quote_div:
        quote = container.span.text

        author = container.find('small', class_='author').text
        
        temp = quote + '  BY:  ' + author + '\n\n'
        quotes += temp
        
print(quotes)
