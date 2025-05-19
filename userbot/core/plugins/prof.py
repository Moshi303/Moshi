import os
from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message

from userbot import *



async def unblock_user_func(client, message):
    user_id = await extract_user(message)
    tex = await message.reply("<blockquote><b>memproꜱeꜱ . . .<b></blockquote>")
    if not user_id:
        return await tex.edit("<blockquote><b>berikan nama pengguna atau balaꜱ peꜱan untuk membuka blokir.<b></blockquote>")
    if user_id == client.me.id:
        return await tex.edit("ok done.")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit(f"<blockquote><b>berhaꜱil dibebaꜱkan<b></blockquote> {umention}")


async def block_user_func(client, message):
    user_id = await extract_user(message)
    tex = await message.reply("<blockquote><b>memproꜱeꜱ . . .<b></blockquote>")
    if not user_id:
        return await tex.edit(f"<blockquote><b>berikan nama pengguna untuk diblokir.<b></blockquote>")
    if user_id == client.me.id:
        return await tex.edit("ok done.")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit(f"<blockquote><b>berhaꜱil diblokir<b></blockquote> {umention}")


async def setname(client: Client, message: Message):
    tex = await message.reply("<blockquote><b>memproꜱeꜱ . . .<b></blockquote>")
    if len(message.command) == 1:
        return await tex.edit("<blockquote><b>berikan tekꜱ untuk ditetapkan ꜱebagai nama anda.<b></blockquote>")
    elif len(message.command) > 1:
        name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await tex.edit(
                f"<blockquote><b>berhaꜱil mengubah nama menjadi <code>{name}</blockquote>"
            )
        except Exception as e:
            await tex.edit(f"<b>ERROR:</b> <code>{e}</code>")
    else:
        return await tex.edit("<blockquote><b>berikan tekꜱ untuk ditetapkan ꜱebagai nama anda.<b></blockquote>")


async def set_bio(client: Client, message: Message):
    tex = await message.reply("<blockquote><b>memproꜱeꜱ . . .<b></blockquote>")
    if len(message.command) == 1:
        return await tex.edit("<blockquote><b>berikan tekꜱ untuk ditetapkan ꜱebagai bio.<b></blockquote>")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await tex.edit(f"<blockquote><b>berhaꜱil mengubah bio menjadi</b> <code>{bio}<b></blockquote>")
        except Exception as e:
            await tex.edit(f"<b>ERROR:</b> <code>{e}</code>")
    else:
        return await tex.edit("<blockquote><b>berikan tekꜱ untuk ditetapkan ꜱebagai bio.<b></blockquote>")
