from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)


def get_main_keyboard():
    buttons = [
        [KeyboardButton(text="Bot bilan tanishuv")],
        [KeyboardButton(text="Green Card 2023", web_app={
            "url": "https://tornadouz.github.io/greenCard/bot/webapp/index.html"
        })],
        [KeyboardButton(text="Natijalar")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard
