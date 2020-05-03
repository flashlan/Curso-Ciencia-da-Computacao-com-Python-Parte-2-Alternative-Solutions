# -*- coding: utf-8 -*-
"""
Created on Fri May  1 12:40:00 2020

@author: pcstream
"""

def dimensoes(matriz):
    ''' (matriz) -->  recebe uma matriz como parâmetro e 
    imprime as dimensões da matriz recebida, no formato iXj'''
    matriz = str(matriz)
    colunas = matriz.count("[") - 1
    linhas  = int((matriz.count(",") + 1) / colunas)
    out = print(str(colunas) + 'X' + str(linhas))
    return out
