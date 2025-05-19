from userbot import *

__MODULE__ = "qrcode"
__HELP__ = f"""
<blockquotes><b>『 bantuan untuk qrcode 』

  <b>• perintah:</b> <code>{PREFIX[0]}qrGen</code> [text qrcode]
  <b>• penjelasan:</b> untuk merubah qrcode text menjadi gambar

  <b>• perintah:</b> <code>{PREFIX[0]}qrRead</code> [reply to media]
  <b>• penjelasan:</b> untuk merubah qrcode menjadi text.<b></blockquote>
"""

@CB.UBOT("qrgen")
async def _(client, message):
    await qr_gen_cmd(client, message)


@CB.UBOT("qrread")
async def _(client, message):
    await qr_read_cmd(client, message)
