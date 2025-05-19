import asyncio
import random
from pyrogram.errors import FloodWait
from pyrogram import *
from pyrogram import types
from asyncio import sleep
from userbot.config import OWNER_ID
from userbot import *

__MODULE__ = "antiuser"
__HELP__ = """
『 </u>ʙᴀɴᴛᴜᴀɴ ᴀɴᴛɪᴜsᴇʀ</u> 』
<blockquote>⌲ ᴘᴇʀɪɴᴛᴀʜ: <code>{0}x</u>
   <u>ᴜɴᴛᴜᴋ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴜsᴇʀ ᴋᴇ ᴅᴀғᴛᴀʀ ᴀɴᴛɪᴜsᴇʀ</u>

⌲ ᴘᴇʀɪɴᴛᴀʜ: <code>{0}ux</u>
  <u>ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ᴜsᴇʀ ᴅɪ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ ᴀɴᴛɪᴜsᴇʀ</code>

⌲ ᴘᴇʀɪɴᴛᴀʜ: <code>{0}getx</code>
  <u>ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴀғᴛᴀʀ ᴀɴᴛɪᴜsᴇʀ</u>

⌲ ᴘᴇʀɪɴᴛᴀʜ: <code>{0}xl</code>
   <u>ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴀɴᴛɪᴜsᴇʀ</u></blockquote>
"""
@CB.UBOT("xl")
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    txt = await message.reply(f"{prs}<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    arg = get_arg(message)

    if not arg or arg.lower() not in ["off", "on"]:
        return await txt.edit(f"<blockquote>{ggl}<b>ɢᴜɴᴀᴋᴀɴ</b> <code>{message.text.split()[0]}</code> <b>on or off</b></blockquote>")

    type = True if arg.lower() == "on" else False
    await set_vars(client.me.id, "ON_OFF_ANTI_USER", type)
    return await txt.edit(f"<blockquote>{sks}<b>ᴀɴᴛɪᴜsᴇʀ ʙᴇʀʜᴀsɪʟ ᴅɪ sᴇᴛᴛɪɴɢs ᴋᴇ {type}</b></blockquote>")

@CB.UBOT("x")
async def add_user_to_blacklist(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    if len(message.command) != 2 and not message.reply_to_message:
        await message.reply_text(f"<blockquote>{ggl}<b>ɢᴜɴᴀᴋᴀɴ</b> <code>{message.text.split()[0]}</code> <b>[uꜱer_id/reply]</b></blockquote>", quote=True)
        return

    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    else:
        user_id = int(message.command[1])
    if user_id == OWNER_ID:
        return await message.reply(f"<blockquote>{ggl}<b>ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴋᴇ ᴘᴇᴍʙᴜᴀᴛ</b></blockquote>")
    user_ids = await get_user_ids(client.me.id)
    if user_id not in user_ids:
        user_ids.append(user_id)
        await user_collection.update_one({"_id": client.me.id}, {"$set": {"user_dia": user_ids}}, upsert=True)
        await message.reply_text(f"<blockquote>{sks}<b>sᴜᴄᴄᴇs ᴀᴅᴅɪɴɢ ᴛᴏ ᴀɴᴛɪᴜsᴇʀ</b>!</blockquote>", quote=True)
    else:
        await message.reply_text(f"<blockquote>{ggl}<b>ᴀʟʀᴇᴀᴅʏ ɪɴ ᴅᴀᴛᴀʙᴀsᴇ</b></blockquote>", quote=True)

@CB.UBOT("ux")
async def remove_user_from_blacklist(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    if len(message.command) != 2 and not message.reply_to_message:
        await message.reply_text(f"<blockquote>{ggl}<b>ɢᴜɴᴀᴋᴀɴ</b> <code>{message.text.split()[0]}</code> [ʀᴇᴘʟʏ/ᴜsᴇʀ_ɪᴅ]</blockquote>", quote=True)
        return

    if m.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    else:
        user_id = int(message.command[1])

    user_ids = await get_user_ids(client.me.id)
    if user_id in user_ids:
        user_ids.remove(user_id)
        await user_collection.update_one({"_id": client.me.id}, {"$set": {"user_dia": user_ids}}, upsert=True)
        await message.reply_text(f"<blockquote>{sks}</b>ᴜsᴇʀ  :</b> </code>{user_id}</code> \n{sks}<b>ᴛᴇʟᴀʜ ᴅɪʜᴀᴘᴜs ᴅɪ ᴅᴀʟᴀᴍ ᴅᴀᴛᴀʙᴀsᴇ</b></blockquote>", quote=True)
    else:
        await message.reply_text(f"<blockquote>{ggl}<b>ᴜsᴇʀ ᴛᴇʀsᴇʙᴜᴛ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴀʟᴀᴍ ᴅᴀᴛᴀʙᴀsᴇ</b></blockquote>", quote=True)

@CB.UBOT("getx")
async def display_blacklist(client, message):
    try:
        daftar = await get_user_ids(client.me.id)
        pesan = "<b>ʙʟᴀᴄᴋʟɪsᴛ ᴜsᴇʀs :</b>\n" + "\n".join(f"{i+1}. `{x}`" for i, x in enumerate(daftar))
        await message.reply(pesan)
    except Exception as r:
        await message.reply(str(r))