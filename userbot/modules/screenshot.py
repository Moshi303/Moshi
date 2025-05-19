import asyncio
import os

from pyrogram import *
from pyrogram import filters
from pyrogram.types import *

from userbot import *
from pyrogram import Client, enums
from pyrogram.types import Message
from userbot.core.helpers.basic import *
from userbot.config import *

__MODULE__ = "sᴄʀᴇᴇɴsʜᴏᴛ"

__HELP__ = f"""
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ss 』

➢ ᴘᴇʀɪɴᴛᴀʜ: <code>{prefix}sc</code> [ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ]
➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴍʙɪʟ ᴘᴀᴘ ᴛɪᴍᴇʀ, ᴄᴇᴋ ᴘᴇsᴀɴ ᴛᴇʀsɪᴍᴘᴀɴ.<b></blockquote>
"""


@CB.UBOT("sc")
async def pencuri(client, message):
    dia = message.reply_to_message
    me = client.me.id
    if not dia:
        await edit_or_reply(message, "<blockquote><b>ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ᴍᴇᴅɪᴀ.<b></blockquote>")
    anjing = dia.caption or None
    await edit_or_reply(message, "<blockquote><b>ᴄᴇᴋ ᴘᴇsᴀɴ ᴛᴇʀsɪᴍᴘᴀɴ ʟᴜ sᴇᴋᴀʀᴀɴɢ...<b></blockquote>")
    if dia.text:
        await dia.copy("me")
        await message.delete()
    if dia.photo:
        anu = await client.download_media(dia)
        await client.send_photo("me", anu, anjing)
        await message.delete()
        os.remove(anu)
    if dia.video:
        anu = await client.download_media(dia)
        await client.send_video("me", anu, anjing)
        await message.delete()
        os.remove(anu)
    if dia.audio:
        anu = await client.download_media(dia)
        await client.send_audio("me", anu, anjing)
        await message.delete()
        os.remove(anu)
    if dia.voice:
        anu = await client.download_media(dia)
        await client.send_voice("me", anu, anjing)
        await message.delete()
        os.remove(anu)
    if dia.document:
        anu = await client.download_media(dia)
        await client.send_document("me", anu, anjing)
        await message.delete()
        os.remove(anu)
    try:
        await client.send_message("me", "<blockquote><b>**sᴄʀᴇᴇɴsʜᴏᴛ ɴʏᴀ ᴛᴜʜ.**<b></blockquote>")
    except Exception as e:
        print(e)
