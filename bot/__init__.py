from telethon import TelegramClient, events, Button
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
APP_ID = 2031518
API_HASH = "b2c81aace7412612bd7195438af94dbf"
BOT_TOKEN = "7750087038:AAGjhfBBpEwo9xTcGe0gU6evAH8HsWuHZE8"
OWNER_ID = 1234



bot = TelegramClient('bot', APP_ID, API_HASH).start(bot_token=BOT_TOKEN)

