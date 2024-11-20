from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import aioTeleBot

bot = Bot(token=aioTeleBot.api)
dp = Dispatcher(bot, storage=MemoryStorage())


kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
kb.add(button, button2)

inl = InlineKeyboardMarkup()
inlbutton = InlineKeyboardButton(text='Рассчитать норму каллорий', callback_data='сalories')
inlbutton2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formula')
inl.add(inlbutton, inlbutton2)


@dp.message_handler(commands=['start'])
async def start(message):
    text = f'Привет, {message.from_user.first_name}! Я бот помогающий твоему здоровью.'
    await message.answer(text, reply_markup=kb)


class UserState(StatesGroup):
    gender = State()
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer("Выберите опцию", reply_markup=inl)


@dp.callback_query_handler(text='formula')
async def get_formulas(call):
    info_text = """Упрощенный вариант формулы Миффлина-Сан Жеора:

для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;
для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.
"""
    await call.message.answer(info_text)
    await call.answer()


@dp.callback_query_handler(text='сalories')
async def set_gender(call):
    await call.message.answer('Введите Ваш пол М/Ж')
    await call.answer()
    await UserState.gender.set()


@dp.message_handler(state=UserState.gender)
async def set_age(message, state):
    await state.update_data(gender=message.text.lower())
    await message.answer('Введите свой возраст')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост (см)')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес (кг)')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    if ',' in data['weight']:
        data['weight'] = data['weight'].replace(',', '.')
    if data['gender'] == 'м':
        result_calories = 10 * float(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
        await message.answer(f'Ваша норма каллорий для мужчин - {result_calories}\n'
                             f'Формула Миффлина-Сан Жеора – это одна из самых последних формул расчета калорий для '
                             f'оптимального похудения или сохранения нормального веса.')
    elif data['gender'] == 'ж':
        result_calories = 10 * float(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) - 161
        await message.answer(f'Ваша норма каллорий для женщин - {result_calories}\n'
                             f'Формула Миффлина-Сан Жеора – это одна из самых последних формул расчета калорий для '
                             f'оптимального похудения или сохранения нормального веса.')
    await state.finish()


@dp.message_handler()
async def all_message(message):
    text = 'Введите команду /start, чтобы начать общение.'
    await message.reply('Урааааа! Со мной говорят!')
    await message.answer(text)
    print(f'Получили сообщение {message}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
