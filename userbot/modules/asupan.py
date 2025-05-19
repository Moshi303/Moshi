from userbot import *

__MODULE__ = "ᴀsᴜᴘᴀɴ"
__HELP__ = f"""
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀsᴜᴘᴀɴ 』

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}asupan</code>
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴠɪᴅᴇᴏ ᴀsᴜᴘᴀɴ ʀᴀɴᴅᴏᴍ.

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}cewek</code>
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴀᴘ ᴄᴇᴡᴇ ʀᴀɴᴅᴏᴍ.

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}cowok</code>
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴀᴘ ᴄᴏᴡᴏ ʀᴀɴᴅᴏᴍ.

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}anime</code>
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ғᴏᴛᴏ ᴀɴɪᴍᴇ.
  
  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}bokep</code>
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀʀɪ ᴠɪᴅᴇᴏ ʙᴏᴋᴇᴘ.<b></blockquote>
"""


@CB.UBOT("asupan")
async def _(client, message):
    await video_asupan(client, message)


@CB.UBOT("cewek")
async def _(client, message):
    await photo_cewek(client, message)


@CB.UBOT("cowok")
async def _(client, message):
    await photo_cowok(client, message)


@CB.UBOT("anime")
async def _(client, message):
    await photo_anime(client, message)


@CB.UBOT("bokep")
async def _(client, message):
    await video_bokep(client, message)
