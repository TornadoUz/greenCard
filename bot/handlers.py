from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from db import store
import keyboards as k

# All handlers should be attached to the Router (or Dispatcher)
router = Router()


@router.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    """
    This handler receive messages with `/start` command.
    It creates user if user starts firstly otherwise do nothing
    """

    full_name = message.from_user.full_name
    telegram_id = message.from_user.id

    store.get_or_create_user(full_name, telegram_id)

    await message.answer("green Card botga xush kelibsiz", reply_markup=k.get_main_keyboard())


# @router.message()
# async def echo_handler(message: types.Message) -> None:
#     """
#     Handler will forward received message back to the sender

#     By default, message handler will handle all message types (like text, photo, sticker and etc.)
#     """
#     try:
#         # Send copy of the received message
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         # But not all the types is supported to be copied so need to handle it
#         await message.answer("Nice try!")
