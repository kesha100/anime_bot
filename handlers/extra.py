from aiogram import types, Dispatcher
from config import bot, dp



# @dp.message_handler()
async def echo_square(message: types.Message):

    # if message.text.isdigit():
    #     square = int(message.text) ** 2
    #     await bot.send_message(message.chat.id, square)
    #
    # else:
    #     await bot.send_message(message.chat.id, message.text)

    if message.text.startswith('!'):
        await bot.pin_chat_message(message.chat.id, message.message_id)



def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo_square)

