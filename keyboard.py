from aiogram.types import ReplyKeyboardMarkup

kb_button = ReplyKeyboardMarkup(resize_keyboard=True)
kb_button.add('/help').add('/pogoda')
