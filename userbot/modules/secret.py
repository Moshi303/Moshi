from userbot import *

__MODULE__ = "secret"
__HELP__ = f"""
<blockquote><b>『 bantuan untuk secret 』

  <b>• perintah:</b> <code>{PREFIX[0]}msg</code> [reply to user - text]
  <b>• penjelasan:</b> untuk mengirim pesan secara rahasia.<b></blockquote>
"""


@CB.UBOT("msg")
async def _(client, message):
    await msg_cmd(client, message)


@CB.INLINE("^secret")
@INLINE.QUERY
async def _(client, inline_query):
    await secret_inline(client, inline_query)
