# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:23:12 2020

@author: pcstream
"""

lista= [1,2,3,4,5,6,7,8,9]

def busca(lista, elemento):
    primeiro = 0
    ultimo = len(lista) -1
    
    while primeiro <= ultimo:
        meio = (primeiro + ultimo)//2
        if lista[meio] == elemento:
            print(meio)
            return meio
        else:
            if elemento < lista[meio]:
                ultimo = meio -1
                print(meio)
            else:
                primeiro = meio +1
                #return meio
                print(meio)
    
    return False