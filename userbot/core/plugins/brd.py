import asyncio
import random

from gc import get_objects
from asyncio import sleep
from pyrogram.raw.functions.messages import DeleteHistory, StartBot
from pyrogram.enums import ChatType
from pyrogram.errors.exceptions import FloodWait
from pyrogram.types import *

from userbot import *

async def add_auto_text(client, text):
    auto_text = await get_vars(client.me.id, "AUTO_TEXT") or []
    auto_text.append(text)
    await set_vars(client.me.id, "AUTO_TEXT", auto_text)

async def get_data_id(client, query):
    chat_types = {
        "global": [ChatType.CHANNEL, ChatType.GROUP, ChatType.SUPERGROUP],
        "all": [ChatType.GROUP, ChatType.SUPERGROUP, ChatType.PRIVATE],
        "group": [ChatType.GROUP, ChatType.SUPERGROUP],
        "users": [ChatType.PRIVATE],
    }
    return [dialog.chat.id async for dialog in client.get_dialogs() if dialog.chat.type in chat_types.get(query, [])]

async def limit_cmd(client, message):
    ggl = await JANCOK.GAGAL(client)
    sks = await JANCOK.BERHASIL(client)
    prs = await JANCOK.PROSES(client)
    pong = await JANCOK.PING(client)
    tion = await JANCOK.MENTION(client)
    yubot = await JANCOK.UBOT(client)
    await client.unblock_user("SpamBot")
    bot_info = await client.resolve_peer("SpamBot")
    msg = await message.reply(f"<blockquote><b>{prs} processing . . .<b></blockquote>")
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
        print(pjg)
        if pjg <= 100:
            if client.me.is_premium:
                text = f"""
<blockquote><b>{pong} status akun premium : true {sks}
{tion} limit check : akun anda tidak dibatasi {sks}
{yubot} ubot : {bot.me.mention}<b></blockquote>
"""
            else:
                text = f"""
<blockquote><b>status akun : beli prem dulu ya
limit check : akun anda tidak di batasi
ubot : {bot.me.mention}<b></blockquote>
"""
            await client.send_message(message.chat.id, text)
            return await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))
        else:
            if client.me.is_premium:
                text = f"""
<blockquote><b>{pong} status akun premium : true
{tion} limit check : akun anda bermasalah{ggl} 
{yubot} ubot : {bot.me.mention}<b></blockquote>
"""
            else:
                text = f"""
<blockquote><b>status akun : beli prem dulu ya
limit check : akun anda bermasalah
ubot : {bot.me.mention}<b></blockquote>
"""
            await client.send_message(message.chat.id, text)
            return await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))
    else:
        print("<blockquote><b>Status tidak valid atau status text tidak ada.<b></blockquote>")

gcast_progress = False

async def babi_gcast(client, message):
    global gcast_progress
    gcast_progress = True
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    gcs = await EMO.BROADCAST(client)
    xbot = await EMO.MENTION(client)
    _msg = f"{prs} ʙᴇɴᴛᴀʀ ʙɢ ʟᴀɢɪ ᴘʀᴏsᴇs..."
    bcs = await message.reply(_msg)
    if not message.reply_to_message:
        return await bcs.edit(f"<blockquote><u>{ggl} ᴅɪ ʀᴇᴘʟʏ ʏᴀ ɢᴏʙʟᴏᴋ !.</u></blockquote>")
        await sleep(1)

    countdown = 10
    for i in range(countdown, 0, -1):
        await bcs.edit(f"<blockquote><b>{prs} ɴɪʜ <code>{i}</code> ᴅᴇᴛɪᴋ ɢᴀ ᴀᴅᴀ ɢᴄᴀsᴛ ʏɢ ᴅɪ ᴄᴀɴᴄᴇʟ ᴋᴀɴ?\n<b>ɢᴜɴᴀᴋᴀɴ</b> <code>/stopg</code> <b>ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴇɴᴛɪᴋᴀɴ ɢᴄᴀsᴛ<b></blockquote>")
        await asyncio.sleep(1)
    await bcs.edit(f"<blockquote><b>{prs} ᴏᴛᴡ ɢᴄᴀsᴛ ɴɢᴇɴɢɢɢ.....<b></blockquote>")
    text = message.reply_to_message
    chats = await get_data_id(client, "group")
    blacklist = await get_chat(client.me.id)
    done = 0
    failed = 0
    for chat_id in chats:
        if chat_id in blacklist or chat_id in BLACKLIST_CHAT:
            continue
        
        if not gcast_progress:
            break
        try:
            await text.copy(chat_id)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await text.copy(chat_id)
            done += 1
        except Exception:
            failed += 1
            pass
    if client.me.is_premium:
        await bcs.delete()
        _bcs = f"""
<blockquote>{brhsl} <u>ɢᴄᴀsᴛ ᴍᴜ ᴛᴇʟᴀʜ ʙᴇʀʜᴀsɪʟ.</u> {gcs}
{brhsl} ❏ <u>ʙᴇʀʜᴀsɪʟ ɢᴄᴀsᴛ ᴋᴇ {done} <u>ɢʀᴏᴜᴘ.</u>\n{ggl} ╰ <u>ɢᴀɢᴀʟ ɢᴄᴀsᴛ ᴋᴇ</u> {failed} ɢʀᴏᴜᴘ.</u>
{xbot} <u>ᴘᴏᴡᴇʀᴇᴅ ʙʏ:</u> {bot.me.mention}
{ktrng} <u>ᴋᴇᴛᴇʀᴀɴɢᴀɴ:</u> <code>grup</code></blockquote>
"""
    else:
        await bcs.delete()
        _bcs = f"""
<blockquote>{brhsl} <u>ɢᴄᴀsᴛ ᴍᴜ ᴛᴇʟᴀʜ ʙᴇʀʜᴀsɪʟ.</u> {gcs}
{brhsl} ❏ <u>ʙᴇʀʜᴀsɪʟ</u> <code>{done}</code> <u>ɢʀᴏᴜᴘ.</u>\n{ggl} ╰ <u>ɢᴀɢᴀʟ</u> <code>{failed}</code> <u>ɢʀᴏᴜᴘ.</u>
{xbot} ❏ <u>ᴘᴏᴡᴇʀᴇᴅ ʙʏ:</u> {bot.me.mention}
{ktrng} ╰ <u>ᴋᴇᴛᴇʀᴀɴɢᴀɴ:</u> <code>grup</code></blockquote>
"""
    return await message.reply(_bcs)

async def babi_cancel(client, message):
    global gcast_progress
    gcast_progress = False
    await message.reply(f"<blockquote><u>ᴏᴋᴇ ʙᴇʀʜᴀsɪʟ ᴅɪ ʙᴀᴛᴀʟɪɴ ɴɪʜ.</u></blockquote>")
    await sleep(0.5)

async def babi_gukes(client, message):
    prs = await JANCOK.PROSES(client)
    brhsl = await JANCOK.BERHASIL(client)
    ggl = await JANCOK.GAGAL(client)
    bcs = await JANCOK.BROADCAST(client)
    _msg = f"{prs} **proccesing...**"
    gcs = await message.reply(_msg)
    if not message.reply_to_message:
        return await gcs.edit(f"<blockquote><b>{ggl} mohon balas ke pesan !.<b></blockquote>")
    text = message.reply_to_message
    chats = await get_data_id(client, "users")
    blacklist = await get_list_from_vars(client.me.id, "BL_ID")
    done = 0
    failed = 0
    for chat_id in chats:
        if chat_id in blacklist or chat_id in BLACKLIST_CHAT:
            continue

        try:
            await text.copy(chat_id)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await text.copy(chat_id)
            done += 1
        except Exception:
            failed += 1
            pass

    await gcs.delete()
    _gcs = f"""
<blockquote><b>{bcs}broadcast user done.
{brhsl} berhasil {done} user
{ggl} gagal {failed} user.<b></blockquote>
"""
    return await message.reply(_gcs)


async def babi_brd(client, message):
    prs = await JANCOK.PROSES(client)
    brhsl = await JANCOK.BERHASIL(client)
    ggl = await JANCOK.GAGAL(client)
    bcs = await JANCOK.BROADCAST(client)
    
    _msg = f"{prs} **proses...**"
    gcs = await message.reply(_msg)

    command, text = extract_type_and_msg(message)
    
    if command not in ["group", "users", "all"] or not text:
        return await gcs.edit(f"<blockquote><b>{ggl}{message.text.split()[0]} type [reply]<b></blockquote>")

    if not message.reply_to_message:
        return await gcs.edit(f"<blockquote><b>{ggl}{message.text.split()[0]} type [reply]<b></blockquote>")

    chats = await get_data_id(client, command)
    blacklist = await get_list_from_vars(client.me.id, "BL_ID")

    done = 0
    failed = 0
    for chat_id in chats:
        if chat_id in blacklist or chat_id in BLACKLIST_CHAT:
            continue

        try:
            if message.reply_to_message:
                await message.reply_to_message.forward(chat_id)
            else:
                await text.forward(chat_id)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            if message.reply_to_message:
                await message.reply_to_message.forward(chat_id)
            else:
                await text.forward(chat_id)
            done += 1
        except Exception:
            failed += 1
            pass

    await gcs.delete()
    _gcs = f"""
<blockquote><b>{bcs}broadcast fordward done.
{brhsl} berhasil {done} ɢʀᴏᴜᴘ.
{ggl} gagal {failed} ɢʀᴏᴜᴘ.<b></blockquote>
"""
    return await message.reply(_gcs)

AG = []
LT = []


async def babi_auto(client, message):
    prs = await JANCOK.PROSES(client)
    brhsl = await JANCOK.BERHASIL(client)
    bcs = await JANCOK.BROADCAST(client)
    mng = await JANCOK.MENUNGGU(client)
    ggl = await JANCOK.GAGAL(client)   
    msg = await message.reply(f"{prs}**proses...**")
    type, value = extract_type_and_text(message)
    auto_text_vars = await get_vars(client.me.id, "AUTO_TEXT")

    if type == "on":
        if not auto_text_vars:
            return await msg.edit(
                f"<blockquote><b>{ggl} harap setting text terlebih dahulu.<b></blockquote>"
            )

        if client.me.id not in AG:
            await msg.edit(f"<blockquote><b>{brhsl} auto gcast di aktifkan.<b></blockquote>")

            AG.append(client.me.id)

            done = 0
            while client.me.id in AG:
                delay = await get_vars(client.me.id, "DELAY_GCAST") or 1
                blacklist = await get_list_from_vars(client.me.id, "BL_ID")
                txt = random.choice(auto_text_vars)

                group = 0
                async for dialog in client.get_dialogs():
                    if (
                        dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP)
                        and dialog.chat.id not in blacklist
                    ):
                        try:
                            await asyncio.sleep(1)
                            await client.send_message(dialog.chat.id, f"{txt} {random.choice(range(999))}")
                            group += 1
                        except FloodWait as e:
                            await asyncio.sleep(e.value)
                            await client.send_message(dialog.chat.id, f"{txt} {random.choice(range(999))}")
                            group += 1
                        except Exception:
                            pass

                if client.me.id not in AG:
                    return

                done += 1
                await msg.reply(f"""
<blockquote><b>{bcs}auto_gcast done
putaran {done}
{brhsl} berhasil {group} group.
{mng} wait {delay} minutes.<b></blockquote>
""",
                    quote=True,
                )
                await asyncio.sleep(int(60 * int(delay)))
        else:
            return await msg.delete()

    elif type == "off":
        if client.me.id in AG:
            AG.remove(client.me.id)
            return await msg.edit(f"<blockquote><b>{brhsl} auto gcast dinonaktifkan<b></blockquote>")
        else:
            return await msg.delete()

    elif type == "text":
        if not value:
            return await msg.edit(
                f"<blockquote><b>{ggl}{message.text.split()[0]} text - [value]<b></blockquote>"
            )
        await add_auto_text(client, value)
        return await msg.edit(f"<blockquote><b>{brhsl} berhasil di simpan.<b></blockquote>")

    elif type == "delay":
        if not int(value):
            return await msg.edit(
                f"<blockquote><b>{ggl}{message.text.split()[0]} delay - [value]<b></blockquote>"
            )
        await set_vars(client.me.id, "DELAY_GCAST", value)
        return await msg.edit(
            f"<blockquote><b>{brhsl} barhasil ke setting {value} menit.<b></blockquote>"
        )

    elif type == "remove":
        if not value:
            return await msg.edit(
                f"<blockquote><b>{ggl}{message.text.split()[0]} remove - [value]<b></blockquote>"
            )
        if value == "all":
            await set_vars(client.me.id, "AUTO_TEXT", [])
            return await msg.edit(f"<blockquote><b>{brhsl} semua text berhasil dihapus<b></blockquote>")
        try:
            value = int(value) - 1
            auto_text_vars.pop(value)
            await set_vars(client.me.id, "AUTO_TEXT", auto_text_vars)
            return await msg.edit(
                f"<blockquote><b>{brhsl} text ke {value+1} berhasil dihapus.<b></blockquote>"
            )
        except Exception as error:
            return await msg.edit(str(error))

    elif type == "list":
        if not auto_text_vars:
            return await msg.edit(f"<blockquote><b>{ggl} auto gcast text kosong.<b></blockquote>")
        txt = "<blockquote><b>daftar auto gcast text.<b></blockquote>\n\n"
        for num, x in enumerate(auto_text_vars, 1):
            txt += f"{num}> {x}\n\n"
        txt += f"\n<blockquote><b>untuk menghapus text:\n{message.text.split()[0]} remove [angka/all]<b></blockquote>"
        return await msg.edit(txt)

    elif type == "limit":
        if value == "off":
            if client.me.id in LT:
                LT.remove(client.me.id)
                return await msg.edit(f"<blockquote><b>{brhsl} auto cek limit dinonaktifkan.<b></blockquote>")
            else:
                return await msg.delete()

        elif value == "on":
            if client.me.id not in LT:
                LT.append(client.me.id)
                await msg.edit(f"<blockquote><b>{brhsl} auto cek limit started.<b></blockquote>")
                while client.me.id in LT:
                    for x in range(2):
                        await limit_cmd(client, message)
                        await asyncio.sleep(5)
                    await asyncio.sleep(1200)
            else:
                return await msg.delete()
        else:
             return await msg.edit(f"<blockquote><b>{ggl}{message.text.split()[0]} limit - [value]<b></blockquote>")

    else:
        return await msg.edit(f"<blockquote><b>{ggl}{message.text.split()[0]} [query] - [value]<b></blockquote>")
