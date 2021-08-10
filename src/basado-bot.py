
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

# inicio Pavo!!!!
def main():
    updater = Updater(constantesBot.TOKEN,use_context=constantesBot.CONTEXT)
    dispacher = updater.dispatcher
    add_handlers(dispacher)
    updater.start_polling()
    stop = False
    while not stop:
        input_value = input("input stop to stop: ")
        if input_value == "stop":
            stop = True
    updater.stop()

if __name__ == "__main__":
    main()


