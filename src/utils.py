import pathlib

def leerToken(file: str):
    """
        Funcion para leer el token, lo busca en la carpeta raiz
        file: es el __file__ desde donde se este leyendo
    """
    path = pathlib.Path(file).parent.absolute
    directorio_token = f"{path}/../token.txt"
    print(f"Fichero a leer [{directorio_token}]")
    lector = open(f"{path}/../token.txt")
    token = lector.readline()
    
    if token == "":
        return None
    
    return token