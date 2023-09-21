import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import sqlite3
from plugins.ban import blocked
from plugins.unban import unblocked
from content.text import text
from content.other import other
from plugins.everyone_message import message_everyone

# Define the add_user function
def add_user(user_id, username):
    # Implement your logic for adding users to the database here
    pass

def create_db_new():
    db = sqlite3.connect('users.db', check_same_thread=False)
    sql = db.cursor()
    sql.execute('''CREATE TABLE IF NOT EXISTS USERS(
        user_id INTEGER,
        first_name VARCHAR,
        messageid INT,
        message VARCHAR)''')
    sql.execute('''CREATE TABLE IF NOT EXISTS blocked(
        user_id INT)''')
    sql.execute('''CREATE TABLE IF NOT EXISTS user(
        user_id INT)''')
    sql.close()
    db.close()

create_db_new()

import config
bot = telebot.TeleBot(config.TOKEN)

# Sticker ID to be sent when the user starts the bot
start_sticker_id = "CAACAgUAAxkBAAEJ3rdkx-mv7czAKR0AAR_OcrzAvG838cAAAucLAAIUT0FWDj56XbQhG4UvBA"

@bot.message_handler(commands=['start'])
def start2(message):
    # Send the sticker
    bot.send_sticker(message.chat.id, start_sticker_id)

    # Send image by URL and use the start variable in the caption
    image_url = "https://justpaste.it/img/small/279b70b0a58f94a0228979a8087f7ea7.jpg"  # Replace with the actual image URL
    caption = (
        "𝐖𝐞 𝐒𝐭𝐫𝐢𝐜𝐭𝐥𝐲,\n"
        "        𝗱𝗼𝗻'𝘁 𝗮𝗹𝗹𝗼𝘄 𝘁𝗼 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝘀𝘁𝘂𝗱𝘆 𝗺𝗮𝘁𝗲𝗿𝗶𝗮𝗹 𝗮𝗻𝗱 𝗺𝗼𝘃𝗶𝗲𝘀 . "
        "𝗜𝗳 𝘆𝗼𝘂 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝘄𝗶𝘁𝗵𝗼𝘂𝘁 𝗯𝗼𝘁 𝗼𝘄𝗻𝗲𝗿 𝗽𝗲𝗿𝗺𝗶𝘀𝘀𝗶𝗼𝗻 𝘆𝗼𝘂 𝘄𝗶𝗹𝗹 𝗱𝗶𝗿𝗲𝗰𝘁𝗹𝘆 𝗯𝗮𝗻 𝗳𝗿𝗼𝗺 𝗯𝗼𝘁"
        + (message.text.split(' ', 1)[1] if len(message.text.split(' ', 1)) > 1 else '')
    )
    bot.send_photo(message.chat.id, image_url, caption=caption)

# Define start3 function outside of start2 handler
@bot.message_handler(commands=["start3"])
def start3(message):
    id = message.from_user.id 
    user_name = '@' + message.from_user.username if message.from_user.username else None 
    add_user(id, user_name) 
    bot.reply_audio(message.chat.id, audio=f"https://dl.sndup.net/hp75/How%20To%20Download%20Restricted%20Photo%20and.mp3", caption=f"""𝗦𝗲𝗻𝗱 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗢r 𝗚𝗿𝗼𝘂𝗽 𝗟𝗶𝗻𝗸 . \n𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐑𝐞𝐬𝐭𝐫𝐢𝐜𝐭𝐞𝐝 𝐏𝐡𝐨𝐭𝐨 𝐚𝐧𝐝 𝐕𝐢𝐝𝐞𝐨\n\n@adult_updates""", reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "ɪɴᴠɪᴛᴇ ᴀɴᴅ ɢᴇᴛ ᴠɪᴘ ᴀᴄᴄᴇꜱꜱ 🗝️🔐", url=f"https://telegram.me/share/url?url=https://t.me/save_all_file_bot?start=1521651151")
            ]
       ]
    ))
# Rest of your code remains the same

@bot.message_handler(commands=["ban"])
def bloc(message):
    blocked(message)

@bot.message_handler(commands=["unban"])
def some(message):
    unblocked(message)

@bot.message_handler(commands=["admin_message"])
def reklama(message):
    if message.chat.id == config.main_id:
        bot.send_message(message.chat.id, "your message to be sent: ")
        bot.register_next_step_handler(message, textrek)
    else:
        pass

def textrek(message):
    message_everyone(message)

@bot.message_handler(content_types=['text'])
def tex(message):
    text(message)

# photo, sticker, video
@bot.message_handler(content_types=['photo', 'sticker', 'video', 'audio', 'voice', 'location', 'animation', 'contact', 'document', 'dice', 'poll'])
def other2(message):
    other(message)

# Add your bot.polling() here
bot.polling(none_stop=True)
