from userbot import *

__MODULE__ = "telegraph"
__HELP__ = f"""
<blockquote><b>『 bantuan untuk telegraph 』

  <b>• perintah:</b> <code>{PREFIX[0]}tg</code> [reply media/text]
  <b>• penjelasan:</b> untuk mengapload media/text ke telegra.ph<b></blockquote>
"""


@CB.UBOT("tg")
async def _(client, message):
    await tg_cmd(client, message)
