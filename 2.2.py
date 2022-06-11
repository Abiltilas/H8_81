# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

hargaBuku = int(input("Masukkan harga buku :"))
hargaMajalah = int(input("Masukkan harga majalah :"))
JumlahBeli = int(input("Mau beli buku berapa banyak? :"))
TotalBeli = hargaBuku * JumlahBeli
uang = int(input("Terus uang lo berapa? :"))

if uang > TotalBeli:
    print("Selamat, lo bisa beli bukunya... ")
else:
    if uang > hargaMajalah:
        print("Yahhh, lo cuma sanggup beli majalan nih..")
    else:
        print("Hehehe...")
    
    