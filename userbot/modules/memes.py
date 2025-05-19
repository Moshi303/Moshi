from userbot import *

__MODULE__ = "ᴍᴇᴍᴇs"
__HELP__ = f"""
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴍᴇᴍᴇs 』

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ: </b> <code>{PREFIX[0]}memes</code> [text]
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ sᴛɪᴋᴇʀ ᴍᴇᴍᴇs ʀᴀɴᴅᴏᴍ.<b></blockquote>
"""


@CB.UBOT("mm|memes")
async def _(client, message):
    await memes_cmd(client, message)
