# -*- coding: utf-8 -*-
"""
Created on Sun May 17 21:27:11 2020

@author: pcstream
"""

def encontra_impares(lista):
    print ''.join(["*"]*depth), lista
	if len(lista) == 0:
		return []
	e = lista.pop(0)
	if  not e % 2 == 0: # se impar
		return [e] + encontra_impares(lista) # re-add to list on index 0 
	return encontra_impares(lista)

# for debug
print(encontra_impares([1,7,10,12,16,21,3,9,11]))
    
    
    
    
    
    
