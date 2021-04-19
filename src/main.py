# encoding: utf-8
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from arvaus import arvauksen_tarkastaja
import commandShell
import arvausStore

TARKASTAJA = None

def start(update, context):
    text = "ok"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    return

def logMessage(update,context):
    user = update.message.from_user
    text = update.message.text + " | " + user.first_name
    if (user.last_name):
        text += " " + user.last_name
    if (user.username):
        text += " @" + user.username
    print(text)
    return

def arvaa(update, context):
    global TARKASTAJA
    user = update.message.from_user
    teksti = update.message.text.split(" ")
    arvaus = " ".join(teksti[1:])

    timestamp = update.message.date
    if TARKASTAJA.on_oikea_arvaus(arvaus):
        arvausStore.add(timestamp.isoformat(), user.username, arvaus)

    viesti_arvaajalle = "Arvaus lähetetty: " + arvaus
    context.bot.send_message(chat_id=update.effective_chat.id, text=viesti_arvaajalle)

    message_to_log = "@" + user.username + ": " + arvaus
    print(message_to_log)
    return

def main():
    global TARKASTAJA
    token = os.environ.get('TOKEN')

    updater = Updater(token=token)
    dp = updater.dispatcher
    # ignore group messages
    dp.add_handler(MessageHandler(Filters.chat_type.groups, lambda a, b : None))

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("arvaa", arvaa))
    dp.add_handler(MessageHandler(Filters.all, logMessage))
    TARKASTAJA = arvauksen_tarkastaja()
    TARKASTAJA.aseta_arvattava('Hyvät Ystävät')
    arvausStore.init()
    updater.start_polling()
    print("start")
    shell = commandShell.commandShell(TARKASTAJA, arvausStore)
    shell.cmdloop()


if __name__ == '__main__':
    main()
