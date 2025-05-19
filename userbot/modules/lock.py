from userbot import *


__MODULE__ = "ʟᴏᴄᴋs"
__HELP__ = f"""
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʟᴏᴄᴋꜱ 』

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}lock</code> [type]
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜɴᴄɪ ɪᴢɪɴ ɢʀᴏᴜᴘ

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}unlock</code> [type]
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴋᴀ ɪᴢɪɴ ɢʀᴏᴜᴘ

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}locks</code>
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ɪᴢɪɴ sᴀᴀᴛ ɪɴɪ.

  <b>➢ ᴛʏᴘᴇ : `msg`|`media`|`stickers`|`polls`|`info`|`invite`|`webprev`|`pin`<b></blockquote>
"""


@CB.UBOT("lock|unlock")
async def _(client, message):
    await locks_func(client, message)


@CB.UBOT("locks")
async def _(client, message):
    await locktypes(client, message)
