
from userbot import ubot
import os






async def jumlah_user(client, message):
    tt = await message.reply("sebentar proses...")
    xx = len(ubot._ubot)
    await tt.edit(f"jumlah pengguna userbot : {xx}")

















async def cb_restart(client, callback_query):
    await callback_query.message.delete()
    os.system(f"kill -9 {os.getpid()} && python3 -m userbot")


async def cb_gitpull(client, callback_query):
    await callback_query.message.delete()
    os.system(f"kill -9 {os.getpid()} && git pull && python3 -m userbot")
