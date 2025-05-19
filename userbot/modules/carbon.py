from userbot import *

__MODULE__ = "ᴄᴀʀʙᴏɴ"
__HELP__ = f"""
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴀʀʙᴏɴ』

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}carbon</code> [reply/text]
  <b➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇᴋs ᴄᴀʀʙᴏɴᴀʀ.<b></blockquote>
"""

@CB.UBOT("carbon")
async def _(client, message):
    await carbon_func(client, message)
