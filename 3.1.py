# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 09:27:09 2022

@author: 077619
"""
# append itu fungsinya nambahin 1 variabel saja
# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append(1);
   mylist.append(2);
   mylist.append([1,2,3,4]);
   print("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print("Values outside the function: ", mylist)