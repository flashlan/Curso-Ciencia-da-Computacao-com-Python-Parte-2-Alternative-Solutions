# -*- coding: utf-8 -*-
"""
Created on Wed May  6 00:39:24 2020

@author: pcstream

Escreva uma função separa, que recebe um string texto e um 
caractere separador. A função “corta” o texto nos separadores,
 retornando uma lista com as palavras do texto. Exemplo: para o
 texto: ”,1,,2,3,” a saída deve ser a lista: 
     [‘’, ‘1’, ‘’, ‘2’, ‘3’, ‘’] onde ‘’ indica uma palavra 
     vazia (entre 2 separadores consecutivos).
"""
def separa(texto, sep):
     saida = texto.split(sep)
     return saida
 
if __name__ == '__main__':
    texto = ',1,,2,3,'
    print(separa(texto, ','))
