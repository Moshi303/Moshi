from userbot import *
from userbot.core.database.saved import get_chat
from pyrogram import Client
from pyrogram import errors
from pyrogram import enums
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors.exceptions.not_acceptable_406 import ChannelPrivate


__MODULE__ = "ᴊᴏɪɴʟᴇᴀᴠᴇ"
__HELP__ = f"""
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴊᴏɪɴʟᴇᴀᴠᴇ 』

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}kickme</code>
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ɢʀᴜᴘ

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}join</code> [ᴜꜱᴇʀɴᴀᴍᴇɢᴄ]
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴊᴏɪɴ ᴋᴇ ɢʀᴜᴘ ᴍᴇʟᴀʟᴜɪ ᴜꜱᴇʀɴᴀᴍᴇ 

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}leaveallgc</code>
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ꜱᴇᴍᴜᴀ ɢʀᴜᴘ ʏᴀɴɢ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ/ᴏᴡɴᴇʀ

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}leaveallmute</code>
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ꜱᴇᴍᴜᴀ ɢʀᴜᴘ ʏᴀɴɢ ᴍᴇᴍʙᴀᴛᴀsɪ ᴀɴᴅᴀ

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}leaveallch</code>
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ꜱᴇᴍᴜᴀ ᴄʜᴀɴɴᴇʟ ʏᴀɴɢ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ/ᴏᴡɴᴇʀ

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}leave</code> [ᴜsᴇʀɴᴀᴍᴇɢᴄ]
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ɢʀᴜᴘ ᴍᴇʟᴀʟᴜɪ ᴜsᴇʀɴᴀᴍᴇ.<b></blockquote>
"""


@CB.UBOT("kickme|leave")
async def _(client, message):
    await leave(client, message)


@CB.UBOT("join")
async def _(client, message):
    await join(client, message)


@CB.UBOT("leaveallgc")
async def _(client, message):
    done = 0
    Haku = await message.reply(f"ᴘʀᴏᴄᴇssɪɴɢ...")
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (ChatType.SUPERGROUP, ChatType.GROUP):
            chat_id = dialog.chat.id
            await asyncio.sleep(0.1)
            try:
                member = await client.get_chat_member(chat_id, "me")
                if member.status not in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
                    done += 1
                    await client.leave_chat(chat_id)
            except Exception:
                pass
    await Haku.edit(f"<blockquote><b>ʙᴇʀʜᴀsɪʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ {done} ɢʀᴜᴘ ʏᴀɴɢ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ/ᴏᴡɴᴇʀ ✅<b></blockquote>")

@CB.UBOT("leaveallmute")
async def _(client, message):
    done = 0
    Haku = await message.reply(f"ᴘʀᴏᴄᴇssɪɴɢ...")
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (ChatType.SUPERGROUP, ChatType.GROUP):
            chat_id = dialog.chat.id
            try:
                member = await client.get_chat_member(chat_id, "me")
                if member.status == ChatMemberStatus.RESTRICTED:
                    await client.leave_chat(chat_id)
                    done += 1
            except Exception:
                pass
    await Haku.edit(f"<blockquote>ʙᴇʀʜᴀsɪʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ {done} ɢʀᴜᴘ ʏᴀɴɢ ᴍᴇᴍʙᴀᴛᴀsɪ ᴋᴀᴍᴜ</blockquote>")


@CB.UBOT("leaveallch")
async def _(client, message):
    await kickmeallch(client, message)


