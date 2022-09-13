from aiogram import types, Dispatcher
from config import bot, dp, ADMINS
import random


async def game(message: types.Message):
    if message.from_user.id in ADMINS and message.text == 'game':
        emojies = [
            '🎲',
            '⚽️',
            '🏀',
            '🎰',
            '🎳',
            '🎯'
        ]
        await bot.send_dice(message.chat.id, emoji=random.choice(emojies))


def register_handlers_admin(dp):
    dp.register_message_handler(game)