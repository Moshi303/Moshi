from pyrogram.enums import SentCodeType
from datetime import datetime
from userbot import bot, ubot
from time import time
from pyrogram.errors import *
from pyrogram.types import *

from userbot import *


async def ohaja(client, callback_query):
    user_id = callback_query.from_user.id
    if not user_id not in ubot._get_my_id:
        buttons = [
            [
                InlineKeyboardButton("kembali", callback_data=f"home {user_id}"),                
            ]
        ]
        exp = await get_expired_date(user_id)
        prefix = await get_pref(user_id)
        waktu = exp.strftime("%d-%m-%Y") if exp else "None"
        uptime = await get_time((time() - start_time))
        return await callback_query.edit_message_text(
            f"""
<blockquote><b>>{username}
 <b>status :</b> <code>premium</code>
  <b>prefixes :</b> <code>{prefix[0]}</code>
  <b>expired_on:</b> <code>{waktu}</code>
  <b>bot_uptime : <code>{uptime}</code><b>/blockquote>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        
    else:
        buttons = [
            [
                InlineKeyboardButton("kembali", callback_data=f"home {user_id}"),
            ]
        ]
        return await callback_query.edit_message_text(
            f"""
<blockquote><b>**Anda belum memiliki userbot silahkan beli userbot terlebih dahulu.**<b>/blockquote>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
    )
