#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:58:52 2018

@author: cocoa
"""
import os
import ast

 


#chose menu
def menu():
    os.system('cls')
    print('account and password management system')
    print('-------------------------------------------')
    print('1. please enter account、password')
    print('2. display account 、password')
    print('3. edit password')
    print('4. delete account 、password')
    print('0. exit')
    print('-------------------------------------------')

#get account dictionary data
def readData():
    if not os.path.exists('password.txt'):
        with open('password.txt','w',encoding = 'UTF-8-sig') as f:
            print (os.path.abspath('password.txt'))
#        path = os.path.abspath('.')
#        os.    (path + 'password.txt')
    with open('password.txt','r',encoding = 'UTF-8-sig') as f:
        filedata = f.read()
        if filedata != '':
            data = ast.literal_eval(filedata)
            return data
        else:
            return dict()
    
#input account and password
def input_data():
    while True:
        name = input('please enter account (input ‘enter’ to stop write):\n')
        if name == '':
            break
        if name in data:
            print(name+' account already have!')
            continue
        password = input('please enter password:\n')
        data[name] = password
        with open('password.txt','w',encoding = 'UTF-8-sig') as f:
            f.write(str(data))
        print(name+' account create success')
        
#display account and password
def display_data():
    print('account\tpassword')  
    print('===============================')
    for key in data:
        print(key+'\t'+data[key])
    print('===============================')
    input('Press any button to return main menu')
    
#edit password
def edit_data():
    while True:
        name = input('please enter the account to be modified（input ‘enter’ to stop edit）:\n')
        if name == '':
            break
        if not name in data:
            print('account {} not found!'.format(name))
            continue
        originalPwd = input('please enter the original password:\n')
        if originalPwd == data[name]:
            print('original password is'+ originalPwd)
            newPwd = input('please enter new password:\n')
            data[name] = newPwd
            print('new password is' + newPwd)
            with open('password.txt','w',encoding = 'UTF-8-sig') as f:
                f.write(str(data))
                input('password has changed，press any button to return main menu')
                break
        else:
            print('original password error!')
    
#delete account imformation
def delete_data():
    while True:
        name = input('please enter the account to be delete(input ‘enter’ to stop ):\n')            
        if name == '':
            break
        if not name in data:
            print('account {} not found!'.format(name))
            continue
        password = input('please enter password:\n')
        if password == data[name]:
            print('confirm delete {} data'.format(name))
            yn = input('(Y/N)?')
            if(yn == 'Y' or yn == 'y'):
                del data[name]
                with open('password.txt','w',encoding = 'UTF-8-sig') as f:
                    f.write(str(data))
                    input('account deleted,press any button to return main menu')
                    break
        else:
            print('password error')
        
            
#main program
data = {}
data = readData() #读取文件
while True:
    menu()
    type = int(input('please enter your choice:'))
    print()
    if type == 1:
        input_data()
    elif type == 2:
        display_data()
    elif type == 3:
        edit_data()
    elif type == 4:
        delete_data()
    else:
        break
print('program execution')
    
