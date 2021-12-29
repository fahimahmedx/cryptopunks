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
# https://youtu.be/zD0FDYI5_rs
for link in soup.find_all('a'):
    url = link.get('href')

    #check if URL exists and if URL is for a cryptopunk
    if url and '/cryptopunks/details/' in url:
        #print(link.get('href'))
        sale_links.append(url)

ids = []
types = []
attributeCounts = []
attributes = []
sales = []
offers = []
bids = []

#try working with most recently sold CryptoPunk
request = requests.get(base_url + sale_links[0])
soup = BeautifulSoup(request.text)
print(soup.title.string)

# ID and type
details = soup.find("div", class_="col-md-10 col-md-offset-1 col-xs-12")
id = details.h1.text
type = details.h4.a.text

#attributes
details = soup.find("div", class_="col-md-10 col-md-offset-1")
attributeCount = details.p.a.text # number of attributes as a String
attributeCount = attributeCount.split(' ')[0] # get just the number in the sentence

punkAttributes = [] #attributes specific to this CryptoPunk
#append attributes to a list
for attribute in soup.find_all('div', class_="col-md-4"):
    punkAttributes.append(attribute.a.text)
punkAttributes = punkAttributes[1:] #ignore the 0th index as it's not an attribute.

#checking
if int(attributeCount) == len(punkAttributes):
    print('success!')

# most recent sale price
# https://stackoverflow.com/questions/64542519/getting-first-or-a-specific-td-in-beautifulsoup-with-no-class
# foruth column represents price, and we want the most recent price so select 0th index. alternatively, use select_one
details = soup.select("tr.punk-history-row-sold td:nth-of-type(4)")[0]
salePrice = details.text

# recent offer price
details = soup.select("tr.punk-history-row-offer td:nth-of-type(4)")[0]
offerPrice = details.text

# recent bid price
details = soup.select("tr.punk-history-row-bid td:nth-of-type(4)")[0]
bidPrice = details.text
#print(salePrice, offerPrice, bidPrice)

# append to lists
ids.append(id)
types.append(type)
attributeCounts.append(attributeCount)
attributes.append(punkAttributes)
sales.append(salePrice)
offers.append(offerPrice)
bids.append(bidPrice)

# Create Dataframe
cryptoPunks = pd.DataFrame({'ID': ids,
                            'Type': types,
                            'Attributes': attributes,
                            'Attribute Count': attributeCounts,
                            'Recent Sale Price': sales,
                            'Recent Offer': offers,
                            'Recent Bid': bids})

print(cryptoPunks)