
__MODULE__ = "ʟᴏɢs"
__HELP__ = """
<blockquote><b>ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢʀᴏᴜᴘ ʟᴏɢs

➢ ᴘᴇʀɪɴᴛᴀʜ: <code>{0}logger</code> [ᴏɴ/ᴏғғ]
➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴀᴛᴀᴜ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ɢʀᴜᴘ ʟᴏɢ.

➢ : <code>{0}logger on</code> ➛  ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ɢʀᴜᴘ ʟᴏɢ.
➢ : <code>{0}logger off</code> ➛  ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ɢʀᴜᴘ ʟᴏɢ.<b></blockquote>
"""



import asyncio
from pyrogram.enums import *
from pyrogram.errors import FloodWait
from pyrogram.types import *
from userbot import *


async def create_botlog(client):
    name = "RynUbot Logs"
    desc = "❒ ᴊᴀɴɢᴀɴ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ɢʀᴜᴘ ʟᴏɢ ɪɴɪ\n└ ᴘᴏᴡᴇʀᴇᴅ ʙʏ: @{bot.me.mention}"
    group = await client.create_supergroup(name, desc)
    nt = wget.download("https://telegra.ph/file/65bb7e66f28f7d249aaf3.jpg")
    photo_video = {"video": nt} if nt.endswith(".mp4") else {"photo": nt}
    kntl = group.id
    await client.set_chat_photo(kntl, **photo_video)
    await client.send_message(
        kntl,
        f"<blockquote><b>**❒ ɢʀᴏᴜᴘ ʟᴏɢs ʙᴇʀʜᴀsɪʟ ᴅɪʙᴜᴀᴛ\n└ ᴋᴀᴍᴜ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ sɪɴɪ ᴀᴋᴜ ᴄᴀʙᴜʟɪɴ ʀᴀᴍᴇ𝟸!!!**<b></blockquote>",
    )
    return kntl
   

@CB.UBOT("LOGS_GROUP", ubot)
async def _(client, message):
    log = await get_vars(client.me.id, "TAG_LOG")
    if not log:
        return
    if message.chat.id == 777000:
        return
    from_user = (
        message.chat if message.chat.type == ChatType.PRIVATE else message.from_user
    )
    if message.sender_chat:
        if message.sender_chat.username is None:
            user_link = f"{message.sender_chat.title}"
        else:
            user_link = f"[{message.sender_chat.title}](https://t.me/{message.sender_chat.username}"
    else:
        user_link = f"[{message.from_user.first_name} {message.from_user.last_name or ''}](tg://user?id={message.from_user.id})"
    message_link = (
        message.link
        if message.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP)
        else f"tg://openmessage?user_id={from_user.id}&message_id={message.id}"
    )
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        text = f"""
📨 <b><u>Group Notifications</u></b>

• <b>Name Group: {message.chat.title}</b>
• <b>ID Group:</b> <code>{message.chat.id}</code>
• <b>From: {user_link}</b>
• <b>Message:</b> <blockquote>{message.text}</blockquote>
• <b>Link Message: [Here]({message_link}) </blockquote>
"""
        try:
            await asyncio.sleep(0.5)
            return await client.send_message(
                int(log), text, disable_web_page_preview=True
            )
        except ChatForwardsRestricted:
            return f"Error ChatForwardsRestricted {message.chat.id}"
        except MessageIdInvalid:
            return f"Error MessageIdInvalid {message.chat.id}"
        except ChannelPrivate:
            return f"Error ChannelPrivate {message.chat.id}"
        except FloodWait as e:
            await asyncio.sleep(e.value)
            return await client.send_message(
                int(log), text, disable_web_page_preview=True
            )
    else:
        text = f"""
📨 <b><u>Private Notifications</u></b>

• <b>From: {user_link}</b>
• <b>Message:</b> <blockquote>{message.text}</blockquote>
• <b>Link Message: [Here]({message_link}) </b>
"""
        try:
            await asyncio.sleep(0.5)
            await client.send_message(int(log), text, disable_web_page_preview=True)
            return await message.forward(int(log))
        except (ChatForwardsRestricted, MessageIdInvalid, ChatWriteForbidden):
            pass
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await client.send_message(int(log), text, disable_web_page_preview=True)
            return await message.forward(int(log))


@CB.UBOT("logger")
async def _(client, message):
    xx = await message.reply(f"ʙᴇɴᴛᴀʀ ɢᴜᴀ ʙᴜᴀᴛɪɴ ᴅᴜʟᴜ ʟᴏɢsɴʏᴀ...")
    cek = get_arg(message)
    logs = await get_vars(client.me.id, "TAG_LOG")
    if cek.lower() == "on":
        if logs is None:
            ajg = await create_botlog(client)
            babi = await client.export_chat_invite_link(int(ajg))
            await set_vars(client.me.id, "TAG_LOG", int(ajg))
            return await xx.edit(f"ʟᴏɢs ɢʀᴏᴜᴘ ʙᴇʀʜᴀsɪʟ ᴅɪᴀᴋᴛɪғᴋᴀɴ:\n\n{babi}")
        else:
            return await xx.edit(f"ʟᴏɢs ɢʀᴏᴜᴘ ᴀɴᴅᴀ sᴜᴅᴀʜ ᴀᴋᴛɪғ.")
    if cek.lower() == "off":
        if logs is not None:
            await client.delete_supergroup(int(logs))
            await remove_vars(client.me.id, "TAG_LOG")
            return await xx.edit(f"ʟᴏɢs ɢʀᴏᴜᴘs ʙᴇʀʜᴀsɪʟ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ.\n\n{babi}")
        else:
            return await xx.edit(f"ʟᴏɢs ɢʀᴏᴜᴘs ᴀɴᴅᴀ sᴜᴅᴀʜ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ.")
    else:
        return await xx.edit(
            f"ғᴏʀᴍᴀᴛ ʏᴀɴɢ ᴀɴᴅᴀ ʙᴇʀɪᴋᴀɴ sᴀʟᴀʜ. sɪʟᴀʜᴋᴀɴ ɢᴜɴᴀᴋᴀɴ <code>{message.text} on/off</code>"
        )
