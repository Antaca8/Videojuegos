# -*- coding: utf-8 -*-
'''
Created on 12 oct. 2020

@author: anton
'''
from audiencias import *

AUDIENCIAS_GH = lee_audiencias('../data/GH.csv')
print(AUDIENCIAS_GH[:20])

AUDIENCIAS_GH_VIP = lee_audiencias('../data/GH_VIP.csv')
print(AUDIENCIAS_GH_VIP[:20])

suma = 0
for edicion, audiencia in AUDIENCIAS_GH:
    print(edicion, "-->", audiencia)
    suma+= audiencia
    
print(suma/len(AUDIENCIAS_GH))

ediciones = calcula_ediciones(AUDIENCIAS_GH)
print(ediciones)

ediciones = calcula_ediciones(AUDIENCIAS_GH_VIP)
print(ediciones)
