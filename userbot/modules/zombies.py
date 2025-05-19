from userbot import *
from pyrogram.errors.exceptions.bad_request_400 import ChannelInvalid

__MODULE__ = "zombies"
__HELP__ = f"""
<blockquote><b>>『 bantuan untuk zombies 』

  <b>• perintah:</b> <code>{PREFIX[0]}zombies</code>
  <b>• penjelasan:</b> untuk mengeluarkan akun terhapus digrup anda.<b></blockquote>
"""

@CB.UBOT("zombies")
async def zombies_cmd(client, message):
    try:
        chat_id = message.chat.id
        deleted_users = []
        banned_users = 0
        Tm = await message.reply("<blockquote><b>sedang memeriksa<b></blockquote>")
        async for i in client.get_chat_members(chat_id):
            if i.user.is_deleted:
                deleted_users.append(i.user.id)
        if len(deleted_users) > 0:
            for deleted_user in deleted_users:
                try:
                    banned_users += 1
                    await message.chat.ban_member(deleted_user)
                except Exception:
                    pass
            await Tm.edit(f"<blockquote><b>berhasil mengeluarkan {banned_users} akun terhapus.<b></blockquote>")
        else:
            await Tm.edit(f"<blockquote><b>tidak ada akun terhapus di group ini.<b></blockquote>")
    except ChannelInvalid:
        await Tm.edit(f"<blockquote><b>**Gunakan Di Grup.**<b></blockquote>")