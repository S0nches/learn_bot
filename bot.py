from turtle import up
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename="bot.log", level=logging.INFO)

def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def talk_to_me(update,context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def main():
    mybot = Updater("5353195093:AAEeDW46bdf4C2xlbkpcI71YaPAjouExJro", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

main()    