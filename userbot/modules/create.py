from userbot import *

__MODULE__ = "ᴄʀᴇᴀᴛᴇ"
__HELP__ = """
 <blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄʀᴇᴀᴛᴇ 』

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}buat</code> ɢᴄ ɴᴀᴍᴀ ɢᴄ
<b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ɢʀᴜᴘ ᴛᴇʟᴇɢʀᴀᴍ.

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}buat</code> ᴄʜ ɴᴀᴍᴀ ᴄʜ
<b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴇʟᴇɢʀᴀᴍ.<b></blockquote>
"""


@CB.UBOT("buat")
async def _(client, message):
    await create_grup(client, message)
