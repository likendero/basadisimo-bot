import random
import os
from telegram.ext import Updater
from telegram.ext import CallbackContext

file_dir = os.path.dirname(os.path.realpath(__file__))
frases = list()
frases.append("no siento las piernas")

# metodo para devolver una frase basada aleatoria
def basado(update: Updater ,context: CallbackContext):
    frase = random.choice(frases)
    
    context.bot.send_message(chat_id=update.effective_chat.id, text=frase)

# metodo para recargar las frases
def recarga(update: Updater ,context: CallbackContext):
    numero = recarga_frases(f"{file_dir}/../frases.txt")
    
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Vaya me has hecho recargar frases, espero que merezca la pena numero de frases {numero}")

# metodo pos por probar el bot
def start(update: Updater ,context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="empecemos la marcha, señoritas.")

# metodo para recarga de las frases usables
def recarga_frases(fich_frases="./frases.txt"):
    numero = 0
    print(f"añadir frases del siguiente fichero [{fich_frases}]")
    frases.clear()
    try:
        fichero = open(fich_frases,"r")
        for linea in fichero:
            frases.append(linea)
            print(f"se encuentra y se añade la siguiente linea[{linea}]")
            numero = numero + 1
        fichero.close()
    except OSError as err:
        print(f"oh ha ocurrido un error {err}")
    return numero

# dicicionario con los comandos, cuando se lanza el bot los carga
COMAND_DIC = {"start":start, "basado":basado,"recarga":recarga}
