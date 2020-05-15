# -*- coding: utf-8 -*-
"""
Created on Thu May 14 20:13:48 2020

@author: pcstream
"""

def ordenada(lista):
    ''' retorna True se a lista for ordenada e False caso não seja'''
    listaori = lista[:]
    fim = len(lista)
    for i in range(fim - 1):
        posicao_do_minimo = i
        for j in range(i + 1, fim):
            if lista[j] <  lista[posicao_do_minimo]:
                posicao_do_minimo = j
        lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
    if listaori == lista:
        return True
    else:
        return False