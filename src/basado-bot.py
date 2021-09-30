
import os
import sys
from telegram.ext import Updater, CallbackContext
from telegram.ext import CommandHandler
from telegram.ext.dispatcher import Dispatcher
import accionesBot
import utils
import logging
import time
#Constantes

# obtenemos el directorio del fichero ejecutando :0
#file_dir = os.path.dirname(os.path.realpath(__file__))
file_dir = os.path.dirname(os.path.realpath(__file__))
print(f"el directorio es: [{file_dir}]")

# obtenemos el token, se le pasa la ruta del directorio actual
TOKEN = utils.leerToken(file_dir)
print(f"el token rescatado: [{TOKEN}]")
LIST = list()

# obtencion de la configuracion
general_config = None
try:
    general_config = utils.cargarConfiguracionJson(file_dir,"init.json")
    print(general_config)
except Exception as err:
    print("ha sucedido un error")
    print(err)

# generar logger

logger_level = general_config['LOGGER']['level']

logging.basicConfig(filename=f"{file_dir}/../basado.log",level=logger_level)



# funcioncilla que añade los comandillos parametrizados en acciones bot :0
def add_handlers(dispacher:Dispatcher):
    for key, value in accionesBot.COMAND_DIC.items():
        command = CommandHandler(key,value)
        dispacher.add_handler(command)

def add_error_handlers(dispacher:Dispatcher):
    """
        Funcion para añadir los eventos de error
    """
    dispacher.add_error_handler(callback=error_event,run_async=False)

def error_event(update:object,context:CallbackContext):
    logging.error("ha sucedido un error durante la ejecucion del bot")
    logging.error(context.error)
    time.sleep(30)
# fucnion para lanzar el mnu
def menu():
    stop = False
    while not stop:
        print("### MENU ###")
        print(" - recunput recarga to recargar frases")
        print(" - input stop to stop: ")
        input_value = input("que quieres hacer: ")
        if input_value == "stop":
            stop = True
        elif input_value == "recarga":
            accionesBot.recarga_frases(f"{file_dir}/../frases.txt")

def ejecucion_bot(tipo_ejec=""):
    # rescatamos de la config, lo suyo seria hacerlo en otro lado
    context = general_config['CONTEXT']
    print(f"el valor de context es el siguiente{context}")

    updater = Updater(TOKEN,use_context=context)
    dispacher = updater.dispatcher

    # en la primera ejecucion se hace una recarga de las frases
    accionesBot.recarga_frases(f"{file_dir}/../frases.txt")

    # se añaden los listeners
    add_handlers(dispacher)
    
    # se añaden listeners para caso de error  
    add_error_handlers(dispacher)
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
    if TOKEN != None and TOKEN and general_config != None:
        ejecucion_bot(tipo_ejec)



if __name__ == "__main__":
    main()


