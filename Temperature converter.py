# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:03:22 2021

@author: Admin
"""

# convert degree to farenheit or Kelvin, or vice versa.

def cel_to_kel(n1):
    return n1 + 273.15

def cel_to_far(n1):
    return (n1 *(9/5)) + 32
def kel_to_cel(n1,text):
    return n1 - 273.15
def kel_to_far(n1):
    return (n1-273.15) *9/5 + 32
def far_to_cel(n1):
    return (n1 - 32) / 1.8
def far_to_kel(n1):
    return (n1-32) * 5/9 + 273.15


print('input the number and its unit ')



while True:
    text = str(input('enter unit of the value to be given:'))
    n1 = float(input('enter the temperature: '))
    if text =='cel':
        print(cel_to_far(n1), 'Farenheit', ' ', cel_to_kel(n1),'Kelvin')
    elif text =='far':
        print(far_to_cel(n1), 'Celcius',' ', far_to_kel(n1),'Kelvin')
    elif text =='kel':
        print(kel_to_cel(n1),'Celcius',' ',kel_to_far(n1),'Farenheit')
    break 


