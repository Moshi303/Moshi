from userbot import *


__MODULE__ = "audio"
__HELP__ = f"""
<blockquote><b>『 bantuan untuk text to audio 』

  <b>• perintah:</b> <code>{PREFIX[0]}tts</code> [reply/text]
  <b>• penjelasan:</b> untuk merubah tect menjadi menjadi pesan suara

  <b>• perintah:</b> <code>{PREFIX[0]}bahasa</code>
  <b>• penjelasan:</b> untuk merubah bahasa text to audio

  note : atur bahasa daulu untuk menggunakan fitur ini.<b></blockquote>
"""

@CB.UBOT("tts")
async def _(client, message):
    await tts_cmd(client, message)
