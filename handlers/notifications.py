# import asyncio
# import aioschedule
# from aiogram import types, Dispatcher
# from config import bot
#
#
#
# async def get_chat_id(message: types.Message):
#     global chat_id
#     chat_id = message.from_user.id
#     await bot.send_message(chat_id=chat_id, text='ok!')
#
#
# async def go_to_sleep():
#     await bot.send_message(chat_id=chat_id, text='Go to sleep!!!')
#
#
# async def wake_up():
#     video = open('media/video.mp4', 'rb')
#     await bot.send_video(chat_id=chat_id, video=video)
#
#
# async def schedule():
#     aioschedule.every().day.at('13:15').do(go_to_sleep)
#     aioschedule.every().day.at('13:15').do(wake_up)
#
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(2)
#
#
# def register_handlers_notifications(dp: Dispatcher):
#     dp.register_message_handler(get_chat_id,
#                                 lambda word: 'напомни' in word.text)

import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text='Alright!')


async def go_to_geektech():
    await bot.send_message(chat_id=chat_id, text='time to go to GeekTech')


async def text_mom():
    await bot.send_message(chat_id=chat_id, text='don\'t forget to write you mom, that you are on the way home after courses')


async def schedule():
    aioschedule.every().monday.at('17:20').do(go_to_geektech)
    aioschedule.every().monday.at('20:10').do(text_mom)

    aioschedule.every().thursday.at('17:20').do(go_to_geektech)
    aioschedule.every().thursday.at('20:10').do(text_mom)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notifications(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'geektech' in word.text)