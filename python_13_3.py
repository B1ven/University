from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
import aioTeleBot


bot = Bot(token=aioTeleBot.api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    text = f'Привет, {message.from_user.username}! Я бот помогающий твоему здоровью.'
    await message.answer(text)


@dp.message_handler()
async def all_message(message):
    text = 'Введите команду /start, чтобы начать общение.'
    await message.reply('Урааааа! Со мной говорят!')
    await message.answer(text)
    # print(f'Получили сообщение {message}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
