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
    if text == "привет" or text =="Hi":
        bot.send_message(chat_id, 'Привет, я бот - парсер скидок.')

    elif text == "какие" or text == "горячие":
        bot.send_message(chat_id, 'Есть такие')


    elif text == "Огромные" or "Распродажи":
        bot.send_message(chat_id, 'Таких много')


    else:
        bot.send_message(chat_id, 'Простите, я вас не понял ')

bot.polling()
