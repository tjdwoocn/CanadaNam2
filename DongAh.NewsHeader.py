import requests
import bs4 as bs
import urllib.request
import pandas as pd

sauce = urllib.request.urlopen('http://news.donga.com/Politics').read()

soup = bs.BeautifulSoup(sauce, 'lxml')
for div in soup.find_all('span', class_='tit'):
    print(div.text)                #div 태그에 있는 모든 텍스트들을 찾아줌



