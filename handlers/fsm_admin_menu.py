import aiogram
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.client_kb import stop_markup
from config import ADMINS
from config import bot
from database import db
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from database.db import sql_command_insert


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private' and message.from_user.id in ADMINS:
        await FSMAdmin.photo.set()
        await message.answer('Send photo of the new food in the menu',
                             reply_markup=stop_markup)
    else:
        await message.answer('Only admins can add new menu!!!')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer('What is the name of this fucking delicious food?')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Description of the food:')


async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.answer('Price of the food?')


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = f'{message.text}$'
        await bot.send_photo(message.from_user.id, data['photo'], caption=f"Name: {data['name']}\n"
                                     f"Description: {data['description']}\n"
                                     f"price: {data['price']}\n")
    await db.sql_command_insert(state)
    await state.finish()
    await message.answer('Thank you for adding new food for the menu! Foods are really даамдуу!')


# async def valid(id):
#     if id in ADMINS:
#         db.sql_command_insert()
#     else:
#         await bot.send_message('only ADMINS can add new menu!')


async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('It has canceled')


async def delete_data(message: types.Message):
    foods = await db.sql_command_all()
    for food in foods:
        await bot.send_photo(message.from_user.id, food[1],
                             caption=f"Name: {food[2]}\n"
                                     f"Description: {food[3]}\n"
                                     f"price: {food[4]}\n",
                             reply_markup=InlineKeyboardMarkup().add(
                                 InlineKeyboardButton(
                                     f'Delete {food[2]}',
                                     callback_data=f'delete {food[2]}'
                                 ))
                                )


async def complete_delete(call: types.CallbackQuery):
    await db.sql_command_delete(call.data.replace('delete ', ''))
    await call.answer(text='Deleted from database', show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)


def register_handlers_fsm_admin_menu(dp: Dispatcher):
    # dp.register_message_handler(cancel_registration, commands=['stop'], state='*')
    dp.register_message_handler(cancel_registration,
                                Text(equals='stop', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=['photo'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(complete_delete, lambda call: call.data and call.data.startswith('delete '))