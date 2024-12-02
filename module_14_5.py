from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import aioTeleBot
from crud_function import *


bot = Bot(token=aioTeleBot.api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Рассчитать калории'),
     KeyboardButton(text='Купить товар')],
    [KeyboardButton(text='Информация')],
    [KeyboardButton(text='Регистрация')]
],
    resize_keyboard=True)


inl = InlineKeyboardMarkup()
inl_button = InlineKeyboardButton(text='Рассчитать норму каллорий', callback_data='сalories')
inl_button1 = InlineKeyboardButton(text='Формула каллорий', callback_data='formula')
inl.add(inl_button, inl_button1)

inl_gender = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Мужчина', callback_data='male'),
     InlineKeyboardButton(text='Женщина', callback_data='fame')],
    ]
)

inl_buy = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Продукт1', callback_data='product_buying'),
     InlineKeyboardButton(text='Продукт2', callback_data='product_buying'),
     InlineKeyboardButton(text='Продукт3', callback_data='product_buying'),
     InlineKeyboardButton(text='Продукт4', callback_data='product_buying')]
])


@dp.message_handler(commands=['start'])
async def start(message):
    text = f'Привет, {message.from_user.first_name}! Я бот помогающий твоему здоровью.'
    await message.answer(text, reply_markup=kb)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegisterUser(StatesGroup):
    name = State()
    age = State()
    email = State()


@dp.message_handler(text=['Регистрация'])
async def add_username(message):
    await message.answer('Введите ваше имя')
    await RegisterUser.name.set()


@dp.message_handler(state=RegisterUser.name)
async def add_userage(message, state):
    await state.update_data(name=message.text)
    await message.answer('Введите свой возраст')
    await RegisterUser.age.set()


@dp.message_handler(state=RegisterUser.age)
async def add_email(message, state):
    await state.update_data(age=message.text)
    await message.answer('Укажите ваш email')
    await RegisterUser.email.set()


@dp.message_handler(state=RegisterUser.email)
async def create_profile(message, state):
    await state.update_data(email=message.text)
    userdata = await state.get_data()
    await message.answer(user_auth(userdata['name'], userdata['age'], userdata['email']))
    await state.finish()


@dp.message_handler(text=['Рассчитать калории'])
async def main_menu(message):
    await message.answer("Выберите опцию", reply_markup=inl)


@dp.callback_query_handler(text='formula')
async def info_calories(call):
    info_text = """Упрощенный вариант формулы Миффлина-Сан Жеора:

для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;
для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.
"""
    await call.message.answer(info_text)
    await call.answer()


@dp.callback_query_handler(text='сalories')
async def set_age(call):
    await call.message.answer('Введите свой возраст')
    await UserState.age.set()
    await call.answer()


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
    await message.answer('Выберите свой пол', reply_markup=inl_gender)


@dp.callback_query_handler(text='male', state=UserState)
async def send_male_calories(call, state):
    data = await state.get_data()
    if ',' in data['weight']:
        data['weight'] = data['weight'].replace(',', '.')
    result_calories = 10 * float(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    await call.message.answer(f'Ваша норма каллорий - {result_calories}\n'
                              f'Формула Миффлина-Сан Жеора – это одна из самых последних формул расчета калорий для '
                              f'оптимального похудения или сохранения нормального веса.')
    await call.answer()
    await state.finish()


@dp.callback_query_handler(text='fame', state=UserState)
async def send_fame_calories(call, state):
    data = await state.get_data()
    if ',' in data['weight']:
        data['weight'] = data['weight'].replace(',', '.')
    result_calories = 10 * float(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) - 161
    await call.message.answer(f'Ваша норма каллорий - {result_calories}\n'
                              f'Формула Миффлина-Сан Жеора – это одна из самых последних формул расчета калорий для '
                              f'оптимального похудения или сохранения нормального веса.')
    await call.answer()
    await state.finish()


@dp.message_handler(text=['Купить товар'])
async def get_buying_list(message):
    list_product = crud_function.get_all_products()
    for i in list_product:
        title, description, price = i[1:]
        text = f'Название: {title} | {description} | Цена: {price}'
        await message.answer(text)
        with open('кот.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки', reply_markup=inl_buy)


@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler()
async def all_message(message):
    text = 'Введите команду /start, чтобы начать общение.'
    await message.reply('Урааааа! Со мной говорят!')
    await message.answer(text)
    print(f'Получили сообщение {message}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

