# -*- coding: utf-8 -*-
"""
Created on Fri May 15 23:53:28 2020

@author: pcstream
"""

def  bubble_sort(lista):
    fim = len(lista)
    for i in range(fim -1, 0 ,-1):
        trocou = False
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True
                print(lista)
        if trocou == False:
            return lista     
    