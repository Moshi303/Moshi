from userbot import *

__MODULE__ = "ʙʟᴀᴄᴋʟɪsᴛ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙʟᴀᴄᴋʟɪsᴛ ᴄʜᴀᴛ. 』

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}addbl</code>
  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍᴀsᴜᴋᴋᴀɴ ɢʀᴜᴘs ᴋᴇ ᴅᴀғᴛᴀʀ ʜɪᴛᴀᴍ sᴜᴘᴀʏᴀ ɢᴄᴀsᴛ ᴋᴀʟɪᴀɴ ᴛɪᴅᴀᴋ ᴍᴀsᴜᴋ ᴋᴇ ɢʀᴜᴘs [ʟᴀᴋᴜᴋᴀɴ ᴅɪ ɢʀᴜᴘs, sᴇʟᴀɪɴ ᴅɪ ɢʀᴜᴘs ʙᴏᴛ ᴛɪᴅᴀᴋ ᴀᴋᴀɴ ᴍᴇʀᴇsᴘᴏɴ.]

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}unbl</code>
  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ɢʀᴜᴘs ᴅᴀʀɪ ᴅᴀғᴛᴀʀ ʜɪᴛᴀᴍ ᴀɢᴀʀ ɢᴄᴀsᴛ ʙɪsᴀ ᴍᴀsᴜᴋ ᴋᴇ ɢʀᴜᴘs [ʟᴀᴋᴜᴋᴀɴ ᴅɪ ɢʀᴜᴘs, sᴇʟᴀɪɴ ᴅɪ ɢʀᴜᴘs ʙᴏᴛ ᴛɪᴅᴀᴋ ᴀᴋᴀɴ ᴍᴇʀᴇsᴘᴏɴ.]
  
  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}rallbl</code>
  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs sᴇᴍᴜᴀ ʙʟᴀᴄᴋʟɪsᴛ ɢʀᴜᴘs.
  
  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}listbl</code>
  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍᴇʀɪᴋsᴀ ᴅᴀғᴛᴀʀ ʙʟᴀᴄᴋʟɪsᴛ ɢʀᴜᴘs.<b></blockquote>
"""
  
  
@CB.UBOT("addbl")
async def _(client, message):
    await add_blaclist(client, message)


@CB.UBOT("unbl")
async def _(client, message):
    await del_blacklist(client, message)


@CB.UBOT("rallbl")
async def _(client, message):
    await rem_all_blacklist(client, message)


@CB.UBOT("listbl")
async def _(client, message):
    await get_blacklist(client, message)
