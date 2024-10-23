import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import confic
import random
from keyboards import kb1, kb2
from randomfox import fox
from random import randint
API_TOKEN = confic.token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

dp.include_router(career_choice.router)
dp.include_router(common.router)


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Салют! Я эхобот на aiogram 3. Отправь мне любое сообщение и я повторю его",reply_markup=kb1)


@dp.message(Command("fox"))
@dp.message(Command("лиса"))
@dp.message(F.text.lower() == "покажи лису")
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f"Держи лису- {name}")
    await message.answer_photo(photo=img_fox)
    # await bot.send_photo(message.from_user.id, photo=img_fox)

@dp.message(F.text.lower() == "num")
async def send_random (messege: types.Message):
    number = random.randint(1, 10)
    await messege.answer(f"{number}")


#Хендлер на сообщение
@dp.message(F.text)
async def msg_echo(message:types.Message):
     msg_user = message.text.lower()
     name = message.chat.first_name
     if "привет" in msg_user:
        await message.answer(f"Привет-привет - {name}")
     elif "пока" == msg_user:
         await message.answer(f"Пока-пока - {name}")
     elif "ты кто" in msg_user:
         await message.answer(f"Я бот,  - {name}")
     elif "лиса" in msg_user:
         await message.answer(f"Смотри что у меня есть,  - {name}",reply_markup=kb2)
     else:
         await message.answer(message.text)


#@dp.message()
#async def echo(message: types.Message):
# await message.answer(message.text)
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())


