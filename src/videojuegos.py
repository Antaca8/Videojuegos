# -*- coding: utf-8 -*-
'''
Created on 13 nov. 2020

@author: anton
'''
import csv

from collections import namedtuple

juego = namedtuple("Juego", "Rank, Name, Platform, Year, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales")

def lee_juegos(fichero):
    juegos=[]
    with open (fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for Rank, Name, Platform, Year, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales in lector:
            Rank = int(Rank)
            Year = int(Year)
            NA_Sales = float(NA_Sales)
            EU_Sales = float(EU_Sales)
            JP_Sales = float(JP_Sales)
            Other_Sales = float(Other_Sales)
            Global_Sales = float(Global_Sales)
            juegos.append(juego(Rank, Name, Platform, Year, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales))
    return juegos

def num_distribuidoras(lista_juegos):
    conj = set()
    for juego in lista_juegos:
        conj.add(juego.Publisher)
    return len(conj)

def juegos_distribuidora_anyo(lista_juegos, publisher, anyo):
    filtro = []
    for juego in lista_juegos:
        if juego.Publisher == publisher and juego.Year == anyo:
            filtro.append(juego.Name)
    return filtro
        
def obten_plataformas(lista_juegos):
    conj = set()
    for _, _, Platform, _, _, _, _, _, _, _, _ in lista_juegos:
        conj.add(Platform)
    return conj

def filtrar_por_genero(lista_juegos, genre):
    filtro = []
    for _, Name, _, _, Genre, _, _, _, _, _, _ in lista_juegos:
        if Genre == genre:
            filtro.append(Name)
    return filtro

def num_juegos_mas_ventas_JP(lista_juegos):
    cont = 0
    for t_juego in lista_juegos:
        if t_juego.JP_Sales > t_juego.NA_Sales:
            cont+=1
    return cont

def juego_mas_antiguo(lista_juegos):
    #return min(juego for juego in lista_juegos, key=lambda juego:juego.Year) #tupla juego 
    anyo_menor = min(juego.Year for juego in lista_juegos)
    return [juego for juego in lista_juegos if juego.Year == anyo_menor]
    
    
    