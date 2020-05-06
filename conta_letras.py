# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:43:45 2020

@author: pcstream

"""

def conta_letras(frase, contar='vogais'):
    ''' conta_letras(frase, contar='vogais' or contar='consoantes')
    -->  recebe como primeiro parâmetro uma string contendo uma frase
    e como segundo parâmetro uma outra string. Quando o segundo 
    parâmetro for definido como "vogais", a função deve devolver
    o numero de vogais presentes na frase. Quando ele for definido
    como "consoantes", a função deve devolver o número de 
    consoantes presentes na frase. '''
    frase = frase.replace(" ","")
    vogal = 0
    consoante = 0
    for char in frase:
        if char in 'aeiou':
            vogal = vogal + 1
        else:
            consoante = consoante + 1
    if contar == 'vogais':
        return vogal
    if contar == 'consoantes':
        return consoante
    
