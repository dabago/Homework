#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 02:13:33 2018

@author: David
"""

#%%

#%%
def calculate_volume_cylinder (radius, height):
    import math 
    return float(height) * (float(radius)** 2) * math.pi


#%%
def calculate_volume_sphere (radius):
    import math
    return (float(radius)**3) * math.pi * (4/3)


#%% Ex. 2 Investigate how to create histograms using the matplotlib library.  
##Create a function that uses the matplotlib library to plot the histogram 
##of the grade distribution in an imaginary IE class with 100 students.  
## Remember that there are 15% pass, 35% proficiency, 35% excellence, and 15% honors in a class.

import matplotlib.pyplot as plt
#
#n, bins, patches = plt.hist(x=[15, 35, 35, 15],bins=5, color='blue',
#                            alpha=5, rwidth=5)
grades = ["pass", "proficiency", "excellence", "honors"]

#plt.title("Grade distribution")
#plt.xlabel('Students')
#plt.ylabel('Grades')
#plt.show()

plt.bar(grades,[15, 35, 35, 15])



#%%

