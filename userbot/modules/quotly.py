from userbot import *

__MODULE__ = "ǫᴜᴏᴛʟʏ"
__HELP__ = """
<blockquote>❒ <i><u>Bantuan Untuk Quotly</u></i>
┃
┣ Perintah: <code>{0}q</code>
┣ Penjelasan: <i><u>Untuk merubah teks menjadi sticker.</u></i>
┃
┣ Perintah: <code>{0}qf</code> [username/userid]
┃ Penjelasan: <i><u>Untuk memanipulasi teks menjadi sticker.</u></i>
┃
┣ Perintah: <code>{0}color</code>/<code>{0}warna</code>
┖ Penjelasan: <i><u>Untuk mendapatkan Daftar Warna yang tersedia.</u></i>

<b>Notes:</b>
<b><u>Contoh Perintah:</u></b>

• <code>{0}q</code> [text/balas text/caption]
Penjelasan: <i><u>Akan mengubah caption/text yang dibalas menjadi sebuah sticker Quotly dengan latar belakang warna Default.</u></i>

• <code>{0}q</code> [warna] [text/balas text/caption]
Penjelasan: <i><u>Akan mengubah caption/text yang dibalas menjadi sebuah sticker Quotly dengan latar belakang berwarna yang ditentukan.</u></i>

• <code>{0}q</code> [jumlah pesan] [text/balas text/caption]
Penjelasan: <i><u>Akan mengubah beberapa caption/text yang dibalas menjadi sebuah sticker Quote dengan warna latar belakang default.</u></i>

• <code>{0}q</code> [jumlah pesan] [warna] [text/balas text/caption]
Penjelasan: <i><u>Akan mengubah beberapa caption/text yang dibalas menjadi sebuah sticker Quote dengan warna latar belakang yang ditentukan.</u></i>

• <code>{0}qf</code> [username/userid] [text/balas text/caption]
    Penjelasan: <i><u>Akan memanipulasi caption/text yang dibalas menjadi sebuah sticker Quotly dengan warna default.</u></i>

• <code>{0}qf</code> [username pengguna] [warna] [text/balas text/caption]
    Penjelasan: <i><u>Akan memanipulasi caption/text yang dibalas menjadi sebuah sticker Quotly berwarna yang ditentukan.</u></i> </blockquote>
"""


@CB.UBOT("q")
async def _(client, message):
    await q_cmd(client, message)


@CB.UBOT("qf")
async def _(client, message):
    await qf_cmd(client, message)


@CB.UBOT("color|warna")
async def _(client, message):
    await qcolor_cmd(client, message)
