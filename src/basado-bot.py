
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext.dispatcher import Dispatcher
import accionesBot
import constantesBot

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
        elif input_value == input_value:
            accionesBot.recarga_frases()

# inicio Pavo!!!!
def main():
    updater = Updater(constantesBot.TOKEN,use_context=constantesBot.CONTEXT)
    dispacher = updater.dispatcher

    accionesBot.recarga_frases()

    # se añaden los listeners
    add_handlers(dispacher)

    # se empiezan a aceptar solicitudes
    updater.start_polling()
    
    # aqui """"paramos"""" el programa para poder indicar stop
    # tambien es un menu para otras cosillas pero lo importante
    # es poder parar el programa xD
    menu()

    #se dejan de aceptar solicitudes
    updater.stop()

if __name__ == "__main__":
    main()


