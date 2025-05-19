from userbot import *
from pyrogram.raw.functions.messages import DeleteHistory
__MODULE__ = "ᴄʟᴇᴀʀ"
__HELP__ = f"""
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄʟᴇᴀʀ 』

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}clear</code>
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ʜɪsᴛᴏʀʏ.<b></blockquote>
"""


@CB.UBOT("clear")
async def _(client, message):
    user_id = message.chat.id
    bot_info = await client.resolve_peer(user_id)
    await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))
