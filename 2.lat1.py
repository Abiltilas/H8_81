# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 15:34:54 2022

@author: 077619
"""

nilai_absen = int(input("Masukkan nilai absen :"))
nilai_absen = nilai_absen * 0.1

nilai_tugas = int(input("Masukkan nilai tugas :"))
nilai_tugas = nilai_tugas * 0.2

nilai_uts = int(input("Masukkan nilai uts :"))
nilai_uts = nilai_uts * 0.3

nilai_uas = int(input("Masukkan nilai uas :"))
nilai_uas = nilai_uas * 0.4


nilai_total = nilai_absen+nilai_tugas+nilai_uts+nilai_uas

print("Nilai akhir : ",nilai_total)

if nilai_total >= 80:
    print("A")
elif nilai_total < 80 >= 70:
    print("B")
elif nilai_total < 70 >= 60:
    print("C")
elif nilai_total < 60 >= 50:
    print("D")
else:
    print("E")


