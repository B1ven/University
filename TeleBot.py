import telebot
from tkbt import Token
from random import *


bot = telebot.TeleBot(Token)


def check(m):
    chek_random = ('random', 'рандом')
    for i in m:
        if i in chek_random:
            return True
    return False


@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.send_message(message.chat.id, 'Приветствую!')
    text = f'''Твой ник {message.from_user.username}\n
    Я умею складывать твой текст 10 раз\n
    Но! Если увижу слово рандом могу выдать и число\n
    Можешь проверить!'''
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'], func=lambda message: check(message.text.lower().split()))
def num(message):
    num_generation = f'Случайное число: {randint(1, 100)}'
    bot.send_message(message.chat.id, num_generation)


@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text * 10)

if __name__ == '__main__':
    bot.infinity_polling()


