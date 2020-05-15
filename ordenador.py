# -*- coding: utf-8 -*-
"""
Created on Thu May 14 03:12:56 2020

@author: pcstream
"""

class Ordenador:
    
    def selecao_direta(self, lista):
        
        fim = len(lista)
        
        
        for i in range(fim -1):
            posicao_do_minimo = i
            for j in range(i + 1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j
        lista[j], lista[posicao_do_minimo] = lista[posicao_do_minimo],lista[j]
        
        
    def bolha(self,lista):
        fim = len(lista)
        
        for i in range(fim-1, 0 , -1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
            