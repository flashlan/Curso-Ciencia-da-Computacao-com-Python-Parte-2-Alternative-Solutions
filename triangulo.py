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
        if self.a == self.b and self.a == self.c:
            print("Equilátero")
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            print("Isósceles")
        elif self.a != self.b and self.c or self.b != self.a and self.c or self.a != self.c:
            print("Escaleno")
   
  
