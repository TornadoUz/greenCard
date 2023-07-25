import asyncio
import logging

from aiogram import Bot, Dispatcher, Router, types


from config import (
    TELEGRAM_API_TOKEN, DEBUG_MODE, DB_USERNAME, DB_PASSWORD
)
from handlers import router


async def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    # ... and all other routers should be attached to Dispatcher
    dp.include_router(router)

    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TELEGRAM_API_TOKEN, parse_mode="HTML")
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.getLevelName(DEBUG_MODE))
    asyncio.run(main())
