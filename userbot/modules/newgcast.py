from userbot import *
from pyrogram.enums import ChatType, ChatMemberStatus
from userbot.core.database.saved import get_chat


__MODULE__ = "ɢᴄᴀsᴛɴᴇᴡ"
__HELP__ = f"""
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴄᴀsᴛɴᴇᴡ 』

  <b>• perintah:</b> <code>{PREFIX[0]}bc</code> gc balas ke pesan
  <b>• penjelasan:</b> gc[grup], adm[khusus admin], pv [private chat]<b></blockquote>
"""

def get_message(message):
    msg = (
        message.reply_to_message
        if message.reply_to_message
        else ""
        if len(message.command) < 2
        else " ".join(message.command[1:])
    )
    return msg

@CB.UBOT("bc")
async def _(c, m):
    done = 0
    if len(m.command) != 2:
        await m.reply(f"<blockquote><b>mohon gunakan format: bc [gc adm pv] **<b></blockquote>")
        return
    send = get_message(m)
    if not send:
        await m.reply_text(f"<blockquote><b>**mohon balas ke pesan** !<b></blockquote>")
        return
    if not m.reply_to_message:
        await m.reply_text(f"<blockquote><b>**mohon balas ke pesan** !<b></blockquote>")
        return
    blacklist = await get_chat(c.me.id)
    try:
        if m.command[1] == "gc":
            Haku = await m.reply(f"**sedang memproses**...")
            async for dialog in c.get_dialogs():
                if dialog.chat.type in (ChatType.SUPERGROUP, ChatType.GROUP):
                    chat_id = dialog.chat.id
                    await asyncio.sleep(0.1)
                    if chat_id not in blacklist:
                        try:
                            await send.copy(chat_id)
                            done += 1
                        except Exception:
                            pass

            await Haku.edit(
                f"<blockquote><b>ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢɪʀɪᴍ ᴋᴇ {done} ɢʀᴏᴜᴘ.<b></blockquote>\n\n"
                f"<blockquote><b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ {bot.me.mention}<b></blockquote>\n")

        elif m.command[1] == "pv":
            Haku = await m.reply(f"ᴘʀᴏᴄᴇssɪɴɢ...")
            async for dialog in c.get_dialogs():
                if dialog.chat.type == ChatType.PRIVATE:
                    chat_id = dialog.chat.id
                    await asyncio.sleep(0.1)
                    if chat_id not in blacklist:
                        try:
                            await send.copy(chat_id)
                            done += 1
                        except Exception:
                            pass

            await Haku.edit(
                f"<blockquote><b>ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢɪʀɪᴍ ᴋᴇ {done} ᴜsᴇʀ.<b></blockquote>\n\n"
                f"<blockquote><b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ {bot.me.mention}<b></blockquote>\n")

        elif m.command[1] == "adm":
            Haku = await m.reply(f"ᴘʀᴏᴄᴇssɪɴɢ...")
            async for dialog in c.get_dialogs():
                if dialog.chat.type in (ChatType.SUPERGROUP, ChatType.GROUP):
                    chat_id = dialog.chat.id
                    await asyncio.sleep(0.1)
                    try:
                        member = await c.get_chat_member(chat_id, "me")
                        if member.status in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
                            await send.copy(chat_id)
                            done += 1
                    except Exception:
                        pass
            await Haku.edit(
                f"<blockquote><b>ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢɪʀɪᴍ ᴋᴇ {done} ᴀᴅᴍɪɴ.<b></blockquote>\n\n"
                f"<blockquote><b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ {bot.me.mention}<b></blockquote>\n")


    except IndexError:
        await m.reply(f"<blockquote><u>ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ʙᴄ ɢᴄ|ᴀᴅᴍ|ᴘᴠ ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ</u></blockquote>")
