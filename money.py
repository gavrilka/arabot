# -*- coding: utf-8 -*-
import requests
import telebot
token = '495756900:AAH8y13cVaP5rgc3b2Bd9AmkmcLY5mr9LFE'  # УКАЖИТЕ ТОКЕН. Например misc.token
bot = telebot.TeleBot(token)

# НАЧАЛО КОДА, КОТОРЫЙ НУЖНО ПЕРЕКОПИРОВАТЬ В ОСНОВНОЙ ФАЙЛ PY
#from money import money

#@bot.message_handler(commands=['money'])
#def moneyCommand(message):
#    money(message)
# КОНЕЦ КОДА, КОТОРЫЙ НУЖНО ПЕРЕКОПИРОВАТЬ В ОСНОВНОЙ ФАЙЛ PY

def money(message):
    if message.text == '/money':
        bot.send_message(message.chat.id,
                         'Dear *' + message.from_user.first_name + '*! choose currency pairs, for example /money USD RUB',
                         parse_mode='Markdown')
    else:
        try:
            text = message.text
            texts = text.split(' ')
            bot.send_message(message.chat.id,
                             'Hello *' + message.from_user.first_name + '*, current currency rate is ' + '*' + str.upper(
                                 texts[1]) + ' *' + 'составляет: ' + '*' + get_money(str.upper(texts[2]),
                                                                                     str.upper(texts[1])) + '*',
                             parse_mode='Markdown')
        except Exception:
            bot.send_message(message.chat.id,
                             'Bro *' + message.from_user.first_name + '*, there is no such pairs, please try again!',
                             parse_mode='Markdown')

def get_money(pair, base): #курс бата к доллару, рублю
    url1 = 'https://api.fixer.io/latest?base=' + base
    api_key = '2c0dc80667b4e31306e88188178d132d'
    response = requests.get(url1).json()
    price = response['rates'][pair]
    return str(price)