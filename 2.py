# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x = 50

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')
    
    
if 'f' in 'foo': print('1'); print('2'); print('3')
    
hargaBuku = 20000
hargaMajalah = 5000
JumlahBeli = 3
TotalBeli = hargaBuku * JumlahBeli
uang = 2000

if uang > hargaBuku:
    print("beli buku")
elif uang > hargaMajalah:
    print("beli majalah")
else:
    print("uang tidak cukup")