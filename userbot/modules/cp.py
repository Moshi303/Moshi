# Jangan bilang copas mulu bg
# lu juga sering copas soalnya 
# Credit By : @Usern4meDoestExist404
# Gausah Riweh Ye Ini CP gua bangsat


import random
import asyncio

from userbot import *
from pyrogram.types import *
from userbot import bot, ubot
from pyrogram.types import Message
from pyrogram import __version__
from pyrogram.enums import *


@CB.UBOT("ppcp")
async def pcp(client: Client, message: Message):
    ryn = await message.edit("🔎 **Search PPCP...**")
    await message.reply_photo(
        choice(
            [
                ky.photo.file_id
                async for ky in client.search_messages(
                    "ppcpcilik", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Nih Hasilnya.\nUpload by {bot.me.mention}",
    )
    await ryn.delete()

@CB.UBOT("ppcp2")
async def cp(client, message):
    ryn = await message.edit("🔎 **Search Ppcp 2...**")
    await message.reply_photo(
        choice(
            [
                cot.photo.file_id
                async for cot in client.search_messages(
                    "mentahanppcp", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Nih Hasilnya.\nUpload by {bot.me.mention}",
    )
    await ryn.delete()

@CB.UBOT("anim")
async def anim(client, message):
    ryn = await message.edit("🔎 **Search Anime...**")
    await message.reply_photo(
        choice(
            [
                jir.photo.file_id
                async for jir in client.search_messages(
                    "animehikarixa", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Nih Hasilnya.\nUpload by {bot.me.mention}",
    )
    await ryn.delete()

@CB.UBOT("pap")
async def pap(client, message):
    ryn = await message.edit("🔎 **Nih PAP Nya...**")
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "mm_kyran", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"**Nih Papnya Buat Kamu** 🥺😘 <b><a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a></b>",
    )
    await ryn.delete()


__MODULE__ = "ᴘᴘᴄᴘ"
__HELP__ = f"""
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘᴘᴄᴘ 』
✓ Perintah : <code>{0}ppcp</code>
✓ Penjelasan: Untuk mencari foto ppcp random.
✓ Perintah : <code>{0}ppcp2</code>
✓ Penjelasan: Untuk mencari foto ppcp random.
✓ Perintah : <code>{0}anim</code>
✓ Penjelasan: Untuk mencari foto anim random
✓ Perintah : <code>{0}pap</code>
✓ Penjelasan: Untuk mencari foto pap random.</b><blockquote>
"""
