from config import dp
from aiogram.utils import executor
import logging
from handlers import client, callback, extra, fsm_admin_menu

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
# fsm_anketa.register_handlers_fsm_anketa(dp)
fsm_admin_menu.register_handlers_fsm_admin_menu(dp)
# admin.register_handlers_admin(dp)

extra.register_handlers_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
