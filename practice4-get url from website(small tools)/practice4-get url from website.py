#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 16:03:52 2018

@author: cocoa
"""

import os,requests
from bs4 import BeautifulSoup



        
#get url  
def input_url_and_encode(url_string,encode_type):
    url = url_string
    html = requests.get(url)
    html.encoding = encode_type
    sp = BeautifulSoup(html.text,'html.parser')
    links = sp.find_all(['a','img'])
    url_string_all = ''
    for link in links:
        href = link.get('href')
        if href != None and href.startswith('http://'):
            url_string_all += (href + '\n')
            print(href)
    with open('url.txt','w',encoding = 'UTF-8-sig') as f:
        print ('path'+os.path.abspath('url.txt'))
        f.write(url_string_all)


#main program
url_string = input('Please input url:\n')
encoding = input('Please input encode type:\n')
input_url_and_encode(url_string,encoding)