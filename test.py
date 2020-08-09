# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import os
import json
import urllib.request
import urllib.parse
import urllib.error
from urllib.request import urlretrieve

web_url="https://www.google.co.in/search?q=" + "dog" + "&source=lnms&tbm=isch"
header={
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
            
            }
request=urllib.request.Request(web_url,headers=header)
response = urllib.request.urlopen(request)
responseData = response.read()
html = bs(responseData, 'html.parser')

for a in html.find_all("div", {"class": "rg_meta"}):
    print(a)


