from userbot import *
import psutil
import time

import random
from datetime import datetime
from pyrogram import __version__
from pyrogram.enums import *
from platform import python_version
from userbot import bot, ubot
from userbot.modules import loadModule
from pyrogram.methods.chats.get_dialogs import GetDialogs
from os import environ, getpid, execle
from time import time
from userbot.core.database.permit import *
from userbot.core.helpers.formatter import *

from pyrogram.raw.functions import Ping
from pyrogram.types import (InlineKeyboardMarkup, InlineQueryResultArticle,
                            InputTextMessageContent)


__MODULE__ = "ᴀʟɪᴠᴇ"
__HELP__ = """
<blockquote><b> 『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀʟɪᴠᴇ 』

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}alive</code></code>
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:<b> ᴄᴏʙᴀɪɴ ᴀᴊᴀ ʙɪᴀʀ ʟᴜ ᴛᴀᴜ sᴇɴᴅɪʀɪ.<b></blockquote>
"""


@CB.CALLBACK("sys_stats")
@INLINE.DATA
async def _sys_callback(
    client,
    cq: CallbackQuery,
):
    text = sys_stats()
    await bot.answer_callback_query(
        cq.id,
        text,
        show_alert=True,
    )

def sys_stats():
    cpu = psutil.cpu_percent()
    mem = (
        psutil.virtual_memory().percent
    )
    disk = psutil.disk_usage(
        "/"
    ).percent
    process = psutil.Process(getpid())
    stats = f"""
-----------------------
uptime: {time_formatter((time() - start_time) * 1000)}
bot: {round(process.memory_info()[0] / 1024 ** 2)} MB
cpu: {cpu}%
ram: {mem}%
disk: {disk}%
-----------------------
"""
    return stats


@CB.UBOT("alive")
async def alive_cmd(client, message):
    x = await client.get_inline_bot_results(
        bot.me.username, f"alive {message.id} {client.me.id}"
    )
    await message.reply_inline_bot_result(x.query_id, x.results[0].id, quote=True)
   
  
@CB.INLINE("^alive")
async def _(client, inline_query):
    get_id = inline_query.query.split()
    len(ubot._ubot)
    for my in ubot._ubot:
        if int(get_id[2]) == my.me.id:
            users = 0
            group = 0
            async for dialog in my.get_dialogs(limit=None):
                if dialog.chat.type == enums.ChatType.PRIVATE:
                    users += 1
                elif dialog.chat.type in (
                    enums.ChatType.GROUP,
                    enums.ChatType.SUPERGROUP,
                ):
                    group += 1
            get_exp = await get_expired_date(my.me.id)
            if get_exp is None:
                expired = ""
            else:
                exp = get_exp.strftime("%d-%m-%Y")
                expired = f"<code>{exp}</code>"
            if my.me.id == OWNER_ID:
                status = "**official**"
            else:
                status = "**unofficial**"
            antipm = None
            cekpc = await get_vars(my.me.id, "ENABLE_PM_GUARD")
            if not cekpc:
                antipm = "disable"
            else:
                antipm = "enable"
            button = [
                [
                    InlineKeyboardButton(
                        text="ᴛᴜᴛᴜᴘ",
                        callback_data=f"alv_cls {int(get_id[1])} {int(get_id[2])}",
                    ),
                    InlineKeyboardButton(
                        text="sᴛᴀᴛs",
                        callback_data="sys_stats"
                    ),
                ]
            ]
            start = datetime.now()
            await my.invoke(Ping(ping_id=0))
            ping = (datetime.now() - start).microseconds / 1000
            uptime = await get_time((time() - start_time))
            msg = f"""
<blockquote><u>ǫᴜᴇᴇɴ ᴜsᴇʀʙᴏᴛ</u>
     <u>sᴛᴀᴛᴜs:</b> [{status}]
        <u>ᴅᴇᴠɪᴄᴇ_ᴍᴏᴅᴇʟ:</u> <code>Sweet</code>
        <u>ᴍᴀɢɪsᴋ_ʜɪᴅᴇ:</u> <code>{antipm}</code>
        <u>ᴍᴀɢɪsᴋ_ᴍᴏᴅᴜʟᴇ:</u> <code>{len(ubot._ubot)}</code>
        <u>ᴄᴘᴜ_ᴍᴏᴅᴇʟ:</u> <code>snapdragon</code>
        <u>ᴋᴇʀɴᴇʟ_ᴠᴇʀsɪᴏɴ:</u> <code>genom R{group}-{users}</code>
        <u>ᴅᴇᴠɪᴄᴇ_ᴠᴇʀsɪᴏɴ:</u> <code>14.0.2</code>
        <u>ʙᴀsᴇʙᴀɴᴅ_ᴠᴇʀsɪᴏɴ:</u> <code>unknown</code>
        <u>ᴅᴇᴠɪᴄᴇ_ᴘɪɴɢ:</u> <code>{ping}</code>
        <u>ᴅᴇᴠɪᴄᴇ_ᴜᴘᴛɪᴍᴇ:</u> <code>{uptime}</code>
        <u>sᴇᴄᴜʀɪᴛʏ_ᴘᴀᴛᴄʜ:</u> <code>{expired}</blockquote>
"""
            await client.answer_inline_query(
                inline_query.id,
                cache_time=300,
                results=[
                    (
                        InlineQueryResultArticle(
                            title="💬",
                            reply_markup=InlineKeyboardMarkup(button),
                            input_message_content=InputTextMessageContent(msg),
                        )
                    )
                ],
            )
         
      
      

@CB.CALLBACK("alv_cls")
@INLINE.DATA
async def alive_close(client, callback_query):
    get_id = callback_query.data.split()
    if not callback_query.from_user.id == int(get_id[2]):
        return await callback_query.answer(
            f"❌ ᴛᴏᴍʙᴏʟ ɪɴɪ ʙᴜᴋᴀɴ ᴜɴᴛᴜᴋᴍᴜ. {callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}",
            True,
        )
    unPacked = unpackInlineMessage(callback_query.inline_message_id)
    for my in ubot._ubot:
        if callback_query.from_user.id == int(my.me.id):
            await my.delete_messages(
                unPacked.chat_id, [int(get_id[1]), unPacked.message_id]
  )
