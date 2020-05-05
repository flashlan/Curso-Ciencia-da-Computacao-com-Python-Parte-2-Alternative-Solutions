# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:14:09 2020

@author: pcstream
"""

# na tabela ascii maiusculas --> 65 a 90
def  maiusculas(frase):
    lista = ''
    for i in frase:
        leu = ord(i)
        #read frase
        if leu >= 65 and leu <= 90:
            lista += i
    return lista 