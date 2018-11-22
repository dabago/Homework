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
from functools import reduce

def sumAnotherItemPrice(acc,item):
    print("Acc so far is", acc)
    print("processing item", item)
    return acc+item["price"]

def checkout(products):
    return reduce(sumAnotherItemPrice, products, 0)


def addProduct(acc, item):
    return acc + " " + item["name"] + "."

def viewCheckout(products):
    return reduce(addProduct, products, "My checkout contains:")

#def checkout(products):
#    total = 0
#    for item in products:
#        total = total + item["price"]
#    return total





inventory = [
        {"name": "Guitar",
        "price": 1000}, 
        {"name": "Pick box",
        "price": 5},
         {"name": "Guitar strings",
        "price": 10}
        ]

total_1 = checkout(inventory)

print(viewCheckout(inventory))

print("My total is", total_1)


def create_product(name,price):
    return {"name":name, "price":price}

product_1 = create_product("Insurance",5)
    

print(product_1)
    

products = [create_product("Priority mail",10),]




#total_2 = checkout (inventory)






#
#
#inventory2 = []
#total2 = checkout(inventory2)
#print("My total2 is", total2)
#
#inventory3 = []


#%%


