

from telegram.ext import Updater
from telegram.ext import CallbackContext

def basado(update: Updater ,context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="soy un bot basadisimo")

def start(update: Updater ,context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="empecemos la marcha")

COMAND_DIC = {"start":start, "basado":basado}