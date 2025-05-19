from userbot import *
import asyncio
import random

from pyrogram import Client, filters
from pyrogram.types import Message
from userbot.core.helpers.basic import *
from pyrogram.types import *
from userbot import bot, ubot
from pyrogram import __version__
from pyrogram.enums import *

ok = []
nyet = [
    "50",
    "350",
    "97",
    "670",
    "24",
    "909",
    "57",
    "89",
    "4652",
    "153",
    "877",
    "890",
]
babi = ["2", "3", "6", "7", "9"]


@CB.UBOT("fgiben")
async def giben(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply_text("ɢʙᴀɴɪɴɢ...")
    else:
        ex = await message.edit("<blockquote><b>ᴘʀᴏsᴇs ɢʙᴀɴ ᴀɴᴀᴋ ᴀɴᴊɪɴɢ ᴅᴜʟᴜ...<b></blockquote>")
    if not user_id:
        return await ex.edit(
            "<blockquote><b>**ʙᴀʟᴀs ᴘᴇsᴀɴ ᴘᴇɴɢɢᴜɴᴀ ᴀᴛᴀᴜ ʙᴇʀɪᴋᴀɴ ɴᴀᴍᴀ ᴘᴇɴɢɢᴜɴᴀ/ɪᴅ_ᴘᴇɴɢɢᴜɴᴀ**<b></blockquote>"
        )
    if user_id == client.me.id:
        return await ex.edit("<blockquote><b>**ʟᴜ ᴍᴀᴜ ɢʙᴀɴ ᴅɪʀɪ sᴇɴᴅɪʀɪ? ᴛᴏʟᴏʟ!**<b></blockquote>")
    if user_id in DEVS:
        return await ex.edit("<blockquote><b>ᴅᴇᴠs ᴛɪᴅᴀᴋ ʙɪsᴀ ᴅɪ ɢʙᴀɴ, ᴏɴʟʏ ɢᴏᴅs ᴄᴀɴ ᴅᴇғᴇᴀᴛ ɢᴏᴅs<b></blockquote>")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit(
                "<blockquote><b>**ʙᴀʟᴀs ᴘᴇsᴀɴ ᴘᴇɴɢɢᴜɴᴀ ᴀᴛᴀᴜ ʙᴇʀɪᴋᴀɴ ɴᴀᴍᴀ ᴘᴇɴɢɢᴜɴᴀ/ɪᴅ_ᴘᴇɴɢɢᴜɴᴀ**<b></blockquote>"
            )
    ok.append(user.id)
    done = random.choice(nyet)
    msg = (
        f"<u>ɢʙᴀɴɴᴇᴅ</u>"
        f"\n\n<blockquote><b> **ɴᴀᴍᴀ:** [{user.first_name}](tg://user?id={user.id})<b></blockquote>"
        f"\n<blockquote><b> **ᴜsᴇʀ ɪᴅ:** `{user.id}`<b></blockquote>"
    )
    if reason:
        msg += f"\n<blockquote><b> **ᴀʟᴀsᴀɴ:** `{reason}`<b></blockquote>"
    msg += f"\n<blockquote><b> **sᴜᴋsᴇs ᴅɪ:** `{done}` **ᴏʙʀᴏʟᴀɴ**<b></blockquote>"
    await asyncio.sleep(5)
    await ex.edit(msg)


@CB.UBOT("fgimut")
async def gimut(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply_text("ɢᴍᴜᴛɪɴɢ...")
    else:
        ex = await message.edit("<blockquote><b>ᴘʀᴏsᴇs ɢᴍᴜᴛᴇ ᴀɴᴀᴋ ᴀɴᴊɪɴɢ ᴅᴜʟᴜ...<b></blockquote>")
    if not user_id:
        return await ex.edit(
            "<blockquote><b>**ʙᴀʟᴀs ᴘᴇsᴀɴ ᴘᴇɴɢɢᴜɴᴀ ᴀᴛᴀᴜ ʙᴇʀɪᴋᴀɴ ɴᴀᴍᴀ ᴘᴇɴɢɢᴜɴᴀ/ɪᴅ_ᴘᴇɴɢɢᴜɴᴀ**<b></blockquote>"
        )
    if user_id == client.me.id:
        return await ex.edit("<blockquote><b>**ʟᴜ ᴍᴀᴜ ɢᴍᴜᴛᴇ ᴅɪʀɪ sᴇɴᴅɪʀɪ? ᴛᴏʟᴏʟ!**<b></blockquote>")
    if user_id in DEVS:
        return await ex.edit("<blockquote><b>ᴅᴇᴠs ᴛɪᴅᴀᴋ ʙɪsᴀ ᴅɪ ɢᴍᴜᴛᴇ, ᴏɴʟʏ ɢᴏᴅs ᴄᴀɴ ᴅᴇғᴇᴀᴛ ɢᴏᴅs.<b></blockquote>")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit(
                "<blockquote><b>ʙᴀʟᴀs ᴘᴇsᴀɴ ᴘᴇɴɢɢᴜɴᴀ ᴀᴛᴀᴜ ʙᴇʀɪᴋᴀɴ ɴᴀᴍᴀ ᴘᴇɴɢɢᴜɴᴀ/ɪᴅ_ᴘᴇɴɢɢᴜɴᴀ<b></blockquote>"
            )
    ok.append(user.id)
    done = random.choice(nyet)
    msg = (
        f"<u>ɢᴍᴜᴛᴇᴅ</u>"
        f"\n\n<blockquote><b> **ɴᴀᴍᴀ:** [{user.first_name}](tg://user?id={user.id})<b></blockquote>"
        f"\n<blockquote><b> **ᴜsᴇʀ ɪᴅ:** `{user.id}`<b></blockquote>"
    )
    if reason:
        msg += f"\n<blockquote><b> **ᴀʟᴀsᴀɴ:** `{reason}`<b></blockquote>"
    msg += f"\n<blockquote><b> **sᴜᴋsᴇs ᴅɪ:** `{done}` **ᴏʙʀᴏʟᴀɴ**<b></blockquote>"
    await asyncio.sleep(5)
    await ex.edit(msg)


@CB.UBOT("fgikik")
async def gikik(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply_text("ɢᴋɪᴄᴋ...")
    else:
        ex = await message.edit("ᴘʀᴏsᴇs ɢᴋɪᴄᴋɪɴɢ ᴀɴᴀᴋ ᴀɴᴊɪɴɢ ᴅᴜʟᴜ...")
    if not user_id:
        return await ex.edit(
            "<blockquote><b>**ʙᴀʟᴀs ᴘᴇsᴀɴ ᴘᴇɴɢɢᴜɴᴀ ᴀᴛᴀᴜ ʙᴇʀɪᴋᴀɴ ɴᴀᴍᴀ ᴘᴇɴɢɢᴜɴᴀ/ɪᴅ_ᴘᴇɴɢɢᴜɴᴀ**<b></blockquote>"
        )
    if user_id == client.me.id:
        return await ex.edit("<blockquote><b>**ʟᴜ ᴍᴀᴜ ɢᴋɪᴄᴋ ᴅɪʀɪ sᴇɴᴅɪʀɪ? ᴛᴏʟᴏʟ!**<b></blockquote>")
    if user_id in DEVS:
        return await ex.edit("<blockquote><b>ᴅᴇᴠs ᴛɪᴅᴀᴋ ʙɪsᴀ ᴅɪ ɢᴋɪᴄᴋ, ᴏɴʟʏ ɢᴏᴅs ᴄᴀɴ ᴅᴇғᴇᴀᴛ ɢᴏᴅs<b></blockquote>")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit(
                "<blockquote><b>**ʙᴀʟᴀs ᴘᴇsᴀɴ ᴘᴇɴɢɢᴜɴᴀ ᴀᴛᴀᴜ ʙᴇʀɪᴋᴀɴ ɴᴀᴍᴀ ᴘᴇɴɢɢᴜɴᴀ/ɪᴅ_ᴘᴇɴɢɢᴜɴᴀ**<b></blockquote>"
            )
    ok.append(user.id)
    done = random.choice(nyet)
    msg = (
        f"<u>ɢᴋɪᴄᴋᴇᴅ</u>"
        f"\n\n<blockquote><b> **ɴᴀᴍᴀ:** [{user.first_name}](tg://user?id={user.id})<b></blockquote>"
        f"\n<blockquote><b> **ᴜsᴇʀ ɪᴅ:** `{user.id}`<b></blockquote>"
    )
    if reason:
        msg += f"\n<blockquote><b> **ᴀʟᴀsᴀɴ:** `{reason}`<b></blockquote>"
    msg += f"\n<blockquote><b> **sᴜᴋsᴇs ᴅɪ:** `{done}` **ᴏʙʀᴏʟᴀɴ**<b></blockquote>"
    await asyncio.sleep(5)
    await ex.edit(msg)


@CB.UBOT("fgikes")
async def gcast_cmd(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        tex = await message.reply_text("<blockquote><b>**sᴀʙᴀʀ ᴀɴᴊɪɴɢ ʟᴀɢɪ ᴅɪ ɢᴄᴀsᴛ ɪɴᴋ...**<b></blockquote>")
    else:
        return await message.edit_text("<blockquote><b>ᴋᴀsɪʜ ᴘᴇsᴀɴɴʏᴀ ɴɢᴇɴᴛᴏᴛ!.<b></blockquote>")
    done = random.choice(nyet)
    fail = random.choice(babi)
    await asyncio.sleep(5)
    await tex.edit_text(
        f"<blockquote><b> ʙᴇʀʜᴀsɪʟ ᴋᴇ `{done}` ɢᴄ.\n ɢᴀɢᴀʟ ᴋᴇ `{fail}` ɢᴄ.<b></blockquote>"
    )


__MODULE__ = "ғᴀᴋᴇ ᴀᴄᴛɪᴏɴ"
__HELP__ = f"""
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ғᴀᴋᴇ ᴀᴄᴛɪᴏɴ 』

➢ ᴘᴇʀɪɴᴛᴀʜ: <code>{0}fgiben</code>
➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ: ғᴀᴋᴇ ɢʟᴏʙᴀʟ ʙᴀɴ.

➢ ᴘᴇʀɪɴᴛᴀʜ: <code>{0}fgimut</code>
➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ: ғᴀᴋᴇ ɢʟᴏʙᴀʟ ᴍᴜᴛᴇ.

➢ ᴘᴇʀɪɴᴛᴀʜ: <code>{0}fgikik</code>
➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ: ғᴀᴋᴇ ɢʟᴏʙᴀʟ ᴋɪᴄᴋ.

➢ ᴘᴇʀɪɴᴛᴀʜ: <code>{0}fgikes</code>
➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ: ғᴀᴋᴇ ɢʟᴏʙᴀʟ ʙʀᴏᴀᴅᴄᴀsᴛ.<b></blockquote>
"""
