import asyncio

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, ChatPrivileges, Message
from pyrogram.errors import *
from pyrogram.types import *
from userbot.core.function.emoji import emoji
from userbot.config import *

from userbot import *
from pyrogram import Client, enums
from pyrogram.types import Message

absen = [
    "**Hadir Sayang** 🫶🏻",
    "**Hadir Pikachu** 👋🏻",
    "**Hadir Cintakuu** 💕",
    "**Maaf ka habis nemenin ka Ami** 🥹🥹",
    "**Maaf ka habis Anu Sama Pikachu** 😁😁",
    "**Akuuuuhhh haaadiirrrr** 😎😎",
    "**Hadir Sister** ✨",
    "**Sokap bet lu** 😼",
    "**Apasi Bawel** 🙈",
    "**Punten Kak Amii** 😇😇",
    "**Apa Cantikk** 🤧🤧",
    "**Hadir Cantikk** 🫨🫨",
    "**Apa Ami Sayang** 🥵🥵",
    
]

@CB.INDRI("oi")
async def _(client, message):
    await message.reply(choice(absen))
