# -*- coding: utf-8 -*-
'''
Created on 13 nov. 2020

@author: anton
'''
from videojuegos import *

def mostrar_numerado(coleccion):
    i=0
    for p in coleccion:
        i= i + 1
        print(i,p)

def test_juegos():
    print(mostrar_numerado(VIDEOJUEGOS))
    
def test_num_distribuidoras():
    print(num_distribuidoras(VIDEOJUEGOS))

def test_juegos_distribuidoras_anyo():
    distribuidoras_anyo = juegos_distribuidora_anyo(VIDEOJUEGOS, "Nintendo", 2011)
    print(mostrar_numerado(distribuidoras_anyo))

def test_obten_plataforma():
    plataforma = obten_plataformas(VIDEOJUEGOS)
    print(mostrar_numerado(plataforma))

def test_filtrar_por_genero():
    filtro = filtrar_por_genero(VIDEOJUEGOS, "Platform")
    print(mostrar_numerado(filtro))

def test_num_juegos_mas_ventas_JP():
    print(num_juegos_mas_ventas_JP(VIDEOJUEGOS))
    
def test_juego_mas_antiguo():
    juego_antiguo = juego_mas_antiguo(VIDEOJUEGOS)
    print(mostrar_numerado(juego_antiguo))

if __name__ == '__main__':
    VIDEOJUEGOS = lee_juegos("../data/videojuegos.csv")
    
    #test_juegos()
    #test_num_distribuidoras()
    test_juegos_distribuidoras_anyo()
    #test_obten_plataforma()
    #test_filtrar_por_genero()
    #test_num_juegos_mas_ventas_JP()
    #test_juego_mas_antiguo()