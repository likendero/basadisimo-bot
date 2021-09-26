
import os
import sys
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext.dispatcher import Dispatcher
import accionesBot
import constantesBot
import utils

#Constantes

# obtenemos el directorio del fichero ejecutando :0
#file_dir = os.path.dirname(os.path.realpath(__file__))
file_dir = os.path.dirname(os.path.realpath(__file__))
print(f"el directorio es: [{file_dir}]")

# obtenemos el token, se le pasa la ruta del directorio actual
TOKEN = utils.leerToken(file_dir)
print(f"el token rescatado: [{TOKEN}]")
LIST = list()
try:
    general_config = utils.cargarConfiguracionJson(file_dir,"init.json")
except Exception as err:
    print("ha sucedido un error")
    print(err)
# funcioncilla que añade los comandillos parametrizados en acciones bot :0
def add_handlers(dispacher:Dispatcher):
    for key, value in accionesBot.COMAND_DIC.items():
        command = CommandHandler(key,value)
        dispacher.add_handler(command)

# fucnion para lanzar el mnu
def menu():
    stop = False
    while not stop:
        print("### MENU ###")
        print(" - unput recarga to recargar frases")
        print(" - input stop to stop: ")
        input_value = input("que quieres hacer: ")
        if input_value == "stop":
            stop = True
        elif input_value == "recarga":
            accionesBot.recarga_frases(f"{file_dir}/../frases.txt")

def ejecucion_bot(tipo_ejec=""):
    updater = Updater(TOKEN,use_context=constantesBot.CONTEXT)
    dispacher = updater.dispatcher

    accionesBot.recarga_frases(f"{file_dir}/../frases.txt")

    # se añaden los listeners
    add_handlers(dispacher)

    # se empiezan a aceptar solicitudes
    updater.start_polling()

    # aqui """"paramos"""" el programa para poder indicar stop
    # tambien es un menu para otras cosillas pero lo importante
    # es poder parar el programa xD
    #solo si no es ejecucion tipo servidor, sino se queda ejecutando hasta kill del sistema :0
    if tipo_ejec != "-s":
        menu()
         #se dejan de aceptar solicitudes
        updater.stop()
   

# inicio Pavo!!!!
def main():
    num_args = len(sys.argv)
    tipo_ejec = ""
    if num_args == 2:
        tipo_ejec = sys.argv[1]
        print(f"tipo de ejecucion introducida [{tipo_ejec}]")
    #empezamos la ejecucion del bot en el caso que el token este bien
    if TOKEN != None and TOKEN:
        ejecucion_bot(tipo_ejec)



if __name__ == "__main__":
    main()


