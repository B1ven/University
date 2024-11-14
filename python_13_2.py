"""
Напишите две асинхронные функции:

    start(message) - печатает строку в консоли 'Привет! Я бот помогающий твоему здоровью.' . Запускается только когда
    написана команда '/start' в чате с ботом. (используйте соответствующий декоратор) all_massages(message) -
    печатает строку в консоли 'Введите команду /start, чтобы начать общение.'. Запускается при любом обращении не
    описанном ранее. (используйте соответствующий декоратор)

Запустите ваш Telegram-бот и проверьте его на работоспособность.
"""
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio, aioTeleBot


bot = Bot(token=aioTeleBot.api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    text = f'Привет, {message.from_user.username}! Я бот помогающий твоему здоровью.'
    await message.answer(text)


@dp.message_handler()
async def all_message(message):
    text = 'Введите команду /start, чтобы начать общение.'
    await message.answer(text)
    print(f'Получили сообщение {message}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
