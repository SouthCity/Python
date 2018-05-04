#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 16:10:30 2018

@author: cocoa
"""
import requests,re,os 

 #get email address
def input_website(url_string):
    url_regex = re.compile('(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]')
    if url_regex.match(url_string) != None :
        regex = re.compile('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+')
        html = requests.get(url_string)
        #html.encoding = 'GBK'
        emails = regex.findall(html.text) 
        with open('email.txt','w',encoding = 'UTF-8-sig') as f:
            print ('path'+os.path.abspath('email.txt'))
            f.write('\n'.join(emails))
            os.system('notepad python.txt')   
            for email in emails:
                print(email)
    else:
        print('url error')
    

#main program
url_string = input('Please input url:\n')
input_website(url_string)



