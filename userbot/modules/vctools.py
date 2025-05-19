__MODULE__ = "vctools"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴠᴄᴛᴏᴏʟꜱ 』

• Perintah: <code>{0}startvc</code>
• Penjelasan: Untuk memulai voice chat grup.

• Perintah: <code>{0}stopvc</code>
• Penjelasan: Untuk mengakhiri voice chat grup.

• Perintah: <code>{0}joinvc</code>
• Penjelasan: Untuk bergabunf voice chat grup.

• Perintah: <code>{0}leavevc</code>
• Penjelasan: Untuk meninggalkan voice chat grup.<b></blockquote>
"""

from asyncio import sleep
from contextlib import suppress
from random import randint
from typing import Optional
from pytgcalls.exceptions import *
from pyrogram import Client, enums
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message
from pyrogram.errors import *
from userbot import *

async def get_group_call(

    client: Client, message: Message, err_msg: str = ""

) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (
                await client.invoke(GetFullChannel(channel=chat_peer))
            ).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await eor(message, f"<blockquote><b>**No group call Found** {err_msg}<b></blockquote>")
    return False



@CB.UBOT("leavevc")
async def leave_vc(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)
    grp = await EMO.BL_GROUP(client)
    ktrn = await EMO.BL_KETERANGAN(client)
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    chat_id = int(chat_id)
    calls = await client.call_py.calls
    chat_call = calls.get(chat_id)
    mex = await message.reply(f"<b>{prs} ᴘʀᴏᴄᴄᴇsɪɴɢ...</b>")
    if chat_call == None:
        return await mex.edit(f"<blockquote>{ggl} ❏ <u>ɴᴀᴍᴀ</u>: <b><a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a></b> \n{ktrn} ├ <u>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴀᴋᴜɴ ʟᴜ ʙᴇʟᴏᴍ ᴅɪ ᴏs.</u>\n{grp} ╰ <u>ɢʀᴏᴜᴘ</u>: {message.chat.title}</blockquote>")
    else:
        try:
            await client.call_py.leave_call(chat_id)
            await mex.edit(f"<blockquote><b>{brhsl} ❏ <u>ɴᴀᴍᴀ</u>: <b><a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a></b> \n{ktrn} ├ <u>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴛᴜʀᴜɴ ᴅᴀʀɪ ᴏs.</u>\n{grp} ╰ <u>ɢʀᴏᴜᴘ</u>: {message.chat.title}</blockquote>")
        except (BaseException, Exception) as x:
            return await mex.edit(f"<blockquote><b>{x}</b></blockquote>")

@CB.UBOT("joinvc")
async def join_vc(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)
    grp = await EMO.BL_GROUP(client)
    ktrn = await EMO.BL_KETERANGAN(client)
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    chat_id = int(chat_id)
    calls = await client.call_py.calls
    chat_call = calls.get(chat_id)
    mex = await message.reply(f"<b>{prs} ᴘʀᴏᴄᴄᴇsɪɴɢ...</b>")
    if chat_call == None:
        try:
            await client.call_py.play(chat_id)
            await client.call_py.mute_stream(chat_id)
            await mex.edit(f"<blockquote>{brhsl} ❏ <u>ɴᴀᴍᴀ</u>: <b><a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a></b> \n{ktrn} ├ <u>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ɴᴀɪᴋ ᴋᴇ ᴏs.</u>\n{grp} ╰ <u>ɢʀᴏᴜᴘ</u>: {message.chat.title}</blockquote>")
        except (BaseException, Exception) as x:
            return await mex.edit(f"<blockquote>{x}</b></blockquote>")
    else:
        return await mex.edit(f"<blockquote>{ggl} ❏ <u>ɴᴀᴍᴀ</u>: <b><a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a></b> \n{ktrn} ├ <u>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴀᴋᴜɴ ʟᴜ ᴜᴅᴀʜ ᴅɪ ᴏs.</u>\n{grp} ╰ <u>ɢʀᴏᴜᴘ</u>: {message.chat.title}</blockquote>")

def run_sync(func, *args, **kwargs):
    return get_event_loop().run_in_executor(None, partial(func, *args, **kwargs)) 
            
@CB.UBOT("startvc")
async def opengc(client: Client, message: Message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)
    grp = await EMO.BL_GROUP(client)
    ktrn = await EMO.BL_KETERANGAN(client)
    ky = await message.reply(f"{prs} **ᴍᴇᴍᴘʀᴏsᴇs....**")
    vctitle = get_arg(message)
    if message.chat.type == "channel":
        chat_id = message.chat.title
    else:
        chat_id = message.chat.id
    args = f"<blockquote>{brhsl} ❏ <u>ɴᴀᴍᴀ</u>: <b><a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a></b> \n{ktrn} ├ <u>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴍᴇᴍᴜʟᴀɪ ᴏs.</u>\n{grp} ╰ <u>ɢʀᴏᴜᴘ</u>: {message.chat.title}</blockquote>"
    try:
        if not vctitle:
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                )
            )
        else:
            args += f"\n<blockquote><b> • <b>ᴛɪᴛʟᴇ ᴏs {vctitle}<b></blockquote>"
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                    title=vctitle,
                )
            )
        await ky.edit(args)
    except Exception as e:
        await ky.edit(f"<blockquote><b>INFO: `{e}`<b></blockquote>")

@CB.UBOT("stopvc")
async def end_vc_(client: Client, message: Message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)
    grp = await EMO.BL_GROUP(client)
    ktrn = await EMO.BL_KETERANGAN(client)
    ky = await message.reply(f"<blockquote><b>{brhsl} **ᴍᴇᴍᴘʀᴏsᴇs....**<b></blockquote>")
    if not (group_call := await get_group_call(client, message, err_msg="Error...")):
        return
    await client.invoke(DiscardGroupCall(call=group_call))
    await ky.edit(f"<blockquote>{brhsl} ❏ <u>ɴᴀᴍᴀ</u>: <b><a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a></b> \n{ktrn} ├ <u>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴍᴇᴍᴀᴛɪᴋᴀɴ ᴏs.</u>\n{grp} ╰ <u>ɢʀᴏᴜᴘ</u>: {message.chat.title}</blockquote>")

@CB.UBOT("cjvc")
@CB.OWNER
async def _(c: ubot, m):
    ky = await m.reply("<b>Processing...</b>")
    chat_id = m.command[1] if len(m.command) > 1 else m.chat.id
    
    try:
        for X in c._ubot:
            try:
                await X.call_py.play(chat_id)
                await X.call_py.mute_stream(chat_id)
            except (
                ChannelInvalid,
                NoActiveGroupCall,
                AlreadyJoinedError,
                GroupCallNotFound,
            ):
                continue
        await ky.delete()
        ae = await m.reply(
            "<blockquote><b>✅ Berhasil Naik Os:\nChat ID: `{}`\nTotal Userbot: {}</b><blockquote>".format(chat_id, len(ubot._ubot)
            )
        )
        await sleep(3)
        return await ae.delete()
    except Exception as e:
        await ky.delete()
        return await m.reply("**Gagal `{}`**".format(str(e)))

@CB.UBOT("clvc")
@CB.OWNER
async def _(c: ubot, m):
    ky = await m.reply(_("proses").format(em.proses, proses_))
    chat_id = m.command[1] if len(m.command) > 1 else m.chat.id
    sk = 0
    gl = 0
    if "/+" in str(chat_id):
        gid = await c.get_chat(str(chat_id))
        chat_id = int(gid.id)
    elif "t.me/" in str(chat_id) or "@" in str(chat_id):
        chat_id = chat_id.replace("https://t.me/", "")
        gid = await c.get_chat(str(chat_id))
        chat_id = int(gid.id)
    else:
        chat_id = int(chat_id)
    try:
        for X in nlx._ubot:
            try:
                await X.call_py.leave_call(chat_id)
                sk += 1
            except:
                gl += 1
                continue
        await ky.delete()
        return await m.reply(
            "<b>{} Berhasil Turun Os:\nChat ID: `{}`\nSukses `{}`\nGagal `{}`\nDari Total Userbot: {}</b>".format(
                em.sukses, chat_id, sk, gl, len(nlx._ubot)
            )
        )
    except Exception as e:
        await ky.delete()
        return await m.reply(_("err").format(em.gagal, e))
