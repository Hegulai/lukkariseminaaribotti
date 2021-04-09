# encoding: utf-8
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

def start(update, context):
    text = "ok"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    return

def logMessage(update,context):
    print(update.message.text)
    return

def main():
    token = os.environ.get('TOKEN')

    updater = Updater(token=token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.all, logMessage))

    updater.start_polling()
    print("start")
    updater.idle()


if __name__ == '__main__':
    main()
