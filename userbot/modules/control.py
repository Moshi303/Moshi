from userbot import *

__MODULE__ = "ᴄᴏɴᴛʀᴏʟ"
__HELP__ = f"""
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴏɴᴛʀᴏʟ 』

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}setprefix</code> [sɪᴍʙᴏʟ ᴘʀᴇғɪx]
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ᴘʀᴇғɪx/ʜᴀɴᴅʟᴇʀ ᴄᴏᴍᴍᴀɴᴅs

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}setemoji</code> [ǫᴜᴇʀʏ] [ᴠᴀʟᴜᴇ]
  <b>➢ ǫᴜᴇʀʏ: </b>
       <b>➢ `PONG` </b>
       <b>➢ `MENTION` </b>
       <b>➢ `UBOT` </b>
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴘᴀᴅᴀ ᴛᴀᴍᴘɪʟᴀɴ ᴘᴏɴɢ ᴘᴀᴅᴀ ᴘɪɴɢ.<b></blockquote>

"""

@CB.UBOT("setprefix")
async def _(client, message):
    await setprefix(client, message)

@CB.UBOT("setemoji")
async def _(client, message):
    await change_emot(client, message)

