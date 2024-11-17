from art import tprint
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()
button = KeyboardButton(text= 'Рассчитать норму калорий')
button2 = KeyboardButton(text= 'Информация о боте')
kb.row(button, button2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands= ['start'])
async def start(message):
    await message.answer('Привет!', reply_markup = kb)

@dp.message_handler(text='Рассчитать норму калорий')
async def set_age(message):
    await message.answer('Введите свой возраст: ')
    await UserState.age.set()

@dp.message_handler(text='Информация о боте')
async def info(message):
    await message.answer('Я бот-помощник! Помогу расчитать твою дневную норму калорий \U0001F970')

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост: ')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    growth = await state.get_data()
    await message.answer('Введите свой вес: ')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer(
        f'Ваша дневная норма калорий: {10 * int(data["weight"]) + 6.25 * int(data["growth"]) + 5 * int(data["age"]) + 5} \U00002764')
    await state.finish()

@dp.message_handler()                          # реагирует на все
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение')


if __name__ == '__main__':
    tprint('<<KEYBOARD>>', 'bulbhead')
    executor.start_polling(dp, skip_updates=True)