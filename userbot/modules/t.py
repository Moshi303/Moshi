import os
import random
import asyncio 

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import ChatAdminRequired
from userbot.core.function.emoji import emoji
from pyrogram.types import ChatPermissions, ChatPrivileges, Message
from userbot.core.helpers.basic import edit_or_reply, get_text, get_user
from pyrogram.errors import *
from pyrogram.types import *
from userbot.config import *

from userbot import *
from pyrogram import Client, enums
from pyrogram.types import Message


@CB.UBOT("pbanall")
async def banall(client, message):
    if not message.from_user:
        return
    ok = await message.edit("ɢᴇᴛᴛɪɴɢ ᴄʜᴀᴛ ᴍᴇᴍʙᴇʀꜱ....")
    mem = []
    async for x in client.get_chat_members(message.chat.id):
        mem.append(x.user.id)
    try:
        await ok.edit("ʙᴀɴɴɪɴɢ ᴄʜᴀᴛ ᴍᴇᴍʙᴇʀꜱ....")
    except:
        await message.reply("ʙᴀɴɴɪɴɢ ᴄʜᴀᴛ ᴍᴇᴍʙᴇʀꜱ....")
    a = 0
    b = 0
    for y in mem:
        try:
            await client.ban_chat_member(message.chat.id, y)
            a += 1
        except:
            b += 1
            pass
    try:
        await ok.edit(f"ᴅᴏɴᴇ ✅\n\n{a} ʙᴀɴɴᴇᴅ..!!\n \n{b} ꜰᴀɪʟᴇᴅ..!!")
    except:
        await message.reply(f"ᴅᴏɴᴇ ✅\n\n{a} ʙᴀɴɴᴇᴅ..!!\n \n {b} ꜰᴀɪʟᴇᴅ..!!")

@CB.UBOT("punbanall")
async def unbanall(client, message):
    unban_count = 0
    async for meki in c.get_chat_members(chat_id, filter=ChatMembersFilter.BANNED):
        if meki.user is not None:
            try:
                user_id = meki.user.id
                await c.unban_chat_member(chat_id, user_id)
                unban_count += 1
                await message.edit(
                    f"{em.proses} Memproses unban... Berhasil unban: {unban_count}"
                )
            except FloodWait as e:
                await asyncio.sleep(e.value)
                await c.send_message(
                    chat_id, f"{em.gagal} Harap tunggu {e.value} detik lagi"
                )
    return await message.edit(
        f"{em.sukses} Berhasil unban : <code>{unban_count}</code> member."
    )


@CB.UBOT("anben")
async def _(c: message, _):
    em.initialize()
    dia = await c.get_chat_member(chat_id=m.chat.id, user_id=m.from_user.id)
    pros = await m.reply(f"{em.proses} Sabar ya..")
    if dia.status in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
        if m.from_user.id not in DEVS:
            await m.reply(f"{em.gagal} Maaf, Anda bukan seorang DEVELOPER!")
            await pros.delete()
            return

        return await mak_mek(c, m.chat.id, pros)
    else:
        await m.reply(
            f"{em.gagal} Anda harus menjadi admin atau memiliki izin yang cukup untuk menggunakan perintah ini!"
        )
        await pros.delete()
        return
