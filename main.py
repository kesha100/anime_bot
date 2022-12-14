import asyncio

from config import dp, bot
from aiogram.utils import executor
import logging
from handlers import client, callback, extra, fsm_admin_menu, notifications
from database.db import sql_create


async def on_startup(_):
    asyncio.create_task(notifications.schedule())
    sql_create()


client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
fsm_admin_menu.register_handlers_fsm_admin_menu(dp)
# admin.register_handlers_admin(dp)
notifications.register_handlers_notifications(dp)

extra.register_handlers_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
