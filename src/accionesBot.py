import random
from telegram.ext import Updater
from telegram.ext import CallbackContext

frases = list()
frases.append("no siento las piernas")

# metodo para devolver una frase basada aleatoria
def basado(update: Updater ,context: CallbackContext):
    frase = random.choice(frases)
    
    context.bot.send_message(chat_id=update.effective_chat.id, text=frase)

# metodo pos por probar el bot
def start(update: Updater ,context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="empecemos la marcha, señoritas.")

# metodo para recarga de las frases usables
def recarga_frases(fich_frases="./frases.txt"):
    print(f"añadir frases del siguiente fichero [{fich_frases}]")
    frases.clear()
    try:
        fichero = open(fich_frases,"r")
        for linea in fichero:
            frases.append(linea)
            print(f"se encuentra y se añade la siguiente linea[{linea}]")
        fichero.close()
    except OSError as err:
        print(f"oh ha ocurrido un error {err}")

# dicicionario con los comandos, cuando se lanza el bot los carga
COMAND_DIC = {"start":start, "basado":basado}
