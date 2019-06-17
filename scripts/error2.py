# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:29:20 2019

@author: pvelarde
"""

a, b = 20, 0

def division(x, y):
    return x/y

def imprime_resultado(x, y):
    resultado = division(x, y)

    print("La division de {} entre {} es {}".format(resultado))

imprime_resultado(a, b)