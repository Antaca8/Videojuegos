# -*- coding: utf-8 -*-
'''
Created on 13 nov. 2020

@author: anton
'''
import csv

def lee_juegos(fichero):
    juegos=[]
    with open (fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for juego in lector:
            juegos.append(juego)
        return juegos
            
            
def test_juegos():
    mostrar = lee_juegos("../data/videojuegos.csv")
    print(mostrar)
    
test_juegos()
            