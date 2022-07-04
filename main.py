import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Accept-Language': 'en-US, en;q=0.5'
}

queries = ["vibrator"]
# random page number between 1 and 10

search_query = 'zep'.replace(' ', '+')
print(search_query)
base_url = 'https://www.amazon.com/s?k={0}'.format(search_query)
print(base_url)
#%%
