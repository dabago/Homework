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
        print("One tier has been created:", self.name, float(self.discount))

class ShoppingCart:
    
    
    def __init__(self,purchaseProduct = [], purchaseService = []):
        self.purchaseProduct = purchaseProduct
        self.purchaseService = purchaseService

    def add_product(self,Product):
        self.purchaseProduct.append(Product)
        
    def add_service(self, service):
        
        print(self.purchaseService)
        if self.can_add_service(service):
            self.purchaseService.append(service)
            print (sp.add_service)
    
    def can_add_service(self, service):
        for purchased in self.purchaseService:
            if purchased.name == service.name:
                return False
        
        return True
    
    def purchase_product(self):
      
        total_product = 0
        for product in self.purchaseProduct: 
            print ("{} ({})".format(product.name,product.price))
            total_product = total_product + product.price
        return total_product
    
        if self.purchase == []:
            return "Empty"
    
    def purchase_service(self):
        
        total_service = 0 
        for service in self.purchaseService:
            print ("{} ({})".format(service.name,service.price))
            total_service = total_service + service.price
        return total_service
#            if service in self.purchaseService:
#                total_service = total_service 
#                return total_service
        if self.purchase == []:
            return "Empty"

    def checkout(self,tier):
        self.tier = tier
       
        if self.tier == "Normal":
            return n.discount*(self.purchase_product() + self.purchase_service())
        
        if self.tier == "Silver":
            return s.discount * (self.purchase_product()) + self.purchase_service()
        
        if self.tier == "Gold":
            return g.discount*(self.purchase_product() + self.purchase_service())
    
        
        


sp = ShoppingCart()


#sp.add_product(Product("Pick box", 5))
#sp.add_product(Product("Guitar",1000))
#sp.add_product(Product("Guitar",1000))
sp.add_product(Product("Guitar",1000))


#sp.add_product(Product("Guitar strings",10))
#sp.add_service(Service("Insurance",5))
sp.add_service(Service("Insurance",5))
sp.add_service(Service("Insurance",5))
#sp.add_service(Service("Delivery",5))
#sp.add_service(Service("Insurance",5))

#sp.add_service(Service("Delivery",5))
#sp.add_service(Service("Insurance",5))

#

n = Tier("Normal",1)
s = Tier("Silver",0.98)
g = Tier("Gold",0.95)

#sp.purchase_service()
#sp.purchase_product()
sp.checkout("Normal")


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

