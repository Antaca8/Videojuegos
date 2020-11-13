# -*- coding: utf-8 -*-
'''
Created on 30-oct-2020

@author: practica
'''
#Fórmula = (aciertos * 10) / M - (errores * 10)/ (50 - M)
def calcular_nota(num_aciertos, num_errores, total_correctas):
    return ((num_aciertos*10)/total_correctas) - ((num_errores * 10)/ (50 - total_correctas))

if __name__ == "__main__":
    aciertos = int(input("Cuál es el número de aciertos?\n")) 
    errores = int(input("Cuál es el número de errores?\n"))
    num_correctas = int(input("Cuál es el número de respuestas correctas?\n"))
    nota = calcular_nota(aciertos,errores,num_correctas)
    print("Su nota es", nota)
