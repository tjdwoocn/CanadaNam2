import sys
import requests
import bs4 as bs
import urllib.request
import pandas as pd
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage

# sauce = urllib.request.urlopen('http://news.donga.com/Politics').read()
#
# soup = bs.BeautifulSoup(sauce, 'lxml')
#
# print(soup.p)  #first paragraph element
#
# print(soup.find_all('p'))
#
#
# for paragraph in soup.find_all('p'):
#    print(paragraph.text)  #패러그래프 태그 안에 차일드 태그가 포함 되어 있을경우 string으로 불러오면
#                         none으로 뜬다. 그래서 text로 해야 모든 글들이 가져와짐
#
# print(soup.get_text())  #모든 텍스트를 가져와줌
#
# for url in soup.find_all('a'):
#    print(url.get('href'))     #모든 링크들을 가져오기
#
# nav = soup.nav
# print(nav)  #all of navigation bar
#
# for url in nav.find_all('a'):
#    print(url.get('href'))  #all the links finded in
#
# body = soup.body
# for paragraph in body.find_all('p'):               #패러그래프에 있는 모든 결과를 가져옴
#  print(paragraph.text)          # div.text와는 다른 결과
#
#
# for div in soup.find_all('span', class_='tit'):
#    print(div.text)                #div 태그에 있는 모든 텍스트들을 찾아줌
#
# table = soup.table
# table = soup.find('table')   #둘중의 하나의 방법 쓰면 됨
# print(table)
#
# table_rows = table.find_all('tr')
#
# for tr in table_rows:
#    td = tr.find_all('td')
#    row = [i.text for i in td]
#    print(row)
#
# dfs = pd.read_html('https://pythonprogramming.net//parsememcparseface/', header=0)  #data frames
# for df in dfs:
#    print(df)          #판다스를 이용한 데이터프레임 화
#
#

# sauce = urllib.request.urlopen('https://pythonprogramming.net//sitemap.xml').read()
#
# soup = bs.BeautifulSoup(sauce, 'xml')
#
# for url in soup.find_all('loc'):
#     print(url.text)              #사이트맵읨 모든 url만 불러옴

class Client (QWebPage):
   def __init__(self, url):
      self.app = QApplication(sys.argv)
      QWebPage.__init__(self)
      self.loadFinished.connect(self.on_page_load)
   def on_page_load(self):
      self.app.quit()

url = 'https://pythonprogramming.net/parsememcparseface/'
client_response = Client(url)
source = client_response.mainFrame().toHtml()


#sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

js_test = soup.find('p', class_='jstest')
print(js_test.text)



