import aiogram
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import bot


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    age = State()
    gender = State()
    region = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.photo.set()
        await message.answer(f'Hello {message.from_user.first_name} send photo')
        
    else:
        await message.answer('Write to ls')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['username'] = f'@{message.from_user.username}'
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer('WHat is your name?')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("How old are you?")


async def load_age(message: types.Message, state: FSMContext):
    try:
        if int(message.text) < 1950 or int(message.text) > 2015:
            await message.answer('u can come')
        else:
            async with state.proxy() as data:
                data['age'] = 2022 - int(message.text)
            await FSMAdmin.next()
            await message.answer('Which gender?')
    except:
        await message.answer('write digits!')


async def load_gender(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
    await FSMAdmin.next()
    await message.answer('Which region?')


async def load_region(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['region'] = message.text
    await FSMAdmin.next()



def register_handlers_fsm_anketa(dp: Dispatcher):
    # dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=['photo'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)