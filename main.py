from telebot import *

bot = TeleBot("8774780687:AAHlUONg-r6movx_KS8Wr6y1R-BwSR-ptOE")

@bot.message_handler(commands=["start"])
def startCmd(mes):
    bot.send_message(mes.chat.id, "Bot is running")

@bot.message_handler(content_types=["text"])
def textHandler(mes):
    bot.send_message(mes.chat.id, f"some")

bot.polling(non_stop=True, interval=0)