import re

from importlib import import_module

from pyrogram.types import *

from userbot import *
from userbot.core.function.emoji import emoji


@CB.UBOT("help")
async def user_help(client, message):
    try:
        x = await client.get_inline_bot_results(bot.me.username, "user_help")
        await message.reply_inline_bot_result(x.query_id, x.results[0].id)
    except Exception as error:
        await message.reply(error)

@CB.INLINE("^user_help")
@INLINE.QUERY
async def user_help_inline(client, inline_query):
    SH = await ubot.get_prefix(inline_query.from_user.id)
    msg = f"<blockquote><b>❏ ʜᴇʟᴘ: <a href=tg://user?id={inline_query.from_user.id}>{inline_query.from_user.first_name} {inline_query.from_user.last_name or ''}</a> </b>\n<b>├  ᴘʀᴇғɪxᴇs: {' '.join(SH)}</b>\n<b>╰  ᴄᴏᴍᴍᴀɴᴅs: {len(HELP_COMMANDS)}\nᴄʀᴇᴀᴛᴇ ʙʏ : {bot.me.mention}<b></blockquote>"
    results = [InlineQueryResultArticle(
        title="Help Menu!",
        reply_markup=InlineKeyboardMarkup(paginate_modules(0, HELP_COMMANDS, "help")),
        input_message_content=InputTextMessageContent(msg),
    )]
    await client.answer_inline_query(inline_query.id, cache_time=60, results=results)


@CB.CALLBACK("help_(.*?)")
# @INLINE.DATA
async def help_callback(client, callback_query):
    mod_match = re.match(r"help_module\((.+?)\)", callback_query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", callback_query.data)
    next_match = re.match(r"help_next\((.+?)\)", callback_query.data)
    back_match = re.match(r"help_back", callback_query.data)
    SH = await ubot.get_prefix(callback_query.from_user.id)
    top_text = f"<blockquote><b>❏ ʜᴇʟᴘ: <a href=tg://user?id={callback_query.from_user.id}>{callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}</a> </b>\n<b>├  ᴘʀᴇғɪxᴇs: {' '.join(SH)}</b>\n<b>╰  ᴄᴏᴍᴍᴀɴᴅs: {len(HELP_COMMANDS)}\nᴄʀᴇᴀᴛᴇ ʙʏ : {bot.me.mention}<b></blockquote>"

    if mod_match:
        module = (mod_match.group(1)).replace(" ", "_")
        text = HELP_COMMANDS[module].__HELP__.format(next((p) for p in SH))
        button = [[InlineKeyboardButton("◁ ᴋᴇᴍʙᴀʟɪ", callback_data="help_back")]]
        await callback_query.edit_message_text(
            text=text + f"\n<blockquote><u> ᴜʙᴏᴛ ʙʏ :</u> 𝐓𝐞𝐚𝐦 𝐀𝐥𝐥 𝐁𝐨𝐭𝐬 ✘ 𝐐𝐮𝐞𝐞𝐧 𝐔𝐬𝐞𝐫𝐛𝐨𝐭</blockquote>",
            reply_markup=InlineKeyboardMarkup(button),
            disable_web_page_preview=True,
        )
    elif prev_match:
        curr_page = int(prev_match.group(1))
        await callback_query.edit_message_text(
            top_text,
            reply_markup=InlineKeyboardMarkup(paginate_modules(curr_page - 1, HELP_COMMANDS, "help")),
            disable_web_page_preview=True,
        )
    elif next_match:
        next_page = int(next_match.group(1))
        await callback_query.edit_message_text(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(paginate_modules(next_page + 1, HELP_COMMANDS, "help")),
            disable_web_page_preview=True,
        )
    elif back_match:
        await callback_query.edit_message_text(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(paginate_modules(0, HELP_COMMANDS, "help")),
            disable_web_page_preview=True,
        )
