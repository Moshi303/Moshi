from userbot import *

__MODULE__ = "sangmata"
__HELP__ = f"""
<blockquote><b>『 bantuan untuk sangmata 』

  <b>• perintah:</b> <code>{PREFIX[0]}sg</code> [user_id/reply user]
  <b>• penjelasan:</b> untuk memeriksa histori nama/username.<b></blockquote>
"""


@CB.UBOT("sg")
async def _(client, message):
    await sg_cmd(client, message)
