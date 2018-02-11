# -*- coding: utf-8 -*-
import requests
import telebot
token = '495756900:AAGvm2io0-UCK4nopKkLCuPgLXXMqV3H2Xs'  # УКАЖИТЕ ТОКЕН. Например misc.token
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
                         'Дорогой *' + message.from_user.first_name + '*! Укажи какие валюты, например /money USD RUB',
                         parse_mode='Markdown')
    else:
        try:
            text = message.text
            texts = text.split(' ')
            bot.send_message(message.chat.id,
                             'Привет *' + message.from_user.first_name + '*, на текущий момент курс ' + '*' + str.upper(
                                 texts[1]) + ' *' + 'составляет: ' + '*' + get_money(str.upper(texts[2]),
                                                                                     str.upper(texts[1])) + '*',
                             parse_mode='Markdown')
        except Exception:
            bot.send_message(message.chat.id,
                             'Братишка *' + message.from_user.first_name + '*, ты ошибся, таких пар нет, попробуй еще раз!',
                             parse_mode='Markdown')

def get_money(pair, base): #курс бата к доллару, рублю
    url1 = 'https://api.fixer.io/latest?base=' + base
    response = requests.get(url1).json()
    price = response['rates'][pair]
    return str(price)