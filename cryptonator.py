# -*- coding: utf-8 -*-
import requests
import telebot
token = '495756900:AAH8y13cVaP5rgc3b2Bd9AmkmcLY5mr9LFE'  # УКАЖИТЕ ТОКЕН. Например misc.token
bot = telebot.TeleBot(token)

# НАЧАЛО КОДА, КОТОРЫЙ НУЖНО ПЕРЕКОПИРОВАТЬ В ОСНОВНОЙ ФАЙЛ PY
#from cryptonator import crypt

#@bot.message_handler(commands=['crypt'])
#def cryptCommand(message):
#    crypt(message)
# КОНЕЦ КОДА, КОТОРЫЙ НУЖНО ПЕРЕКОПИРОВАТЬ В ОСНОВНОЙ ФАЙЛ PY

def crypt(message):
    if message.text =='/crypt':
        bot.send_message(message.chat.id, 'Dead *' + message.from_user.first_name + '*! Select crypto pair, for example /crypt btc usd', parse_mode='Markdown')
    else:
        try:
            text = message.text
            texts = text.split(' ')
            bot.send_message(message.chat.id, 'Hello *' + message.from_user.first_name + '*, according to cryptonator, current exchange rate of ' + '*' + str.upper(texts[1]) + ' *' + 'is: ' + '*' + get_crypt(str.upper(texts[1]), str.upper(texts[2])) + '*' + '* ' + str.upper(texts[2]) + '*', parse_mode='Markdown')
        except KeyError:
            bot.send_message(message.chat.id,
                             'Bro *' + message.from_user.first_name + '*, you are mistaken, there is no such crypto, try again!',
                             parse_mode='Markdown')
        except Exception as detail:
            detail = detail.args
            bot.send_message(message.chat.id, detail)

def get_crypt(pair, base): #курс криптовалют
    url1 = 'https://api.cryptonator.com/api/ticker/' + pair + '-' + base
    response = requests.get(url1).json()
    price = response['ticker']['price']
    return str(price)
