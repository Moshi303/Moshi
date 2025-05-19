import asyncio
import random

from userbot.modules import truth_or_dare_string as tod

from userbot import *


@CB.UBOT("apakah")
async def apakah(client, message):
    split_text = message.text.split(None, 1)
    if len(split_text) < 2:
        return await message.reply("<blockquote><b>**Kasih Pertanyaannya Kontol.**<b></blockquote>")
    cot = split_text[1]
    await message.reply(f"{random.choice(tod.AP)}")


@CB.UBOT("knp")
async def kenapa(client, message):
    split_text = message.text.split(None, 1)
    if len(split_text) < 2:
        return await message.reply("<blockquote><b>**Kasih Pertanyaannya Kontol.**<b></blockquote>")
    cot = split_text[1]
    await message.reply(f"{random.choice(tod.KN)}")


@CB.UBOT("bagaimana")
async def bagaimana(client, message):
    split_text = message.text.split(None, 1)
    if len(split_text) < 2:
        return await message.reply("<blockquote><b>**Kasih Pertanyaannya Kontol.**<b></blockquote>")
    cot = split_text[1]
    await message.reply(f"{random.choice(tod.BG)}")


@CB.UBOT("dare")
async def dare(client, message):
    try:        
        await message.reply(f"{random.choice(tod.DARE)}")
    except BaseException:
        pass

@CB.UBOT("truth")
async def truth(client, message):
    try:
        await message.reply(f"{random.choice(tod.TRUTH)}")
    except Exception:
        pass


__MODULE__ = "ᴛᴏᴅ"
__HELP__ = """
<blockquote><b>『 truth & dare 』

  <b>• perintah:</b> <code>dare
  <b>• penjelasan:</b> coba aja
  
  <b>• perintah:</b> <code>truth
  <b>• penjelasan:</b> coba aja
  
  <b>• perintah:</b> <code>apakah 
  <b>• penjelasan:</b> coba aja
  
  <b>• perintah:</b> <code>bagaimana 
  <b>• penjelasan:</b> coba aja
  
  <b>• perintah:</b> <code>kenapa
  <b>• penjelasan:</b> coba aja<b></blockquote>
  """
