import logging
import asyncio
from aiogram import Bot, Dispatcher
import confic
from handlers import common, career_choice



#@dp.message()
#async def echo(message: types.Message):
# await message.answer(message.text)
async def main():
    API_TOKEN = confic.token

    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    dp.include_router(career_choice.router)
    dp.include_router(common.router)


    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())


