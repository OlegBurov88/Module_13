from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

api = '***'  # ввести api бота
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    adress = State()


@dp.message_handler(text=['Заказать'])
async def buy(message):
    await message.answer('Отправь нам свой адрес, пожалуйста')
    await UserState.adress.set()


@dp.message_handler(state=UserState.adress)
async def fsm_handler(message, state):
    await state.update_data(first=message.text)
    data = await state.get_data()
    await message.answer(f'Доставка будет отправлена на {data["first"]}')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
