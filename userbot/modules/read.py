from userbot import *

__MODULE__ = "read"
__HELP__ = f"""
<blockquote><b>『 bantuan untuk baca 』

  <b>• perintah:</b> <code>{PREFIX[0]}bacagc</code>
  <b>• penjelasan:</b> untuk membaca semua pesan yang belum terbaca.<b></blockquote>
"""
from pyrogram import Client, idle, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.types import ChatMember
from pyrogram.errors.exceptions import UserNotParticipant

@CB.UBOT("bacapc")
async def baca_read(client, message):
    Mai = await message.reply_text(f"Proccesing...")
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == ChatType.PRIVATE:
            user_id = dialog.chat.id
            anjai = await client.read_chat_history(user_id)
            if anjai:
                done += 1
    await Mai.edit_text(f"<blockquote><b>**Berhasil Membaca Pesan Dari : {done} User**✅<b></blockquote>")
