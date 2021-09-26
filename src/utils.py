import pathlib
import json
"""
Fichero para las funciones generales que se puedan usar dentro del programa
"""

def leerToken(path: str):
    """
        Funcion para leer el token, lo busca en la carpeta raiz
        file: es el __file__ desde donde se este leyendo
    """
    directorio_token = f"{path}/../token.txt"
    print(f"Fichero a leer [{directorio_token}]")
    lector = open(directorio_token)
    token = lector.readline()
    
    if token == "":
        return None
    
    return token

def cargarConfiguracionJson(file:str, config_file:str):
    """
    Funcion para cargar las configuraciones del programa
    Esta funcion esta preparada para cargarlas desde un Json
    """
    config_file_path = f"{file}/../config/{config_file}"
    config_file_readable = open(config_file_path,"r")
    return json.load(config_file_readable)