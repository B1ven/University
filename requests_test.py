import requests, json
import telebot
import tkbt

bot = telebot.TeleBot(tkbt.Token)


@bot.message_handler(commands=['coffee'])
def send_random_cofee(message):
    url = 'https://coffee.alexflipnote.dev/random.json'
    img_coffee = requests.get(url)
    params = img_coffee.json()
    bot.send_photo(message.chat.id, params["file"])


if __name__ == '__main__':
    bot.infinity_polling()