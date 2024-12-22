import requests
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup

base_url = 'https://www.yes24.com'
main_url = '/Product/Category/NewProduct?categoryNumber=001&pageSize=24&newProductType=NEW'
url = f'{base_url}{main_url}&pageNumber=1'
# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
# result = requests.get(url, headers=header)
result = requests.get(url)
soup = BeautifulSoup(result.text)

