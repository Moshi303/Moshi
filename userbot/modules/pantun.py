
import asyncio
import random

import requests
from pyrogram import *
from pyrogram import filters
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.types import *
from pyrogram.types import Message

from userbot import *
from userbot.core.helpers.basic import edit_or_reply, get_text
from userbot.core.helpers.constants import MEMES

DEFAULTUSER = "ubot"

@CB.UBOT("lipkol")
async def ngelipkol(client, message):
    mg = await edit_or_reply(message, "**kk it gmw call ma ak kh?** 🥹🥹")
    await asyncio.sleep(1.5)
    await mg.edit("**yakin ni gmau call ma ak?** 😖")
    await asyncio.sleep(1.5)
    await mg.edit("**gmau denger suara aku yg berdemeg ini kah kak?** 🗿")
    await asyncio.sleep(1.5)
    await mg.edit("**nanti aku ceritain sejarahnya katak bijer loh kak** 😭")
    await asyncio.sleep(1.5)
    await mg.edit("**yug kak lipkol eum** 🤧")
    await asyncio.sleep(1.5)
    await mg.edit("**nit kol anet ni akuh** 😫")
    await asyncio.sleep(1.5)
    await mg.edit("**aku call ya kak eum** 🥺")
    await asyncio.sleep(1.5)
    await mg.edit("**OTW CALL KAMU KAK NGENGGG...** 😘😘")

@CB.UBOT("nikah")
async def ngenikah(client, message):
    e = await edit_or_reply(message, "**Kak nikah yug**")
    await asyncio.sleep(2)
    await e.edit("**nanti biar anu kya gini**")
    await asyncio.sleep(1)
    await e.edit("🤵🏻     👰🏻")
    await asyncio.sleep(1)
    await e.edit("🤵🏻    👰🏻")
    await asyncio.sleep(1)
    await e.edit("🤵🏻   👰🏻")
    await asyncio.sleep(1)
    await e.edit("🤵🏻👶🏻👰🏻")
    await asyncio.sleep(1)
    await e.edit("**NAH GITU**")
    
@CB.UBOT("pantun1")
async def ngepantun(client, message):
    mg = await edit_or_reply(message, "**SAYANG AKU PUNYA PANTUN NI BUAT KAMU**")
    await asyncio.sleep(1.5)
    await mg.edit("**Dua tiga makan ketoprak**")
    await asyncio.sleep(1.5)
    await mg.edit("**Mau kah mukamu ku depak?**")

@CB.UBOT("pantun2")
async def ngepantun(client, message):
    mg = await edit_or_reply(message, "**SAYANG AKU PUNYA PANTUN NI BUAT KAMU**")
    await asyncio.sleep(1.5)
    await mg.edit("**ikan hiu nelayang layang**")
    await asyncio.sleep(1.5)
    await mg.edit("**i love u sayang** 🥺😘")
    await asyncio.sleep(1.5)
    await mg.edit("**anjay kewlazzz ang ang ang ang**")

@CB.UBOT("pantun3")
async def ngepantun(client, message):
    mg = await edit_or_reply(message, "**SAYANG AKU PUNYA PANTUN NI BUAT KAMU**")
    await asyncio.sleep(1.5)
    await mg.edit("**ikan hiu naik perahu**")
    await asyncio.sleep(1.5)
    await mg.edit("**i can't stop thinking about you** 🥹")
    await asyncio.sleep(1.5)
    await mg.edit("**anjay kewlazzz ang ang ang ang**")

@CB.UBOT("pantun4")
async def ngepantun(client, message):
    mg = await edit_or_reply(message, "**SAYANG AKU PUNYA PANTUN NI BUAT KAMU**")
    await asyncio.sleep(1.5)
    await mg.edit("**Ikan hiu makan perahu**")
    await asyncio.sleep(1.5)
    await mg.edit("**i love you kamoeh** 🫨")
    await asyncio.sleep(1.5)
    await mg.edit("**btw kol yu**")

@CB.UBOT("pantun5")
async def ngepantun(client, message):
    mg = await edit_or_reply(message, "**SAYANG AKU PUNYA PANTUN NI BUAT KAMU**")
    await asyncio.sleep(1.5)
    await mg.edit("**makan pempek makan kerupuk**")
    await asyncio.sleep(1.5)
    await mg.edit("**lagi capek pengen di pukpuk** 🥺🥺")
    

__MODULE__ = "ᴘᴀɴᴛᴜɴ"
__HELP__ = """
<blockquote><b>Bantuan Untuk Gombal
<code>{0}lipkol</code>
<code>{0}pantun1</code>
<code>{0}pantun2</code>
<code>{0}pantun3</code>
<code>{0}pantun4</code>
<code>{0}pantun5</code><b></blockquote>
"""
