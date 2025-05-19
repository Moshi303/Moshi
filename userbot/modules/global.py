from userbot import *

__MODULE__ = "ɢʟᴏʙᴀʟ"
__HELP__ = f"""
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢʟᴏʙᴀʟ 』

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}gban</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ]
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ʙᴀɴɴᴇᴅ ᴜsᴇʀ ᴅᴀʀɪ sᴇᴍᴜᴀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ 

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}ungban</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ]
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴜɴʙᴀɴɴᴇᴅ ᴜsᴇʀ ᴅᴀʀɪ sᴇᴍᴜᴀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}listgban</code>
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴀғᴛᴀʀ ᴘᴇɴɢɢᴜɴᴀ ɢʙᴀɴ.<b></blockquote>
"""


@CB.UBOT("gban")
async def _(client, message):
    await global_banned(client, message)

@CB.INDRI("cgban")
async def _(client, message):
    await global_banned(client, message)


@CB.UBOT("ungban")
async def _(client, message):
    await cung_ban(client, message)


@CB.UBOT("listgban")
async def _(client, message):
    await gbanlist(client, message)
