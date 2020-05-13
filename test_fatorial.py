# -*- coding: utf-8 -*-
"""
Created on Wed May 13 03:02:36 2020

@author: pcstream
"""

def fatorial(n):
    if n < 0:
        return 0
    i = fat = 1
    while i <= n:
      fat = fat * i
      i += 1
    return fat


import pytest


@pytest.mark.parametrize("entrada, esperado", [
    (0, 1),
    (1, 1),
    (-10, 0),
    (4, 24),
    (5, 120)
    ])
    
def test_fatorial1(entrada, esperado):
    assert fatorial(entrada) == esperado