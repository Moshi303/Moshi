import random

from userbot.modules import kodam_string as tod

from userbot import *

__MODULE__ = "ᴋʜᴏᴅᴀᴍ"
__HELP__ = """
<blockquote>❏──「<u>ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴋʜᴏᴅᴀᴍ</u>」──❏
➢ ᴘᴇʀɪɴᴛᴀʜ: <code>cekkodam</code>
  ➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ: <u>ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴋʜᴏᴅᴀᴍ.</u>
➢ ᴘᴇʀɪɴᴛᴀʜ: <code>cekkntl</code>
  ➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ: <u>ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴋᴏɴᴛᴏʟ.</u>
➢ ᴘᴇʀɪɴᴛᴀʜ: <code>cektt</code>
  ➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ: <u>ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴛᴇᴛᴇ.</u></blockquote>
  """

@CB.UBOT("cekkntl")
async def kontol(client, message):
    try:      
        await message.reply(f"{random.choice(tod.KNTL)}")
    except BaseException:
        pass

@CB.UBOT("cektt")
async def tete(client, message):
    try:      
        await message.reply(f"{random.choice(tod.TT)}")
    except BaseException:
        pass
      
@CB.UBOT("cekkodam")
async def kodam(client, message):
    try:      
        await message.reply(f"{random.choice(tod.KODAM)}")
    except BaseException:
        pass