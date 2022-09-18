from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_button = KeyboardButton('/start')

start_markup = ReplyKeyboardMarkup()
start_markup.add(start_button)
