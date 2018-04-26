#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:57:18 2018
@author: cocoa
"""
import sqlite3
import os


def menu():
    os.system('cls')
    print('account,password management system')
    print('------------------------------------------')
    print('1. input account,password')
    print('2. display account,password')
    print('3. edit password')
    print('4. delete account,password')
    print('0. exit program')
    print('------------------------------------------')


#create account 
def input_data():
    while True:
        name = input('please input account (input \'Enter\' to stop write):\n')
        if name == '':
            break
        sqlstr = 'select * from password where name = "{}"'.format(name)
        cursor = conn.execute(sqlstr)
        row = cursor.fetchone()
        if not row == None:
            print('{} account already exists'.format(name))
            continue
        password = input('please input password:\n')
        sqlstr = "insert into password values('{}','{}');".format(name,password)
        conn.execute(sqlstr)
        conn.commit()
        print(name+' account create success')
            
#display all account        
def display_data():
    cursor = conn.execute('select * from password')
    print('account\tpassword')
    print('==========================')      
    for row in cursor.fetchall():
        print('{}\t{}'.format(row[0],row[1]))
    input('Press any button to return main menu')
            
#edit password
def edit_data():
    while True:
        name = input('please input accout(input \'Enter\' to stp write):\n')
        if name == '':
            break
        sqlstr = 'select *from password where name = \'{}\''.format(name)
        cursor = conn.execute(sqlstr)
        row = cursor.fetchone()
        if row == None:
            print('{} account not found !'.format(name))
            continue
        else:
            print('original password is {}'.format(row[1]))
            password = input('please input new password:\n')
            sqlstr = 'update password set password = \'{}\' where name = \'{}\''.format(password,name) 
            conn.execute(sqlstr)
            conn.commit
            input('password has changed,press any button to return main menu')
            break
            
#delete data()
def delete_data():
    while True:
        name = input('please enter the account to be delete(input \'enter\' to stop):\n')
        if name == '':
            break
        sqlstr = 'select * from password where name = \'{}\''.format(name)
        cursor = conn.execute(sqlstr)
        row = cursor.fetchone()
        if row == None:
            print (name+' account not found')
            continue
        print ('confirm delete {} data'.format(name))
        yn = input('\'(Y/N)?\'')
        if yn == 'y' or yn == 'Y':
            sqlstr = 'delete from password where name = \'{}\''.format(name)
            conn.execute(sqlstr)
            conn.commit()
            input('account delete,press any button to return main menu')
            break
            
        
#main      
            
conn = sqlite3.connect('Sqlite01.sqlite')   

sqlstr = 'create table if not exists password (\'name\' varchar primary key not null,\'password\' varchar )'
conn.execute(sqlstr)
conn.commit()
  
while True:
    menu()
    choice = int(input('please input your choice:\n'))
    print()
    if choice == 1:
        input_data()
    elif choice == 2:
        display_data()
    elif choice == 3:
        edit_data()
    elif choice == 4:
        delete_data()
    else:
        break

conn.close()
print('Program execution ')
    