# -*- coding: utf-8 -*-
'''
Created on 13 nov. 2020

@author: anton
'''
from videojuegos import *

def test_juegos():
    print(VIDEOJUEGOS)
    
def test_num_distribuidoras():
    print(num_distribuidoras(VIDEOJUEGOS))
    
def test_juegos_distribuidoras_anyo():
    juegos = juegos_distribuidora_anyo(VIDEOJUEGOS, "Nintendo", 2011)
    print(juegos)
    
def test_obten_plataforma():
    print(obten_plataformas(VIDEOJUEGOS))
    
def test_filtrar_por_genero():
    juegos = filtrar_por_genero(VIDEOJUEGOS, "Fighting")
    print(juegos)
if __name__ == '__main__':
    VIDEOJUEGOS = lee_juegos("../data/videojuegos.csv")
    
    #test_juegos()
    #test_num_distribuidoras()
    #test_juegos_distribuidoras_anyo()
    #test_obten_plataforma()
    #test_filtrar_por_genero()