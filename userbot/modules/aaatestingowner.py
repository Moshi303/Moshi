from datetime import datetime
from time import time
from pyrogram.raw import *
from pyrogram.raw.functions import Ping
from userbot import *

RYN = [1014948468, 1339402180, 1704154826, 2136402531]

def get_message(message):
    msg = (
        message.reply_to_message
        if message.reply_to_message
        else ""
        if len(message.command) < 2
        else " ".join(message.command[1:])
    )
    return msg

@CB.INDRI("cping")
async def _(client, message):
    await ping_cmd(client, message)

@CB.INDRI("kuda")
async def _(client, message):
    await message.react("🦄")

@CB.INDRI("cinta")
async def _(client, message):
    await message.react("❤")

@CB.INDRI("absen")
async def _(client, message):
    await ongjir_cmd(client, message)

@CB.INDRI("emut")
async def _(client, message):
    await devsreact_cmd(client, message)

@CB.INDRI("radd")
async def _(client, message):
    Tm = await message.reply(f"<blockquote><b>tunggu sebentar . . .</b></blockquote>")
    chat_id = message.chat.id
    blacklist = await get_chat(client.me.id)
    if chat_id in blacklist:
        return await Tm.edit(f"<blockquote><b>group ini sudah ada dalam blacklist</b></blockquote>")
    add_blacklist = await add_chat(client.me.id, chat_id)
    if add_blacklist:
        await Tm.edit(f"<blockquote><b>{message.chat.title} berhasil ditambahkan ke daftar blacklist group.</b></blockquote>")
    else:
        await Tm.edit(f"<blockquote><b>terjadi kesalahan yang tidak diketahui</b></blockquote>")
        await asyncio.sleep(2)
    return await Tm.delete() 

@CB.INDRI("rdel")
async def _(client, message):
    Tm = await message.reply(f"<blockquote><b>tunggu sebentar . . .</b></blockquote>")
    try:
        if not get_arg(message):
            chat_id = message.chat.id
        else:
            chat_id = int(message.command[1])
        blacklist = await get_chat(client.me.id)
        if chat_id not in blacklist:
            return await Tm.edit(f"<blockquote><b>{message.chat.title} tidak ada dalam daftar blacklist group.</b></blockquote>")
        del_blacklist = await remove_chat(client.me.id, chat_id)
        if del_blacklist:
            await Tm.edit(f"<blockquote><b>{chat_id}\nberhasil dihapus dari daftar blacklist group.</b></blockquote>")
        else:
            await Tm.edit(f"<blockquote><b>terjadi kesalahan yang tidak diketahui</b></blockquote>")
    except Exception as error:
        await Tm.edit(error)
        await asyncio.sleep(2)
    return await Tm.delete()

@CB.INDRI("cgcast")
async def _(client, message):
    jancok = await message.reply("**Otw Gcast Kak Ami...**")
    send = get_message(message)
    if not send:
        await m.reply_text(f"<blockquote><b>**mohon balas ke pesan** !</b></blockquote>", quote=True)
        return
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (ChatType.SUPERGROUP, ChatType.GROUP):
            chat_id = dialog.chat.id
            await asyncio.sleep(0.1)
            blacklist = await get_chat(client.me.id)
            if chat_id not in blacklist and chat_id not in BLACKLIST_CHAT:
                try:
                    await send.copy(chat_id)
                    done += 1
                except Exception:
                    pass
                   
    await client.send_message(message.chat.id, f"<blockquote><b>**berhasil mengirim ke {done} grup** <emoji id=5798623990436074786>✅</emoji><b></blockquote>\n\n")

@CB.INDRI("cungban")
async def _(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply(f"<blockquote><b>Global Unbanned Sedang Diproses....</b></blockquote>")
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        await Tm.edit(
            f"<blockquote><b><code>cungban</code> [user_id/username/reply to user]<b></blockquote>"
        )
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
    try:
        user = await client.get_users(user_id)
    except PeerIdInvalid:
        await Tm.edit(f"<blockquote><b>tidak dapat menemukan user tersebut.</b></blockquote>")
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
                return await Tm.edit(
                    f"<blockquote><b>anda tidak bisa gban dia karena dia adalah owner saya.</b></blockquote>"
                )
            elif prik in prok:
                return await Tm.edit(
                    f"<blockquote><b>anda tidak bisa gban dia, karna dia adalah admin userbot anda.</b></blockquote>"
                )
            elif udah:
                return await Tm.edit(
                    f"<blockquote><b>pengguna ini sudah di gban.</b></blockquote>"
                )
            elif prik not in prok and prik not in DEVS:
                try:
                    await add_banned_user(gua, prik)
                    await client.ban_chat_member(chat, prik)
                    iso = iso + 1
                    await asyncio.sleep(0.1)
                except BaseException:
                    gagal = gagal + 1
                    await asyncio.sleep(0.1)
    return await Tm.edit(
        f"""
<blockquote><b>global banned</b>

<u>ʙᴇʀʜᴀsɪʟ ʙᴀɴɴᴇᴅ:</u> {iso} <u>ᴄʜᴀᴛ</u>
<u>ɢᴀɢᴀʟ ʙᴀɴɴᴇᴅ:</u> {gagal} <u>ᴄʜᴀᴛ</u>
<u>ʙᴇʀʜᴀsɪʟ ᴜɴʙᴀɴɴᴇᴅ:</u> {iso} <u>ᴄʜᴀᴛ</u>
<u>ᴜsᴇʀ:</u> <a href='tg://user?id={prik}'>{user.first_name}</a></b></blockquote>
"""
                          )
