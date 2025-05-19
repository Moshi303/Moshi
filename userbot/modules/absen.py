from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton)
from datetime import datetime
import pytz

from userbot import *

__MODULE__ = "ᴀʙsᴇɴ"
__HELP__ = """
❏──「ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ  ᴀʙsᴇɴ」──❏"
<blockquote>➢ ᴘᴇʀɪɴᴛᴀʜ: <code>abs</code>
  ➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ: <u>ᴜɴᴛᴜᴋ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴀʙsᴇɴ ᴅɪ ɢʀᴏᴜᴘ.</u>
➢ ᴘᴇʀɪɴᴛᴀʜ: <code>rmabs</code>
  ➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ: <u>ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ᴀʙsᴇɴ ɢʀᴏᴜᴘ.</u></blockquote>
"""

hadir_list = []

def get_hadir_list(client):
    return "\n".join([f"👤 {user['mention']} - {user['jam']}" for user in hadir_list])

@CB.UBOT("rmabs")
async def clear_absen_command(client, message):
    if not hadir_list:
        await message.reply(f"Not absen!")
    else:
        hadir_list.clear()
        await message.reply(f"Clear absen!")

@CB.INLINE("^absen_in")
async def absen_query(client, inline_query):
    user_id = inline_query.from_user.id
    mention = inline_query.from_user.mention
    timestamp = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%d-%m-%Y")
    jam = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%H:%M:%S")

    hadir_text = get_hadir_list(client)

    text = f"<blockquote><b>ᴛᴀɴɢɢᴀʟ: {timestamp}</b></blockquote>\n<blockquote><b>ɴᴀᴍᴀ ᴍᴀɴᴜsɪᴀ:</b></blockquote>\n<blockquote><b>{hadir_text}</b></blockquote>\n"
    buttons = [[InlineKeyboardButton("ᴀʙsᴇɴ ᴊɪɴɢ", callback_data="absen_hadir")]]
    keyboard = InlineKeyboardMarkup(buttons)
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="💬",
                    input_message_content=InputTextMessageContent(text),
                    reply_markup=keyboard
                )
            )
        ],
    )

@CB.CALLBACK("absen_hadir")
async def hadir_callback(client, callback_query):
    user_id = callback_query.from_user.id
    mention = callback_query.from_user.mention
    timestamp = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%d-%m-%Y")
    jam = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%H:%M:%S")
    if any(user['user_id'] == user_id for user in hadir_list):
        await callback_query.answer("Anda sudah absen sebelumnya!", show_alert=True)
    else:
        hadir_list.append({"user_id": user_id, "mention": mention, "jam": jam})
        hadir_text = get_hadir_list(client)
        text = f"<blockquote><b>ᴛᴀɴɢɢᴀʟ: {timestamp}</b></blockquote>\n<blockquote><b>ɴᴀᴍᴀ ᴍᴀɴᴜsɪᴀ:</b></blockquote>\n<blockquote><b>{hadir_text}</b></blockquote>\n"
        buttons = [[InlineKeyboardButton("ᴀʙsᴇɴ ᴊɪɴɢ", callback_data="absen_hadir")]]
        keyboard = InlineKeyboardMarkup(buttons)
        await callback_query.edit_message_text(text, reply_markup=keyboard)

@CB.UBOT("abs")
async def absen_command(client, message):
    user_id = message.from_user.id
    mention = message.from_user.mention
    timestamp = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%d-%m-%Y")
    jam = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%H:%M:%S")

    try:
        x = await client.get_inline_bot_results(bot.me.username, "absen_in")
        if x.results:
            await message.reply_inline_bot_result(x.query_id, x.results[0].id)
        else:
            await message.reply(f"Error!")
    except asyncio.TimeoutError:
        await message.reply(f"Error!")
    except Exception as e:
        await message.reply(e)
  
