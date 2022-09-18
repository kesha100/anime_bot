import aiogram
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import ADMINS
from config import bot

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private' and message.from_user.id in ADMINS:
        await FSMAdmin.photo.set()
        await message.answer('Send photo of the new food in the menu')
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
    await state.finish()
    await message.answer('Thank you for adding new food for the menu! Foods are really даамдуу!')


def register_handlers_fsm_admin_menu(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=['photo'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
