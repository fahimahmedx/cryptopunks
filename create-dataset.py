import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

from time import sleep
from random import randint

page = "https://www.larvalabs.com/cryptopunks/sales"
request = requests.get(page)
soup = BeautifulSoup(request.text)

base_url = "https://www.larvalabs.com"
sale_links = []

# find all cryptopunk links.
for link in soup.find_all('a'):
    url = link.get('href')

    #check if URL exists and if URL is for a cryptopunk
    if url and '/cryptopunks/details/' in url:
        #print(link.get('href'))
        sale_links.append(url)

#print(len(sale_links))
