import asyncio
from gc import get_objects

from pyrogram.enums import ChatType
from pyrogram.errors.exceptions import FloodWait

from userbot import *
from userbot.config import *

def get_message(message):
    msg = (
        message.reply_to_message
        if message.reply_to_message
        else ""
        if len(message.command) < 2
        else " ".join(message.command[1:])
    )
    return msg


async def get_broadcast_id(client, query):
    chats = []
    chat_types = {
        "group": [ChatType.GROUP, ChatType.SUPERGROUP],
        "users": [ChatType.PRIVATE],
    }
    async for dialog in client.get_dialogs():
        if dialog.chat.type in chat_types[query]:
            chats.append(dialog.chat.id)

    return chats


async def spam_broadcast_cmd(client, message):
    msg = await message.reply("<blockquote><b>ᴏᴛᴡ ɴɢɪʀɪᴍ ᴋᴇ ɢᴄ ʏɢ ʙᴀɴʏᴀᴋ ᴊᴀᴍᴇᴛɴʏᴀ...<b></blockquote>")

    send = get_message(message)
    if not send:
        return await msg.edit("<blockquote><b>ᴍᴏʜᴏɴ ʙᴀʟᴀs sᴇsᴜᴀᴛᴜ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ sᴇsᴜᴀᴛᴜ<b></blockquote>")

    global broadcast_running
    broadcast_running = True

    chats = await get_broadcast_id(client, "group")
    blacklist = await get_chat(client.me.id)

    done = 0
    failed = 0
    for chat_id in chats:
        if not broadcast_running:
            break

        if chat_id in blacklist or chat_id in BLACKLIST_CHAT:
            continue

        try:
            if message.reply_to_message:
                count_message = int(message.command[1])
                for i in range(count_message):
                    await send.copy(chat_id)
                    await asyncio.sleep(0.1)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            if message.reply_to_message:
                count_message = int(message.command[1])
                for i in range(count_message):
                    await send.copy(chat_id)
                    await asyncio.sleep(0.1)
            done += 1
        except Exception:
            failed += 1

    return await msg.edit(f"<blockquote><b>📊 ᴘᴇsᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀɴᴅᴀ ᴛᴇʀᴋɪʀɪᴍ ᴋᴇ {done} 📚 ɢʀᴜᴘ. ɢᴀɢᴀʟ: {failed}<b></blockquote>")
