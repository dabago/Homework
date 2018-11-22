#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 17:35:09 2018

@author: David
"""
#%% 
"""
My package
"""

#def sumAnotherItemPrice(acc,item):
#    print("Acc so far is", acc)
#    print("processing item", item)
#    return acc+item["price"]

#def checkout(products):
#    return reduce(sumAnotherItemPrice, products, 0)

##### PRIVATE  ####

def create_product(name,price):
    return {"name":name, "price":price}


###### HELP ####
    
def viewCheckout(products):
    
    s = "My checkout contains:"
    for item in products:
        s = s + " " + item["name"] + "." 
    return s


#### PUBLIC ######


def checkout(products):
    
    if products == []:
        return None
    
    total = 0
    for item in products:
        total = total + item["price"]
    return total













#total_2 = checkout (inventory)






#
#
#inventory2 = []
#total2 = checkout(inventory2)
#print("My total2 is", total2)
#
#inventory3 = []


#%%


