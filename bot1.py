import bs4
import parser
import telebot
#main variables
TOKEN = "1632439641:AAE-WEigKZktbUOtpp4cC8YwLBPRxjm4HeE"
bot = telebot.TeleBot(TOKEN)

#handlers
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, когда я вырасту, я буду парсить скидки с Али')

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "привет":
        bot.send_message(chat_id, 'Привет, я бот - парсер скидок.')
    else: bot.send_message(chat_id, 'Не Понял')

@bot.message_handler(content_types=['text'])
def text_handler1(message):
    text1 = message.text.lower()
    chat_id = message.chat.id
    if text1 =="Hi":
        bot.send_message(chat_id, 'Привет, я найду Вам выгодные скидки.')


    elif text1 == 'Скидки':
        bot.send_message(chat_id, 'Какие')

    elif text == 'горячие':
        bot.send_message(chat_id, 'Сейчас найду')


    elif text == 'Распродажи есть':
        bot.send_message(chat_id, 'Растродажи есть')


    else:
        bot.send_message(chat_id, 'Простите, я вас не понял ')

bot.polling()
