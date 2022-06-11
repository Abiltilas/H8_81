# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 09:57:55 2022

@author: 077619
"""

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print("Values inside the function: ", mylist)
   return mylist

# Now you can call changeme function
mylist = [10,20,30];
mylist = changeme( mylist );
print("Values outside the function: ", mylist)