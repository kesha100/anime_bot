from aiogram import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
from aiogram import types
import random


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

    photo = open('media/megumi.jpeg', 'rb')
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


async def send_meme(message: types.Message):
    photos = [
        'media/meme3.jpeg',
        'media/meme4.jpeg'
    ]
    photo = open(random.choice(photos), 'rb')
    await bot.send_message(message.chat.id, 'me doing homework:')
    await bot.send_photo(message.chat.id, photo)


async def dice_game(message: types.Message):
    await bot.send_message(message.chat.id, 'gamer 1 is bot')
    await bot.send_message(message.chat.id, 'gamer 2 is you')
    gamer1 = await bot.send_dice(message.chat.id, emoji='🎲')
    gamer2 = await bot.send_dice(message.chat.id, emoji='🎲')
    if gamer1.dice.value > gamer2.dice.value:
        await bot.send_message(message.chat.id, 'winner is gamer 1')
    elif gamer1.dice.value == gamer2.dice.value:
        await bot.send_message(message.chat.id, "winner is 'friendship")
    elif gamer2.dice.value > gamer1.dice.value:
        await bot.send_message(message.chat.id, 'winner is gamer2')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(send_meme, commands=['meme'])
    dp.register_message_handler(dice_game, commands=['dice'])