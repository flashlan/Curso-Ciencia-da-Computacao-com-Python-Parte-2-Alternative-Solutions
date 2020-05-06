# -*- coding: utf-8 -*-
"""
Created on Wed May  6 01:11:38 2020

@author: pcstream

"""
# require separa.py
from separa import separa as sepa 
    

def cria_e_soma(linhas, arquivo = "arquivo.txt"):
    ''' write a file with a list of numbers, line a line, 
    to sumup then'''
    arquivo = "arquivo.txt"
    with open(arquivo, 'w', encoding='utf-8') as arqu:
        for line in range(linhas): # arrumar
            arqu.write(input("Digite a sequencia de numeros para somar na linha separando cada um com um espaço. \n"))
    with open(arquivo, 'r', encoding= 'utf-8') as arq:
        #conteudo = arq.read()
        for line in arq:
            newlist = sepa(arquivo, ' ')
            print(newlist)
            # implementar soma
