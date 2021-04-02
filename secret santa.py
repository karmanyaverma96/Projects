# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 22:42:34 2021

@author: Admin
"""



import random
import copy



names = ['shimul', 'anmol', 'sahil', 'manhar', 'karmanya']

def secret_santa(names):
    my_list = names
    choose = copy.copy(my_list)
    result = []
    
    for i in my_list:
        names= copy.copy(my_list)
        names.pop(names.index(i))
        chosen = random.choice(list(set(choose)&set(names)))
        result.append([i,chosen])
        choose.pop(choose.index(chosen))
    print(result)


    

secret_santa(names)


          







    




        
