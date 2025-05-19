# ini buatan sendiri y anjing 
# minimal kalo mau copy jangan hapus credit bgst


import asyncio
import random

from userbot.modules import fun2_string as tod

from userbot import *


@CB.UBOT("fun")
async def dare(client, message):
    try:        
        await message.reply(f"{random.choice(tod.FUN)}")
    except BaseException:
        pass


__MODULE__ = "ғᴜɴ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ғᴜɴ 』

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>fun
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> coba aja<b></blockquote>
  """
