# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 19:06:49 2021

@author: Admin
"""
# Program to simulate a simple calculater

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

print('select the operation')
print('1: add /n2: subtract/n 3: multiply/n 4: divide')

while True:
    # taking input from the user
    choice = input('enter choice (1/2/3/4): ')
    
    # check if choice is listed among the operations list
    if choice in ('1','2','3','4'):
        n1 = float(input('Enter first number:'))
        n2 = float(input('Enter second number:'))
        
        if choice =='1':
            print(n1,'+',n2, '=', add(n1,n2))
        elif choice=='2':
            print(n1,'-',n2, '=', subtract(n1,n2))
        elif choice== '3':
            print(n1,'*',n2, '=', multiply(n1,n2))
        elif choice== '4':
            print(n1,'/',n2, '=', divide(n1,n2))
        break
    else:
        print('invalid input')
