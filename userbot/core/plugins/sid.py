import html
import asyncio
from pyrogram import *
from pyrogram.raw.types import *
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram import filters

import logging

from pyrogram.enums import ChatType


from userbot import *


async def id_cmd(client, message):
    chat = message.chat
    your_id = message.from_user.id
    message_id = message.id
    reply = message.reply_to_message

    text = f"<blockquote><b>**[Message ID:]({message.link})** `{message_id}`\n"
    text += f"**[Your ID:](tg://user?id={your_id})** `{your_id}`<b></blockquote>\n"

    if not message.command:
        message.command = message.text.split()
        
    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await client.get_users(split)).id
            text += f"<blockquote><b>**[User ID:](tg://user?id={user_id})** `{user_id}`<b></blockquote>\n"

        except Exception:
            return await message.reply("<blockquote><b>This user doesn't exist.<b></blockquote>", quote=True)

    text += f"<blockquote><b>**[Chat ID:](https://t.me/{chat.username})** `{chat.id}`<b></blockquote>\n"

    if not getattr(reply, "empty", True) and not message.forward_from_chat and not reply.sender_chat:
        text += (
            f"<blockquote><b>**[Replied Message ID:]({reply.link})** `{message.reply_to_message.id}`<b></blockquote>\n"
        )
        text += f"<blockquote><b>**[Replied User ID:](tg://user?id={reply.from_user.id})** `{reply.from_user.id}`<b></blockquote>\n"

    if reply and reply.forward_from_chat:
        text += f"<blockquote><b>The forwarded channel, {reply.forward_from_chat.title}, has an id of `{reply.forward_from_chat.id}`<b></blockquote>\n"
        print(reply.forward_from_chat)
    
    if reply and reply.sender_chat:
        text += f"<blockquote><b>ID of the replied chat/channel, is `{reply.sender_chat.id}`<b></blockquote>"
        print(reply.sender_chat)

    await message.reply(
       text,
       disable_web_page_preview=True,
    )
