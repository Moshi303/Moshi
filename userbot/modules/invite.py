from userbot import *

__MODULE__ = "ɪɴᴠɪᴛᴇ"
__HELP__ = f"""
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɪɴᴠɪᴛᴇ 』

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}invite</code> [ᴜsᴇʀɴᴀᴍᴇ] 
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜɴᴅᴀɴɢ ᴀɴɢɢᴏᴛᴀ ᴋᴇ ɢʀᴜᴘ ᴀɴᴅᴀ

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}inviteall</code> [ᴜsᴇʀɴᴀᴍᴇ_ɢʀᴏᴜᴘ - ᴄᴏʟʟᴅᴏᴡɴ=ᴅᴇᴛɪᴋ ᴘᴇʀ ɪɴᴠɪᴛᴇ]
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜɴᴅᴀɴɢ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ᴏʙʀᴏʟᴀɴ ɢʀᴜᴘ ʟᴀɪɴ ᴋᴇ ᴏʙʀᴏʟᴀɴ ɢʀᴜᴘ ᴀɴᴅᴀ

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}cancel</code>
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴᴠɪᴛᴇᴀʟʟ.<b></blockquote>
  """


@CB.UBOT("invite")
async def _(client, message):
    await invite_cmd(client, message)


@CB.UBOT("inviteall")
async def _(client, message):
    await inviteall_cmd(client, message)


@CB.UBOT("cancel")
async def _(client, message):
    await cancel_cmd(client, message)
