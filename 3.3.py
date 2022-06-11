# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 10:51:10 2022

@author: 077619
"""

# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print("Output is: ")
   print(arg1)
   for aq in vartuple:
      print(aq)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50, "a" )