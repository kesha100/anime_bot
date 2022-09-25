from aiogram import types, Dispatcher
from config import bot, dp
import time


# @dp.message_handler()
# async def echo_square(message: types.Message):
#
#     if message.text.isdigit():
#         square = int(message.text) ** 2
#         await bot.send_message(message.chat.id, square)
#
#     else:
#         await bot.send_message(message.chat.id, message.text)
#
#     if message.text.startswith('!'):
#         await bot.pin_chat_message(message.chat.id, message.message_id)
#

async def timer(message: types.Message):
    # sec = int(message.text)
    # ty_res = time.gmtime(sec)
    ty_res = time.gmtime(int(message.text[1::]))
    res = time.strftime('%H:%M:%S', ty_res)
    if int(message.text[1::]) > 359999:
        await bot.send_message(message.from_user.id, 'i am not a fucking calculator, use your own brains!')
    else:
        if message.text.startswith('='):
            await bot.send_message(message.from_user.id, res)


def register_handlers_extra(dp: Dispatcher):
    # dp.register_message_handler(echo_square)
    dp.register_message_handler(timer)

