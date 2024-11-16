from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ''
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

@dp.message_handler(text = ['Urban'])           # на какое сообщение реагировать
async def urban_message(message):
    print('Urban message')

@dp.message_handler(commands= ['start'])        # на какую команду после / реагировать
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью')

@dp.message_handler()                          # реагирует на все
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)