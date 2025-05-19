import re
from pyrogram import filters
from userbot.config import *
from userbot import *
from userbot.core.database.filters import get_filters_count, _get_filters, get_filters_names, get_filter, save_filter, delete_filter

__MODULE__ = "ғɪʟᴛᴇʀ"
__HELP__ = """
<b>『 Bantuan Untuk Filter 』</b>

 • Perintah: <code>.addfil</code> [nama filter] [balas ke pesan]
    Penjelasan: Untuk mengatur filter grup.

 • Perintah: <code>.delfil</code> [nama filter]
    Penjelasan: Untuk menghapus filter grup.

 • Perintah: <code>.filters</code>
    Penjelasan: Untuk melihat filter grup.
"""


@CB.UBOT("addfil")
async def save_filters(client, message):
    if len(message.command) < 2 or not message.reply_to_message:
        return await eor(
            message,
            f"<b>ɢᴜɴᴀᴋᴀɴ ғᴏʀᴍᴀᴛ:</b>\n ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ ᴀᴛᴀᴜ sᴛɪᴄᴋᴇʀ <code>addfil</code> [ɴᴀᴍᴀ ғɪʟᴛᴇʀ] [ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ] ᴜɴᴛᴜᴋ sᴀᴠᴇ ғɪʟᴛᴇʀ.",
        )
    if not message.reply_to_message.text and not message.reply_to_message.sticker:
        return await eor(message, "<b>Hanya bisa save text atau sticker.</b>")
    name = message.text.split(None, 1)[1].strip()
    if not name:
        return await eor(
            message,
            f"<b>ɢᴜɴᴀᴋᴀɴ ғᴏʀᴍᴀᴛ:</b>\n ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ ᴀᴛᴀᴜ sᴛɪᴄᴋᴇʀ <code>addfil</code> [ɴᴀᴍᴀ ғɪʟᴛᴇʀ] [ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ] ᴜɴᴛᴜᴋ sᴀᴠᴇ ғɪʟᴛᴇʀ.",
        )
    chat_id = message.chat.id
    user_id = client.me.id
    if message.chat.id in BLACKLIST_CHAT:
        await eor(message, "<u>ғɪʟᴛᴇʀ ᴛɪᴅᴀᴋ ᴅɪᴘᴇʀᴋᴇɴᴀɴᴋᴀɴ ᴅɪ ɢʀᴏᴜᴘ sᴜᴘᴘᴏʀᴛ.</u>")
        return
    _type = "text" if message.reply_to_message.text else "sticker"
    _filter = {
        "type": _type,
        "data": message.reply_to_message.text.markdown
        if _type == "text"
        else message.reply_to_message.sticker.file_id,
    }
    await save_filter(user_id, chat_id, name, _filter)
    await eor(message, f"<b>ғɪʟᴛᴇʀ <code>{name}</code> ᴅɪsɪᴍᴘᴀɴ!.</b>")


@CB.UBOT("filter")
async def get_filterss(client, message):
    user_id = client.me.id
    chat_id = message.chat.id
    _filters = await get_filters_names(user_id, chat_id)
    if not _filters:
        return await eor(message, "<u>ᴛɪᴅᴀᴋ ᴀᴅᴀ ғɪʟᴛᴇʀ ᴛᴇʀsɪᴍᴘᴀɴ ᴅɪ ɢʀᴏᴜᴘ ɪɴɪ.</u>")
    _filters.sort()
    msg = f"๏ ᴅᴀғᴛᴀʀ ғɪʟᴛᴇʀ ᴛᴇʀsɪᴍᴘᴀɴ ᴅɪ <code>{message.chat.title}</code>\n"
    for _filter in _filters:
        msg += f"<b>•<b> <code>{_filter}</code>\n"
    await eor(message, msg)


@CB.UBOT("delfil")
async def del_filter(client, message):
    if len(message.command) < 2:
        return await eor(
            message, f"<b>ɢᴜɴᴀᴋᴀɴ ғᴏʀᴍᴀᴛ:</b>\n<code>delfil</code> [ɴᴀᴍᴀ ғɪʟᴛᴇʀ]"
        )
    user_id = client.me.id
    chat_id = message.chat.id
    name = message.text.split(None, 1)[1].strip()
    if not name:
        return await eor(
            message, f"<b>ɢᴜɴᴀᴋᴀɴ ғᴏʀᴍᴀᴛ:</b>\n<code>delfil</code> [ɴᴀᴍᴀ ғɪʟᴛᴇʀ]"
        )

    deleted = await delete_filter(user_id, chat_id, name)
    if deleted:
        await eor(message, f"<b>ғɪʟᴛᴇʀ <code>{name}</code> ʙᴇʀʜᴀsɪʟ ᴅɪ ʜᴀᴘᴜs.</b>")
    else:
        await eor(message, "<u>ғɪʟᴛᴇʀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.</u>")



async def filters_re(client, message):
    text = message.text.lower().strip()
    if not text:
        return
    user_id = client.me.id
    chat_id = message.chat.id
    list_of_filters = await get_filters_names(user_id, chat_id)
    for word in list_of_filters:
        pattern = r"( |^|[^\w])" + re.escape(word) + r"( |$|[^\w])"
        if re.search(pattern, text, flags=re.IGNORECASE):
            _filter = await get_filter(user_id, chat_id, word)
            data_type = _filter["type"]
            data = _filter["data"]
            if data_type == "text":
                keyb = None
                if re.findall(r"\[.+\,.+\]", data):
                    if keyboard := extract_text_and_keyb(ikb, data):
                        data, keyb = keyboard

                if message.reply_to_message:
                    await message.reply_to_message.reply_text(
                        data,
                        reply_markup=keyb,
                        disable_web_page_preview=True,
                    )

                    if text.startswith("~"):
                        await message.delete()
                    return

                return await message.reply_text(
                    data,
                    reply_markup=keyb,
                    disable_web_page_preview=True,
                )
            if message.reply_to_message:
                await message.reply_to_message.reply_sticker(data)

                if text.startswith("~"):
                    await message.delete()
                return
            return await message.reply_sticker(data)
