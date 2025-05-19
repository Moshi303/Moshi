import asyncio
import random

from gc import get_objects
from asyncio import sleep
from pyrogram.raw.functions.messages import DeleteHistory, StartBot

from pyrogram.errors.exceptions import FloodWait

from userbot import *

__MODULE__ = "blwl"
__HELP__ = """
『 <u>ʙᴀɴᴛᴜᴀɴ ᴡʜɪᴛᴇ ʟɪsᴛ</u> 』
<blockquote>⌲ ᴘᴇʀɪɴᴛᴀʜ: <code>{0}addwl</code>
   <u>ᴍᴇᴍᴀsᴜᴋᴀɴ ᴜsᴇʀ ᴋᴇ ᴅᴀғᴛᴀʀ ᴡʜɪᴛᴇʟɪsᴛ</u>

⌲ ᴘᴇʀɪɴᴛᴀʜ: <code>{0}unwl</code>
   <u>ᴍᴇɴɢʜᴀᴘᴜs ᴜsᴇʀ ᴅᴀʀɪ ᴅᴀғᴛᴀʀ ᴡʜɪᴛᴇʟɪsᴛ</u>
  
⌲ ᴘᴇʀɪɴᴛᴀʜ: <code>{0}rallwl</code>
   <u>ᴍᴇɴɢʜᴀᴘᴜs sᴇᴍᴜᴀ ᴅᴀғᴛᴀʀ ᴡʜɪᴛᴇʟɪsᴛ ᴜsᴇʀ</u>
  
⌲ ᴘᴇʀɪɴᴛᴀʜ: <code>{0}listwl</code>
   <u>ᴍᴇᴍᴇʀɪᴋsᴀ ᴅᴀғᴛᴀʀ ᴡʜɪᴛᴇʟɪsᴛ ᴜsᴇʀ</u></blockquote>
"""


@CB.UBOT("addwl")
async def _(client, message):
    prs = await EMO.PROSES(client)
    grp = await EMO.BL_GROUP(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    _msg = f"<b>{prs} ᴍᴇᴍᴘʀᴏsᴇs...</b>"

    msg = await message.reply(_msg)
    try:
        chat_id = message.chat.id
        whitelist = await get_list_from_vars(client.me.id, "WL_ID", chat_id)

        if chat_id in whitelist:
            txt = f"""
<blockquote>{grp} ᴘʀɪᴠᴀᴛᴇ: {message.chat.first_name}
{ktrng} ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <u>ᴀʟʀᴇᴀᴅʏ ɪɴ ᴡʜɪᴛᴇʟɪsᴛ ᴜsᴇʀ</u></blockquote>
"""
        else:
            await add_to_vars(client.me.id, "WL_ID", chat_id)
            txt = f"""
<blockquote>{grp} ᴘʀɪᴠᴀᴛᴇ: {message.chat.first_name}
{ktrng} ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <u>ᴡʜɪᴛᴇʟɪsᴛ ʙʀᴏᴀᴅᴄᴀsᴛ</u></blockquote>
"""

        return await msg.edit(txt)
    except Exception as error:
        return await msg.edit(error)

@CB.UBOT("listwl")
async def _(client, message):
    prs = await EMO.PROSES(client)
    _msg = f"{prs} ᴍᴇᴍᴘʀᴏsᴇs..."
    mzg = await message.reply(_msg)

    whitelist = await get_list_from_vars(client.me.id, "WL_ID", chat_id)
    total_blacklist = len(whitelist)

    list = "❏ ᴅᴀғᴛᴀʀ ᴡʜɪᴛᴇʟɪsᴛ ᴜsᴇʀ\n"

    for chat_id in whitelist:
        try:
            chat = await client.get_chat(chat_id)
            list += f" ├ {chat.first_name} | {chat.id}\n"
        except:
            list += f" ├ {chat_id}\n"

    list += f"<u>❏ ᴛᴏᴛᴀʟ ᴡʜɪᴛᴇʟɪsᴛ</u> : <code>{total_blacklist}</code>"
    return await mzg.edit(list)

@CB.UBOT("rallwl")
async def _(client, message):
    prs = await EMO.PROSES(client)
    _msg = f"{prs} ᴍᴇᴍᴘʀᴏsᴇs..."

    msg = await message.reply(_msg)
    whitelist = await get_list_from_vars(client.me.id, "WL_ID", chat_id)

    if not whitelist:
        return await msg.edit("<blockquote><u>ᴡʜɪᴛᴇʟɪsᴛ ᴜsᴇʀ ᴇᴍᴘᴛʏ !</u></blockquote>")

    for chat_id in whitelist:
        await remove_from_vars(client.me.id, "WL_ID", chat_id)

    await msg.edit("<blockquote><u>ᴀʟʟ ᴡʜɪᴛᴇʟɪsᴛ ʀᴇᴍᴏᴠᴇᴅ !</u></blockquote>")

@CB.UBOT("unwl")
async def _(client, message):
    prs = await EMO.PROSES(client)
    grp = await EMO.BL_GROUP(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    _msg = f"{prs} ᴍᴇᴍᴘʀᴏsᴇs..."

    msg = await message.reply(_msg)
    try:
        chat_id = get_arg(message) or message.chat.id
        whitelist = await get_list_from_vars(client.me.id, "WL_ID", chat_id)

        if chat_id not in whitelist:
            response = f"""
<blockquote>{grp} ᴘʀɪᴠᴀᴛᴇ: {message.chat.first_name}
{ktrng} ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <u>ɴᴏᴛ ғᴏᴜɴᴅ ɪɴ ᴅᴀᴛᴀʙᴀsᴇ</u></blockquote>
"""
        else:
            await remove_from_vars(client.me.id, "WL_ID", chat_id)
            response = f"""
<blockquote>{grp} ᴘʀɪᴠᴀᴛᴇ: {message.chat.first_name}
{ktrng} ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <u>sᴜᴄᴄᴇs ʀᴇᴍᴏᴠᴇ ᴛᴏ ᴅᴀᴛᴀʙᴀsᴇ</u></blockquote>
"""
        return await msg.edit(response)
    except Exception as error:
        return await msg.edit(error)