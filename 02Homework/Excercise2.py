#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 18:17:04 2018

@author: David
"""
#%%

#from functools import reduce

#def create_product(name,price):
 #   return {"name":name, "price":price}

def create_product(name,price):
    return {"name":name, "price":price}

def print_cart(cart):
    print("Checkout:")
    for item in cart:
        print(item["name"], "price:", item["price"])
    print("Total price:", checkout(cart))
        
def checkout(cart):
    
    
    
    total = 0
    insurance_added = False
    priority_mail_added = False
    
    for item in cart:
        if item["name"] == "Insurance":
            if not insurance_added:
                total =  total + item["price"]
                insurance_added = True            
        elif item["name"] == "Priority mail":
            if not priority_mail_added:
                total =  total + item["price"]
                priority_mail_added = True        
        else:
            total = total + item["price"]
    
    return total
            


################

#def add_to_inventory (inventory,product):
#    return inventory + [product]

guitar = create_product ("Guitar",1000)
pick_box = create_product ("Pick box", 5)
guitar_strings = create_product ("Guitar strings",10)
insurance = create_product ("Insurance",5)
priority_mail = create_product ("Priority mail",10)

cart = [guitar,insurance,priority_mail,insurance, priority_mail]
print_cart(cart)





#cart_2= add_to_inventory (inventory_1,cart_2)


#inventory = [
#        {"name": "Guitar",
#        "price": 1000}, 
#        {"name": "Pick box",
#        "price": 5},
#         {"name": "Guitar strings",
#        "price": 10}
#        ]