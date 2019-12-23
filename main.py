# - *- coding: utf- 8 - *-
import config
import os
import misc
import telebot
from telebot import types
from openweathermap import weather
from money import money
from cryptonator import crypt
import logging
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

bot = telebot.TeleBot(config.token)

# Здесь пишем наши хэндлеры
@bot.message_handler(commands=['help'])
def helpCommand(message):
    bot.send_message(message.chat.id, 'Hello *' + message.from_user.first_name + '*!', parse_mode='Markdown')


@bot.message_handler(commands=['weather'])
def weatherCommand(message):
   weather(message)

@bot.message_handler(commands=['money'])
def moneyCommand(message):
   money(message)

@bot.message_handler(commands=['crypt'])
def cryptCommand(message):
   crypt(message)

@bot.message_handler(content_types=['text'])
def handle_text(message):
# Если пользователь отправил "привет, как тебя зовут?" отвечаем "робот я"
    if message.text == "Bunny":
        bot.send_message(message.from_user.id, 'Fuck you TKS')

# Если пользователь отправил "и чо?" отвечаем "да ничо"
    elif message.text == "TKS":
        bot.send_message(message.from_user.id, 'Send us your sandwich')

#Если пользователь отправил слово/фразу, на которое(ую) нет ответа
    # else:
# bot.send_message(message.from_user.id, "Извините, я Вас не понимаю")

# Проверим, есть ли переменная окружения Хероку (как ее добавить смотрите ниже)
# if "HEROKU" in list(os.environ.keys()):
#     logger = telebot.logger
#     telebot.logger.setLevel(logging.INFO)
#
#     server = Flask(__name__)
#     @server.route("/bot", methods=['POST'])
#     def getMessage():
#         bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
#         return "!", 200
#     @server.route("/")
#     def webhook():
#         bot.remove_webhook()
#         bot.set_webhook(url="https://aratestbot.herokuapp.com/") # этот url нужно заменить на url вашего Хероку приложения (стер /bot
#         return "?", 200
#     server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))
# else:
#     # если переменной окружения HEROKU нету, значит это запуск с машины разработчика.
#     # Удаляем вебхук на всякий случай, и запускаем с обычным поллингом.
#     bot.remove_webhook()
bot.polling(none_stop=True)