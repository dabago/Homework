#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 23:04:50 2018

@author: David
"""

#%%


#def create_product(name,price):
 #   return {"name":name, "price":price}

def create_product(name,price):
    return {"name":name, "price":price}

def print_cart(cart):
    print("Checkout:")
    for item in cart:
        print(item["name"], "price:", item["price"])
    print("Total price:", checkout(cart,tier))
        
    
def normal_discount(tier):
    if tier == "Silver":
        return 0.92
    if tier == "Gold":
        return 0.95
    return 1

def special_discount(tier):
    if tier == "Gold":
        return 0.95
    return 1

    
def checkout(cart,tier):
    
    if cart == []:
        return None
    
    total = 0
    insurance_added = False
    priority_mail_added = False
    
    
    for item in cart:
        
        if item["name"] == "Insurance":
            if not insurance_added:
                total = total + special_discount(tier) * item["price"]
                insurance_added = True
    
        elif item["name"] == "Priority mail":
            if not priority_mail_added:
                total = total + special_discount(tier) * item["price"]
                priority_mail_added = True                    
                
        else:
            total = total + normal_discount(tier) * item["price"]
    
    return total
            


################

#def add_to_inventory (inventory,product):
#    return inventory + [product]

guitar = create_product ("Guitar",1000)
pick_box = create_product ("Pick box", 5)
guitar_strings = create_product ("Guitar strings",10)
insurance = create_product ("Insurance",5)
priority_mail = create_product ("Priority mail",10)

#cart = [guitar,guitar,ins#urance,priority_mail,insurance, priority_mail]
#cart = [guitar, insurance,priority_mail]
#tier = "Gold"
#print_cart(cart)


