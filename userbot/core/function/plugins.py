from importlib import import_module
from platform import python_version

from pyrogram import __version__
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from userbot import bot, ubot
from userbot.config import OWNER_ID
from userbot.core.helpers import CB
from userbot.modules import loadModule

HELP_COMMANDS = {}


async def loadPlugins():
    modules = loadModule()
    for mod in modules:
        imported_module = import_module(f"userbot.modules.{mod}")
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                HELP_COMMANDS[
                    imported_module.__MODULE__.replace(" ", "_").lower()
                ] = imported_module
    print(f"[🤖 @{bot.me.username} 🤖] [💠 TELAH BERHASIL DIAKTIFKAN! 💠]")
    TM = await bot.send_message(
        OWNER_ID,
        f"""
<blockquote><b>🤖 {bot.me.mention} ʙᴇʀʜᴀsɪʟ ᴅɪᴀᴋᴛɪғᴋᴀɴ.

<b>📁 ᴍᴏᴅᴜʟᴇs: {len(HELP_COMMANDS)}</b>
<b>📘 ᴘʏᴛʜᴏɴ: {python_version()}</b>
<b>📙 ᴘʏʀᴏɢʀᴀᴍ: {__version__}</b>

<b>👤 ᴜsᴇʀʙᴏᴛ: {len(ubot._ubot)}<b></blockquote>
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🛠️ gitpull", callback_data="gitpull"),
                    InlineKeyboardButton("restart 🔁", callback_data="restart"),
                ],
            ]
        ),
    )
    
    

@CB.CALLBACK("0_cls")
async def _(client, callback_query):
    await callback_query.message.delete()
    
