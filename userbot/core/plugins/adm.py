import asyncio

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, ChatPrivileges, Message
from pyrogram.errors import *
from pyrogram.types import *
from userbot.core.function.emoji import emoji

from userbot import *

BANNED_USERS = filters.user()            


async def global_banned(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply(emoji("proses") + "<blockquote><b>ᴏᴛᴡ ɢʙᴀɴ sɪ ᴊᴀᴍᴇᴛ....<b></blockquote>")
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        await message.reply(
            "<blockquote><b>gban [user_id/username/reply to uꜱer]<b></blockquote>"
        )
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
    try:
        user = await client.get_users(user_id)
    except PeerIdInvalid:
        await message.reply(
            f"<blockquote><b>tidak dapat menemukan user tersebut.<b></blockquote>")
        return
    iso = 0
    gagal = 0
    prik = user.id
    prok = await get_seles()
    gua = client.me.id
    udah = await is_banned_user(gua, prik)
    async for dialog in client.get_dialogs():
        chat_type = dialog.chat.type
        if chat_type in [
            ChatType.GROUP,
            ChatType.SUPERGROUP,
            ChatType.CHANNEL,
        ]:
            chat = dialog.chat.id
            
            if prik in DEVS:
                return await message.reply(
                    emoji("gagal") + f"<blockquote><b>Lu ga akan bisa gban dia tolol dia Developers {bot.me.mention} goblok.<b></blockquote>"
                )
            elif prik in prok:
                return await message.reply(
                    emoji("gagal") + f"<blockquote><b>Dia tu admin dari userbot {bot.me.mention} goblok<b></blockquote>"
                )
            elif udah:
                return await message.reply(
                    f"<blockquote><b>Si bocah tolol ini udah di gban sama lu goblok.<b></blockquote>"
                )
            elif prik not in prok and prik not in DEVS:
                try:
                    await add_banned_user(gua, prik)
                    await client.ban_chat_member(chat, prik)
                    iso = iso + 1
                except BaseException:
                    gagal = gagal + 1
    return await Tm.edit(
        f"""
<blockquote><b>global banned

<b>ʙᴇʀʜᴀsɪʟ ʙᴀɴɴᴇᴅ: {iso} Chat</b>
<b>ɢᴀɢᴀʟ ʙᴀɴɴᴇᴅ: {gagal} Chat</b>
<b>ᴜsᴇʀ: <a href='tg://user?id={prik}'>{user.first_name}</a><b></blockquote>
"""
    )

async def cung_ban(client, message):
    user_id = await extract_user(message)
    if message.from_user.id != client.me.id:
        Tm = await message.reply(emoji("proses") + "<blockquote><b>ᴍᴇᴍᴘʀᴏsᴇs.....<b></blockquote>")
    else:
        Tm = await message.reply(emoji("proses") + "<blockquote><b>ᴍᴇᴍᴘʀᴏsᴇs....<b></blockquote>")
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        await Tm.reply_to_message(
            "<blockquote><b>ungban [user_id/username/reply to user]<b></blockquote>"
        )
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
    try:
        user = await client.get_users(user_id)
    except PeerIdInvalid:
        await Tm.reply_to_message(emoji("gagal") + "<blockquote><b>tidak menemukan user tersebut.<b></blockquote>")
        return
    iso = 0
    gagal = 0
    prik = user.id
    gua = client.me.id
    udah = await is_banned_user(gua, prik)
    async for dialog in client.get_dialogs():
        chat_type = dialog.chat.type
        if chat_type in [
            ChatType.GROUP,
            ChatType.SUPERGROUP,
            ChatType.CHANNEL,
        ]:
            chat = dialog.chat.id
            if prik in BANNED_USERS:
                BANNED_USERS.remove(prik) 
            try:
                await remove_banned_user(gua, prik)
                await client.unban_chat_member(chat, prik)
                iso = iso + 1
            except BaseException:
                gagal = gagal + 1

    return await Tm.edit(
        f"""
<blockquote><b>global unbanned

<b>ʙᴇʀʜᴀsɪʟ ᴜɴʙᴀɴɴᴇᴅ: {iso} Chat</b>
<b>ɢᴀɢᴀʟ ᴜɴʙᴀɴɴᴇᴅ: {gagal} Chat</b>
<b>ᴜsᴇʀ: <a href='tg://user?id={prik}'>{user.first_name}</a><b></blockquote>
"""
    )


async def gbanlist(client, message):
    gua = client.me.id
    total = await get_banned_count(gua)
    if total == 0:
        return await message.reply_to_message(emoji("gagal") + "<blockquote><b>belum ada pengguna yang digban.<b></blockquote>")
    nyet = await message.reply_to_message(emoji("proses") + "<blockquote><b>ᴍᴇᴍᴘʀᴏsᴇs...<b></blockquote>")
    msg = "total gbanned:\n\n"
    tl = 0
    org = await get_banned_users(gua)
    for i in org:
        tl += 1
        try:
            user = await client.get_users(i)
            user = (
                user.first_name if not user.mention else user.mention
            )
            msg += f"{tl}• {user}\n"
        except Exception:
            msg += f"{tl}• {i}\n"
            continue
    if tl == 0:
        return await nyet.reply(emoji("gagal") + "<blockquote><b>belum ada pengguna yang digban.<b></blockquote>")
    else:
        return await nyet.reply(msg)
