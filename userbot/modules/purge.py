from userbot import *

__MODULE__ = "purge"
__HELP__ = f"""
<blockquote><b>『 bantuan untuk purge 』

  <b>• perintah:</b> <code>{PREFIX[0]}purge</code> [reply to message]
  <b>• penjelasan:</b> bersihkan (hapus semua pesan) obrolan dari pesan yang dibalas hingga yang terakhir

  <b>• perintah:</b> <code>{PREFIX[0]}del</code> [reply to message]
  <b>• penjelasan:</b> hapus pesan yang dibalas

  <b>• perintah:</b> <code>{PREFIX[0]}purgeme</code> [number of messages]
  <b>• penjelasan:</b> hapus pesan anda sendiri dengan menentukan total pesan.<b></blockquote>
"""


@CB.UBOT("del")
async def _(client, message):
    await del_cmd(client, message)


@CB.UBOT("purgeme")
async def _(client, message):
    await purgeme_cmd(client, message)


@CB.UBOT("purge")
async def _(client, message):
    await purge_cmd(client, message)
