from aiogram import types
from config import dp, bot
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('NEXT', callback_data='button_call_1')
    markup.add(button_call_1)

    question = 'From which anime is this photo?'
    answers = [
        'Haikyuu',
        'One-Piece',
        'Jujutsu-Kaisen',
        'Tokyo Revengers'
    ]

    photo = open('media/fushiguro megumi.jpeg', 'rb')
    await bot.send_photo(message.chat.id, photo)
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        open_period=10,
        correct_option_id=2,
        explanation='Guess!',
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def quiz_2(call: types.CallbackQuery):
    question = 'From which anime is this character?'
    answers = [
        'Fruits Basket',
        'Free',
        'Haikyuu',
        'Jujutsu-Kaisen'
    ]
    photo = open('media/Anime İcon.jpeg', 'rb')
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


@dp.message_handler(commands=['meme'])
async def send_mem(messages: types.Message):
    photo = open('media/meme3.jpeg', 'rb')
    await bot.send_message(messages.chat.id, 'me doing homework:')
    await bot.send_photo(messages.chat.id, photo)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        square = int(message.text) ** 2
        await bot.send_message(message.chat.id, square)
    else:
        await bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
