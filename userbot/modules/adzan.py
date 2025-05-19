# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan | @Usern4meDoestExist404
# Kok Bacot
# © @KynanSupport | @CidSupport | @CariTemanSahabatInline_Id
# FULL MONGO NIH JING FIX MULTI CLIENT

import json

import requests
from pyrogram import filters

from userbot import *

__MODULE__ = "ᴀᴅᴢᴀɴ"
__HELP__ = f"""
<blockquote><b>√ Bantuan Untuk Adzan

๏ Perintah: <code>{0}adzan</code> [nama kota]
◉ Penjelasan: Untuk mengetahui jadwal adzan di lokasi anda.</b><blockquote>
"""


@CB.UBOT("adzan")
async def _(client, message):
    LOKASI = message.text.split(None, 1)[1]
    if len(message.command) < 2:
        return await eor(message, "<b>Silahkan Masukkan Nama Kota Anda</b>")
    url = f"http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
    request = requests.get(url)
    if request.status_code != 200:
        await eor(message, f"<b>Maaf Tidak Menemukan Kota <code>{LOKASI}</code>")
    result = json.loads(request.text)
    catresult = f"""
<blockquote><b>ᴊᴀᴅᴡᴀʟ sʜᴏʟᴀᴛ ʜᴀʀɪ ɪɴɪ

<b>ᴛᴀɴɢɢᴀʟ</b> <code>{result['items'][0]['date_for']}</code>
<b>ᴋᴏᴛᴀ</b> <code>{result['query']} | {result['country']}</code>

<b>ᴛᴇʀʙɪᴛ:</b> <code>{result['items'][0]['shurooq']}</code>
<b>sᴜʙᴜʜ:</b> <code>{result['items'][0]['fajr']}</code>
<b>ᴅᴢᴜʜᴜʀ:</b> <code>{result['items'][0]['dhuhr']}</code>
<b>ᴀsʜᴀʀ:</b> <code>{result['items'][0]['asr']}</code>
<b>ᴍᴀɢʜʀɪʙ:</b> <code>{result['items'][0]['maghrib']}</code>
<b>ɪsʏᴀ:</b> <code>{result['items'][0]['isha']}</code></b><blockquote>
"""
    await eor(message, catresult)
