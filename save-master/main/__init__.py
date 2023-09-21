#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID: 26670684
API_HASH: 60592bded0f25a9633a8133601f2c779
BOT_TOKEN: 5835400119:AAG05VIHGiaNvefr3DKF4yd8bTAcZLSyxx4
SESSION: AQGMcpgAsYqcXMmEWFXlqySFMJonkct0APT55wrzwW6bPg5LDW03K4cW1yl-39jS9bHy03kDQJHrul8tGWpYfGl48tyks_P1-_U5w5_pfgs9dqXTBIY8lC7lHs7xtX5USyRuc3lz1oKphyy-Rvgl5F8Lf77IRaRg6rz9-47Y0T9dUKUKh9RsuxRiJKFIacqkyUcjRK5jKQCcPYwPH_OpiUpuleqy3QeWjzWSt1sQGtna8Zlo2QXSqPun-13s30RykcZ4DqzE8Ox7hoyh0h5L4ZfFWtwSI2UH3BY7LkWygpWa7z3QsjYUeZsveP4ubnIDz9nspIIEWHsDiJRC-wNkX5H29OexZAAAAAFr1cQ5AA
AUTH: 6104138809
FORCESUB: adult_chatting_groupxx

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
