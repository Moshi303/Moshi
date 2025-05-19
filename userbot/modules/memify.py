from userbot import *

__MODULE__ = "memify"
__HELP__ = f"""
<blockquote><b>『 bantuan untuk memify 』

  <b>• perintah:</b> <code>{PREFIX[0]}mmf</code> [text]
  <b>• penjelasan:</b> balas ke sticker atau foto akan di ubah menjadi sticker teks meme yang di tentukan.<b></blockquote>
"""


@CB.UBOT("mmf|memify")
async def _(client, message):
    await memify_cmd(client, message)
