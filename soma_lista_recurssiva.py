# -*- coding: utf-8 -*-
"""
Created on Sun May 17 19:56:56 2020

@author: pcstream

pop()
recursao

"""

def soma_lista(lista):
    if len(lista) < 1:   # BASE DA RECURSAO
        return 0
    else:
        return lista.pop() + soma_lista(lista)
    
    
print(soma_lista([2,3,4,2,3,4]))
# p q nao depura?

