#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 14:36:41 2018

@author: David
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 13:31:57 2018

@author: David
"""


#%%

inventory = {
		"Guitar" : 1000,
		"Pick box" : 5,
		"Guitar Strings" : 10,
	}

shopping_cart = ["Pick box", "Guitar Strings", "Guitar","Guitar"]

def checkout(shopping_cart):
    
    final_price = 0
    
    if shopping_cart == []:
        return "You have nothing in your car"
        
    else:
    
       for item in shopping_cart:
           final_price = final_price + (inventory[item])
           
    return final_price
        
        
        
    
