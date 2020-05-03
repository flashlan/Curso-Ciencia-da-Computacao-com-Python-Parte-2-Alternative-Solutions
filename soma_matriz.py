# -*- coding: utf-8 -*-
"""
Created on Fri May  1 19:47:28 2020

@author: pcstream
"""
'''
def dimensoes(matriz):

    matriz = str(matriz)
    colunas = matriz.count("[") - 1
    linhas  = int((matriz.count(",") + 1) / colunas)
    out = print(str(colunas) + '*' + str(linhas))
    return out
'''


def soma_matrizes(m1,m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return False
    
    i =[] # add colchetes
    for l in range(len(m1)): # para cada item l nas colunas
        i.append([]) # adiciona tantos colchetes dentro do colchtes vazio de i
        for j in range(len(m2[0])): # len(m2[0]) retorna qtdade itens lista e percorre a lista
            i[l].append(m1[l][j] + m2[l][j])
    return i

   
