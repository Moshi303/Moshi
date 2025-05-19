import os
import asyncio 
import random

from pyrogram import *
from pyrogram.types import *
from userbot import *
from userbot.config import DEVS
from userbot.core.helpers.basic import edit_or_reply, get_text, get_user
from pyrogram import Client, filters
from .help import *
from userbot import bot, ubot
from pyrogram import __version__
from pyrogram.enums import *

OWNER = os.environ.get("OWNER", None)
BIO = os.environ.get("BIO", "Hi Fake, How About You?")

CLONE_STORAGE = {}

@CB.UBOT("clone")
async def clone(client: Client, message: Message):
    text = get_text(message)
    Tm = await edit_or_reply(message, "**Waiting 3 Seconds for cloning...**")
    userk = get_user(message, text)[0]
    user_id = await extract_user(message)
    user_ = await client.get_users(userk)
    if user_id in DEVS:
        return await message.reply(
             "<blockquote><b>**Perintah ini Dilarang digunakan Kepada Developer Saya**<b></blockquote>"
        )
    get_bio = await client.get_chat(user_.id)
    f_name = user_.first_name
    c_bio = get_bio.bio
    pic = user_.photo.big_file_id
    poto = await client.download_media(pic)

    await client.set_profile_photo(photo=poto)
    await client.update_profile(
        first_name=f_name,
        bio=c_bio,
    )
    await message.edit(f"**Hi I'M** __{f_name}__")


@CB.UBOT("revert")
async def revert(client: Client, message: Message):
    user = await client.get_users("me")
    CLONE_STORAGE[user] = {
        "first_name": CLONE_STORAGE[user]["first_name"],
        "last_name": CLONE_STORAGE[user]["last_name"],
        "profile_id": CLONE_STORAGE[user]["profile_id"],
        "bio_data": CLONE_STORAGE[user]["bio_data"],
    }
    try:
        clone_data = CLONE_STORAGE.get(user.id)
        photos = [p async for p in client.get_chat_photos("me")]
        if photos:
            await client.delete_profile_photos(photos[0].file_id)
        if clone_data["first_name"]:
            await client.update_profile(
                first_name=clone_data["first_name"],
                last_name=clone_data["last_name"],
                bio=clone_data["bio_data"]
            )
        else:
            return await message.reply_text("User doesn't have a profile bio and last name")
        await message.reply_text("Successfully reverted back to your account!")
        del CLONE_STORAGE[user]
    except RPCError as rpc_error:
        await message.reply_text(f"RPCError: {rpc_error}")
    except Exception as e:
        await message.reply_text(f"Error: {e}")

__MODULE__ = "ᴄʟᴏɴᴇ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄʟᴏɴᴇ 』
<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}clone</code> [user_id/username/reply user]
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɪʀᴜ ᴀᴛᴀᴜ ᴍᴇɴʏᴀᴍᴀʀ sᴇʙᴀɢᴀɪ sᴇsᴇᴏʀᴀɴɢ ʏɢ sᴜᴅᴀʜ ᴅɪ ᴄʟᴏɴᴇ.

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}revert</code> [user_id/username/reply user]
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴋᴇᴍʙᴀʟɪ ᴍᴇɴᴊᴀᴅɪ ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ ᴋᴀʟɪᴀɴ sᴇᴛᴇʟᴀʜ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴄʟᴏɴɴɪɴɢ.<b></blockquote>
  """
