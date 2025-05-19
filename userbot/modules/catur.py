from userbot import *
__MODULE__ = "ɢᴀᴍᴇ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴀᴍᴇ 』

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}catur</code></code>
  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍᴀɪɴᴋᴀɴ ɢᴀᴍᴇ ᴄᴀᴛᴜʀ.
  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}game</code></code>
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍᴀɪɴᴋᴀɴ ɢᴀᴍᴇ ʀᴀɴᴅᴏᴍ.
  <b>➢ ɴᴏᴛᴇ : ᴊᴜᴍʟᴀʜ ᴍᴇɴᴜ 𝟻𝟶+ ɢᴀᴍᴇ <b></blockquote>
"""



@CB.UBOT("catur")
async def _(client, message):
    await catur_cmd(client, message)
    

@CB.UBOT("game")
async def _(client, message):
    await game_cmd(client, message)
