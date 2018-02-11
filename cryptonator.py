# -*- coding: utf-8 -*-
import requests
import telebot
token = '495756900:AAGvm2io0-UCK4nopKkLCuPgLXXMqV3H2Xs'  # УКАЖИТЕ ТОКЕН. Например misc.token
bot = telebot.TeleBot(token)

# НАЧАЛО КОДА, КОТОРЫЙ НУЖНО ПЕРЕКОПИРОВАТЬ В ОСНОВНОЙ ФАЙЛ PY
#from cryptonator import crypt

#@bot.message_handler(commands=['crypt'])
#def cryptCommand(message):
#    crypt(message)
# КОНЕЦ КОДА, КОТОРЫЙ НУЖНО ПЕРЕКОПИРОВАТЬ В ОСНОВНОЙ ФАЙЛ PY

def crypt(message):
    if message.text =='/crypt':
        bot.send_message(message.chat.id, 'Дорогой *' + message.from_user.first_name + '*! Укажи какие криптовалюты, например /crypt btc usd', parse_mode='Markdown')
    else:
        try:
            text = message.text
            texts = text.split(' ')
            bot.send_message(message.chat.id, 'Привет *' + message.from_user.first_name + '*, на бирже cryptonator в данный момент курс ' + '*' + str.upper(texts[1]) + ' *' + 'составляет: ' + '*' + get_crypt(str.upper(texts[1]), str.upper(texts[2])) + '*' + '* ' + str.upper(texts[2]) + '*', parse_mode='Markdown')
        except KeyError:
            bot.send_message(message.chat.id,
                             'Братишка *' + message.from_user.first_name + '*, ты ошибся, таких пар нет, попробуй еще раз!',
                             parse_mode='Markdown')
        except Exception as detail:
            detail = detail.args
            bot.send_message(message.chat.id, detail)

def get_crypt(pair, base): #курс криптовалют
    url1 = 'https://api.cryptonator.com/api/ticker/' + pair + '-' + base
    response = requests.get(url1).json()
    price = response['ticker']['price']
    return str(price)
