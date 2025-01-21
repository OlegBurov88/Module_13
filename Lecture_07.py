from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = '***'  # ввести api бота
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text="Информация", callback_data='info')
# button2 = KeyboardButton(text="Начало")
kb.add(button)
# kb.add(button2)

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Info')],
        [
            KeyboardButton(text='shop'),
            KeyboardButton(text='donate')
        ]
    ], resize_keyboard=True
)


# kb.row(button, button2)
# kb.insert(button)
# kb.insert(button2)

@dp.message_handler(commands=['start'])
async def starter(message):
    await message.answer("Рады вас видеть!", reply_markup=kb)


@dp.message_handler(commands=['stop'])
async def starter(message):
    await message.answer("Рады вас видеть!", reply_markup=start_menu)


@dp.callback_query_handler(text="info")
async def infor(call):
    await call.message.answer("Информация о боте!")
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
