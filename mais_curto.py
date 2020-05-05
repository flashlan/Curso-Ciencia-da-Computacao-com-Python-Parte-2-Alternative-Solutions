# -*- coding: utf-8 -*-
"""
Created on Sun May  3 22:56:24 2020

@author: pcstream
"""
matriz2 = ['maria', ' josé ', '   PAULO', 'Catarina   ']


def menor_nome(matriz):
    pont = "10000000000000"
    for i in range(len(matriz)):
        m = matriz[i].strip().capitalize()
        if len(m) < len(pont):
            pont = m
        i += i
    return pont
