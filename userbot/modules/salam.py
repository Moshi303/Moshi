# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from userbot.core.helpers.msg_type import ReplyCheck
from userbot import *


@CB.UBOT("as")
async def salamone(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "**Assalamualaikum...**",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@CB.UBOT("ass")
async def salamdua(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "**Assalamualaikum Warahmatullahi Wabarakatuh**",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@CB.UBOT("ws")
async def jwbsalam(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "**Wa'alaikumsalam...**",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@CB.UBOT("wr")
async def jwbsalamlngkp(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "**Wa'alaikumsalam Warahmatullahi Wabarakatuh**",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@CB.UBOT("ar")
async def salamarab(client: Client, message: Message):
    xx = await edit_or_reply(message, "Salam Dulu..")
    await asyncio.sleep(2)
    await xx.edit(f"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")


__MODULE__ = "salam"
__HELP__ = f"""
<blockquote><b>Bantuan Untuk Salam

๏ Perintah: <code>{PREFIX[0]}as</code>
◉ Penjelasan: Coba sendiri.

๏ Perintah: <code>{PREFIX[0]}ass</code>
◉ Penjelasan: Coba sendiri.

๏ Perintah: <code>{PREFIX[0]}ws</code>
◉ Penjelasan: Coba sendiri.

๏ Perintah: <code>{PREFIX[0]}wr</code>
◉ Penjelasan: Coba sendiri.

๏ Perintah: <code>{PREFIX[0]}ar</code>
◉ Penjelasan: Coba sendiri.<b></blockquote>
"""
