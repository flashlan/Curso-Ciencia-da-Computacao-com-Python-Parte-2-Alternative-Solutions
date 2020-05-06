# -*- coding: utf-8 -*-
"""
Created on Wed May  6 03:32:03 2020

@author: pcstream
"""

nome = "arquivo_criado.txt"

vezes = 3
#vezes = vezes 

with open(nome, 'w', encoding='utf-8') as arq:
    for line in range(vezes): # arrumar
            
            arq.write(input("Digite a sequencia de numeros para somar na linha separando cada um com um espaço. \n"))
    
with open(nome, 'r', encoding='utf-8') as arq:
    for linha in arq:
        #conteudo = arq.read()
        linhas_em_branco = linha.strip()
        #conteudo = arq.read()
        print(linhas_em_branco)
        # implementar soma dos itens da lista