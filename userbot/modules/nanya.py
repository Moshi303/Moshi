import asyncio
import random

from userbot.modules import question as tod

from userbot import *


# Ini cuma sekedar hiburan untuk para pengguna userbot
# Kalo masih baper gausah maen userbot apalagi maen userbot
# Fake Developer Userbot On Telegram By : https;//t.me/Usern4meDoestExist404

@CB.UBOT("siapaa")
async def siapa(client, message):
    split_text = message.text.split(None, 1)
    if len(split_text) < 2:
        return await message.reply("<blockquote><b>ᴋᴀsɪʜ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴋᴏɴᴛᴏʟ.<b></blockquote>")
    cot = split_text[1]
    await message.reply(f"{random.choice(tod.DEVELOPER)}")

@CB.UBOT("berikann")
async def berikan(client, message):
    split_text = message.text.split(None, 1)
    if len(split_text) < 2:
        return await message.reply("<blockquote><b>ᴋᴀsɪʜ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴋᴏɴᴛᴏʟ.<b></blockquote>")
    cot = split_text[1]
    await message.reply(f"{random.choice(tod.ITU)}")

@CB.UBOT("jelaskannn")
async def jelaskan(client, message):
    split_text = message.text.split(None, 1)
    if len(split_text) < 2:
        return await message.reply("<blockquote><b>ᴋᴀsɪʜ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴋᴏɴᴛᴏʟ.<b></blockquote>")
    cot = split_text[1]
    await message.reply(f"{random.choice(tod.BOT)}")

@CB.UBOT("manaa")
async def jelaskan(client, message):
    split_text = message.text.split(None, 1)
    if len(split_text) < 2:
        return await message.reply("<blockquote><b>ᴋᴀsɪʜ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴋᴏɴᴛᴏʟ.<b></blockquote>")
    cot = split_text[1]
    await message.reply(f"{random.choice(tod.BOTT)}")

@CB.UBOT("apaa")
async def jelaskan(client, message):
    split_text = message.text.split(None, 1)
    if len(split_text) < 2:
        return await message.reply("<blockquote><b>ᴋᴀsɪʜ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴋᴏɴᴛᴏʟ.<b></blockquote>")
    cot = split_text[1]
    await message.reply(f"{random.choice(tod.MUSIC)}")
    
    
