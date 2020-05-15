# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:08:45 2020

@author: pcstream
"""

def busca(lista, elemento):
    key = 0 # conta qtas vezes  elemento pareceu na lista
    pos = 0 # indice da aparição
    aqui = 0
    for i in range(len(lista)): 
        #print(elemento,lista[i],i, key,pos,aqui)# poderia ser simples mas eu estava estudando variaveis
        if lista[i] == elemento:
            key += 1
            aqui = pos
            #print(key, aqui)
        pos += 1
    if key > 0:
        return aqui
    else:
        return False
        
    