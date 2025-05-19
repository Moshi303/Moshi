from userbot import *

__MODULE__ = "cek id"
__HELP__ = f"""
<blockquote><b>『 bantuan untuk showid 』

  <b>• perintah:</b> <code>{PREFIX[0]}id</code>
  <b>• penjelasan:</b> untuk mengetahui id dari user/grup/channel.

  <b>• perintah:</b> <code>{PREFIX[0]}id</code> [reply to user/media]
  <b>• penjelasan:</b> untuk mengetahui id dari user/media.

  <b>• perintah:</b> <code>{PREFIX[0]}id</code> [username user/grup/channel]
  <b>• penjelasan:</b> untuk mengetahui id user/grup/channel melalui username.<b></blockquote>
"""

@CB.UBOT("id")
async def _(client, message):
    await id_cmd(client, message)
