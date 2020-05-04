# -*- coding: utf-8 -*-
"""
Created on Sun May  3 22:56:24 2020

@author: pcstream
"""

matriz2 = ["nome", "marcelo","Äna", "Gilberto", "zé", "Adalberto"]


def mais_curto(matriz):
    pont = "10000000000000"
    for i in range(len(matriz)):
        if len(matriz[i]) < len(pont):
            pont = matriz[i]
        i = i +i
        pont.capitalize().strip()
    return pont
