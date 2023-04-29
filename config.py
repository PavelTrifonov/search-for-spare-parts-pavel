from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token='')
storage = MemoryStorage

dp = Dispatcher(bot, storage= storage)