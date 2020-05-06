# -*- coding: utf-8 -*-
"""
Created on Wed May  6 00:59:38 2020

@author: pcstream
"""

from separa import separa as sep

def maiorpalavra(text):
    maior = ""
    desmenb = sep(text, ',')
    for i in desmenb:
        if len(i) > len(maior):
            maior = i
    return maior
        
    