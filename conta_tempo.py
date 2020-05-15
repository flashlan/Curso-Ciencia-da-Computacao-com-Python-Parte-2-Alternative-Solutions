# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:14:46 2020

@author: pcstream
"""
import random
import ordenador
import time


class ContaTempos:
    def lista_aleatoria(self,n):
        lista = [0 for x in range(n)]
        for i in range(n):
            lista[i] = random.randrange(1000)
        return lista
    
    
    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]
        
        o = ordenador.Ordenador()
        
        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print("bolha demorou", depois - antes,"segundos")
        
        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("selecao direta demorou", depois - antes,"segundos")
        
    
    
        
        