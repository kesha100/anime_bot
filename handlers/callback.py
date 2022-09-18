from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import dp, bot


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('NEXT', callback_data='button_call_2')
    markup.add(button_call_2)

    question = 'From which anime is this character?'
    answers = [
        'Fruits Basket',
        'Free',
        'Haikyuu',
        'Jujutsu-Kaisen'
    ]
    photo = open('media/free.jpeg', 'rb')
    await bot.send_photo(call.message.chat.id, photo)
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        correct_option_id=1,
        open_period=10,
        type='quiz',
        explanation='It is not Kageyama from Haikyuu, dude'
    )


async def quiz_3(call: types.CallbackQuery):
    question = 'From which anime is this character?'
    answers = [
        'Attack on titan',
        'Haikyu',
        'Hunter x hunter',
        'Evangelion'
    ]
    photo = open('media/hunter.jpeg', 'rb')
    await bot.send_photo(call.message.chat.id, photo)
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        correct_option_id=2,
        open_period=10,
        type='quiz',
        explanation='IF you haven\'t watched it yet, go and watch it!!!'
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text='button_call_1')
    dp.register_callback_query_handler(quiz_3, text='button_call_2')