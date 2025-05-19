from asyncio import sleep

from pyrogram.enums import ChatType
from pyrogram.types import *
from pyrogram.raw.functions.messages import DeleteHistory, StartBot
from userbot.core.function.emoji import emoji

from bs4 import BeautifulSoup
from io import BytesIO

from telegraph import Telegraph, exceptions, upload_file
from userbot.core.plugins.lmt import *
from userbot import *

async def limit_cmd(client, message):
    await client.unblock_user("SpamBot")
    bot_info = await client.resolve_peer("SpamBot")
    msg = await message.reply(f"ᴘʀᴏᴄᴇssɪɴɢ . . .")
    response = await client.invoke(
        StartBot(
            bot=bot_info,
            peer=bot_info,
            random_id=client.rnd_id(),
            start_param="start",
        )
    )
    await sleep(1)
    await msg.delete()
    status = await client.get_messages("SpamBot", response.updates[1].message.id + 1) 
    if status and hasattr(status, "text"):
        pjg = len(status.text)
        if pjg <= 100:
            text=status.text
            await client.send_message(message.chat.id, f"<blockquote><b>{text}</b></blockquote>", reply_to_message_id=message.id)
            return await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))
        else:
            text=status.text
            await client.send_message(message.chat.id, f"<blockquote><b>{text}</b></blockquote>", reply_to_message_id=message.id)
            return await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))
