# -*- coding: utf-8 -*-
"""
Created on Wed May 13 03:47:44 2020

@author: pcstream
"""

class Triangulo:
    #construtor
    def __init__(self, a , b , c):
        self.a = a
        self.b = b
        self.c = c
        
       
    
    def perimetro(self):
        per = (self.a + self.b + self.c)
        return per
    
    
    

    def tipo_lado(self):
        a = self.a
        b = self.b
        c = self.c
        if a == b and a == c:
            return "equilátero" 
        elif a == b or b == c or a == c:
            return "isósceles"
        elif a != b and c or b != a and c or a != c:
            return "escaleno"
   
  
