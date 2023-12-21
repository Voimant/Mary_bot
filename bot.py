import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import main_handlers, for_menu
import logging
async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(main_handlers.router, for_menu.router)
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())