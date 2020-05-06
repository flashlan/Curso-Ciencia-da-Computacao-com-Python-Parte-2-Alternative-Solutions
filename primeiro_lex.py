# -*- coding: utf-8 -*-
"""
Created on Tue May  5 20:51:15 2020

@author: pcstream
"""
def primeiro_lex(lista):
    ''' primeiro_lex(lista) --> recebe uma lista de palavras e 
    retorna primeira palavra em ordem lexográfica'''
    lex = '~'
    for word in lista:
        minha = word[0]
        comp = lex[0]
        if ord(minha) < ord(comp):
            lex = word
    return lex
    
    
   
    