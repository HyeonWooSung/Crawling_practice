#!/usr/bin/env python
# coding: utf-8

# In[8]:


from bs4 import BeautifulSoup
import urllib.request as req
import datetime

url = "https://finance.naver.com/marketindex/"
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

res = req.urlopen(url).read()

soup = BeautifulSoup(res,'html.parser')

currency = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value")

print("Date : " + now + " USD: " + currency.string)



# In[2]:


print(datetime.datetime.now())


# In[24]:


from bs4 import BeautifulSoup
ex1 = '''
<html>
    <head>
        <title> 연습용 </title>
    </head>
    <body>
        <p align="center">첫번째 텍스트입니다.</p>
        <p align="right">두번째 텍스트입니다.</p>
        <p align="left">세번째 텍스트입니다.</p>
    </body>
</html>
'''

soup = BeautifulSoup(ex1, 'html.parser')
print('find_all :',soup.find_all(text='center'))
print('findAll :', soup.findAll('p'))

