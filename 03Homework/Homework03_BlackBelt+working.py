#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 15:24:23 2018

@author: David
"""

#%%


class Product:
    
    def __init__(self,name,price):
        self.name = name
        self.price = price
        print("One product has been created:", self.name)
        
    def __str__(self):
        return "{} ({})".format(self.name,self.price)
    
class Service:
    
    def __init__(self,name,price):
        self.name = name
        self.price = price
        print("One service has been created", self.name)

class Tier:
    
    def __init__(self,name,discount):
        self.name = name
        self.discount = discount
        print("One tier has been created", self.name, float(self.discount))

class ShoppingCart:
    
    purchase = []
    
    def __init__(self,purchase = []):
        self.purchase = purchase
#        self.purchase_service = purchase

    def add_product(self,Product):
        self.purchase.append(Product)
        
    def add_service(self,Service):
         self.purchase.append(Service)
    
    def purchase_product(self):
        
        print(self.purchase)
        
        total_product = 0
        for product in self.purchase: 
            print(product.price)
            total_product = total_product + product.price
        return total_product
            
        if self.purchase == []:
            return "Empty"
    
#    def purchase_service(self):
#        total_service = 0
#        for service in self.service: 
#            print(service.price)
#            total_service = total_service + service.price
#        return total_service
#            
#        if self.purchase == []:
#            return "Empty"


            
        
    
#    def checkout(self,tier):
#        
#        for item in purchase:
#            if tier == "Normal"
#            return 
#            
         
    
#    def add_new_product(self,)
        
        


sp = ShoppingCart()

sp.add_product(Product("Pick box", 5))
sp.add_product(Product("Guitar",1000))
#sp.add_product(Product("Guitar",1000))
#sp.add_product(Product("Guitar",1000))


#sp.add_product(Product("Guitar strings",10))
#sp.add_service(Service("Insurance",5))
#
sp.purchase_product()
#sp.purchase_service()



#pick_box = Product("Pick box", 5)
#guitar_strings = Product("Guitar strings",10)
#insurance = Service("Insurance",5)
#priority_mail = Service("Priority mail",10)
#normal = Tier("Normal",1)
#silver = Tier("Silver",0.98)
#gold = Tier("Gold",0.95)

#purchase = [guitar,guitar]

#ShoppingCart.add_product(guitar)

#print(guitar.price)

