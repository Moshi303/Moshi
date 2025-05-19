from userbot import *

__MODULE__ = "ғᴏɴᴛ"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ғᴏɴᴛ 』</b>

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}font</code> [ʀᴇᴘʟʏ/ᴛᴇxᴛ]
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴛᴇxᴛ ғᴏɴᴛ ᴅᴇɴɢᴀɴ ᴛᴀᴍᴘɪʟᴀɴ ʏᴀɴɢ ʙᴇʀʙᴇᴅᴀ.
"""


@CB.UBOT("font")
async def _(client, message):
    await font_message(client, message)


@CB.INLINE("^get_font")
@INLINE.QUERY
async def _(client, inline_query):
    await font_inline(client, inline_query)


@CB.CALLBACK("^get")
@INLINE.DATA
async def _(client, callback_query):
    await font_callback(client, callback_query)


@CB.CALLBACK("^next")
@INLINE.DATA
async def _(client, callback_query):
    await font_next(client, callback_query)


@CB.CALLBACK("^prev")
@INLINE.DATA
async def _(client, callback_query):
    await font_prev(client, callback_query)
