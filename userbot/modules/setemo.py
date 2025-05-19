from userbot import *
from pyrogram.types import EmojiStatus, MessageEntity
from pyrogram.enums import MessageEntityType

__MODULE__ = "setemo"
__HELP__ = f"""
<blockquote><b>『 bantuan untuk setemo 』

  <b>• perintah:</b> <code>{PREFIX[0]}setemo</code> [reply to user - text]
  <b>• penjelasan:</b> untuk mengganti emoji status.<b></blockquote>
"""

@CB.UBOT("setemo")
async def _(client, message):
    try:
        target = message.reply_to_message
        if not target:
            await message.reply_text(f"<blockquote><b>**mohon balas ke pesan** !<b></blockquote>", quote=True)
            return
        entity = target.entities[0]
        custom_emoji_id = entity.custom_emoji_id
        chat_id = message.chat.id
        success = await client.set_emoji_status(EmojiStatus(custom_emoji_id=custom_emoji_id))
        if success:
            my_emoji_str = f"<blockquote><b>**emoji status berhasil di ganti ke** <emoji id={custom_emoji_id}>{target.text}</emoji><b></blockquote>"
            await message.reply_text(my_emoji_str, quote=True)
                    
    except Exception as e:
        await message.reply_text(e)