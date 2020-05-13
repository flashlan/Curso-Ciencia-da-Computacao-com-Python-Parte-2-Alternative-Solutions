# -*- coding: utf-8 -*-
"""
Created on Tue May 12 23:27:33 2020
@author: pcstream

"""

# Para testar por pytest é preciso do sufixo "test_" tanto no nome da função
# quanto no nome do arquivo


import bhaskara_classe
import pytest

class TestBhaskara:
    
    @pytest.fixture
    def b(self):
        return bhaskara_classe.bhaskara()

    def test_uma_raiz(self, b):
            assert b.retorna_raizes(1,0,0) == (1,0)       
            
    def test_duas_raizes(self, b):
        assert  b.retorna_raizes(1,-5, 6) == (2,3,2)
        
    def test_zero_raizes(self, b):
        assert  b.retorna_raizes(10,10,10) == (0)
        
        
        ''' Antes da fixture   
    def test_uma_raiz(self):
        b = bhaskara_classe.bhaskara()
        assert b.retorna_raizes(1,0,0) == (1,0)
'''