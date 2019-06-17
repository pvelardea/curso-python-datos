# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 21:59:55 2019

@author: pvelarde
"""
from IPython import get_ipython
get_ipython().magic('reset -f')

lista = list(range(1000))
#r=range(1000)
#lista=[*r]
suma=0
for i in lista:
 suma += i
print ("La suma es:",suma)