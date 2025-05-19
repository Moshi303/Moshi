import asyncio
import random

from gc import get_objects
from asyncio import sleep
from pyrogram.raw.functions.messages import DeleteHistory, StartBot
from pyrogram.enums import ChatType
from pyrogram.errors.exceptions import FloodWait

from userbot import *

__MODULE__ = "ʙʀᴏᴀᴅᴄᴀsᴛ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙʀᴏᴀᴅᴄᴀsᴛ. 』

➢ ᴘᴇʀɪɴᴛᴀʜ: <code>{0}gikes</code> or <code>{0}gukes</code>
    ɢɪᴋᴇs ɢʀᴜᴘs | ɢᴜᴋᴇs ᴘʀɪᴠᴀᴛᴇ

➢ ᴘᴇʀɪɴᴛᴀʜ: <code>{0}stopg</code>
    ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴇɴᴛɪᴋᴀɴ ᴘʀᴏsᴇs ɢɪᴋᴇs ʏᴀɴɢ sᴇᴅᴀɴɢ ʙᴇʀʟᴀɴɢsᴜɴɢ

➢ ᴘᴇʀɪɴᴛᴀʜ: <code>{0}bcfd</code> or <code>{0}cfd</code>
    ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ sɪᴀʀᴀɴ sᴇᴄᴀʀᴀ ғᴏʀᴡᴀʀᴅ

➢ ᴘᴇʀɪɴᴛᴀʜ: <code>{0}send</code>
    ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ ᴜsᴇʀ/ɢʀᴜᴘs/ᴄʜᴀɴɴᴇʟ

➢ ᴘᴇʀɪɴᴛᴀʜ: <code>{0}auto_gcast</code>
    ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ sɪᴀʀᴀɴ sᴇᴄᴀʀᴀ ᴏᴛᴏᴍᴀᴛɪs

ǫᴜᴇʀʏ:
    |ᴏɴ/ᴏғғ |ᴛᴇxᴛ |ᴅᴇʟᴀʏ |ʀᴇᴍᴏᴠᴇ |ʟɪᴍɪᴛ<b></blockquote>
"""

async def get_data_id(client, query):
    chat_types = {
        "global": [ChatType.CHANNEL, ChatType.GROUP, ChatType.SUPERGROUP],
        "all": [ChatType.GROUP, ChatType.SUPERGROUP, ChatType.PRIVATE],
        "group": [ChatType.GROUP, ChatType.SUPERGROUP],
        "users": [ChatType.PRIVATE],
    }
    return [dialog.chat.id async for dialog in client.get_dialogs() if dialog.chat.type in chat_types.get(query, [])]

@CB.UBOT("gikes")
async def _(client, message):
    await babi_gcast(client, message)

@CB.UBOT("stopg")
async def _(client, message):
    await babi_cancel(client, message)

@CB.UBOT("gukes")
async def _(client, message):
    await babi_gukes(client, message)

@CB.UBOT("bcfd|cfd")
async def _(client, message):
    await babi_brd(client, message)

@CB.UBOT("auto_gcast")
async def _(client, message):
    await babi_auto(client, message)
