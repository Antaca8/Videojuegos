# -*- coding: utf-8 -*-
'''
Created on 12 oct. 2020

@author: anton
'''
def lee_audiencias(fichero):
    ''' Lee el fichero de entrada y devuelve una lista de audiencias
    
    ENTRADA: 
       - fichero: nombre del fichero -> str
    SALIDA: 
       - lista de audiencias -> [(int, float)] 

    Cada línea del fichero se corresponde con la audiencia de un programa,
    y se representa con una tupla con los siguientes valores:
        - edición
        - audiencia
    Hay que transformar la entrada (cadenas de caracteres) en valores numéricos
    para que puedan ser procesados posteriormente.
    '''
    audiencias = []
    with open(fichero, encoding='utf-8') as f:
        for linea in f:
            # Separamos la línea en dos usando ',' como delimitador
            edicion, share = linea.split(',')
            # Transformamos los valores str a int y float
            edicion = int(edicion)
            share = float(share)
            # Creamos una tupla
            tupla = (edicion, share)
            # Añadimos la tupla a la lista
            audiencias.append(tupla)
    return audiencias

def calcula_ediciones(audiencias):
    ediciones = []
    ediciones = {ed for ed, _ in audiencias}
    return sorted(ediciones)