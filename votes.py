import telebot
from tkbt import Token


bot = telebot.TeleBot(Token)


@bot.message_handler(content_types=['text'])
def get_poll(message):
    if 3 <= message.text.count('\n') <= 11:
        temp = message.text.split("\n")
        question = temp[0]
        ans = temp[1:]
        bot.send_poll(message.chat.id, question, ans)
    else:
        text = 'В вашем сообщении должно быть от 3-х до 11 строк'
        bot.send_message(message.chat.id, text)


if __name__ == "__main__":
    bot.infinity_polling()

