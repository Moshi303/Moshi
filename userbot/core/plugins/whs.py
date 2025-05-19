from asyncio import gather
from os import remove

from pyrogram.enums import ChatType

from userbot import *


async def info_cmd(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("<blockquote><b><emoji id=6010111371251815589>⏳</emoji> processing . . .<b></blockquote>")
    if not user_id:
        return await Tm.edit(
            f"<blockquote><b><emoji id =5375452661036358740>🔥</emoji> **berikan userid/username/reply untuk mendapatkan info pengguna tersebut**<b></blockquote>"
        )
    try:
        user = await client.get_users(user_id)
        username = f"@{user.username}" if user.username else "-"
        first_name = f"{user.first_name}" if user.first_name else "-"
        last_name = f"{user.last_name}" if user.last_name else "-"
        fullname = (
            f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
        )
        user_details = (await client.get_chat(user.id)).bio
        bio = f"{user_details}" if user_details else "-"
        h = f"{user.status}"
        if h.startswith("UserStatus"):
            y = h.replace("UserStatus.", "")
            status = y.capitalize()
        else:
            status = "-"
        dc_id = f"{user.dc_id}" if user.dc_id else "-"
        common = await client.get_common_chats(user.id)
        out_str = f"""
<blockquote><b>❏ ᴜsᴇʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ:\n╰• {username}

❏ <b>ᴜsᴇʀ ɪᴅ:</b> <code>{user.id}</code>
├• <b>ғɪʀsᴛ ɴᴀᴍᴇ:</b> {first_name}
├•️ <b>ʟᴀsᴛ ɴᴀᴍᴇ:</b> {last_name}
├• <b>ᴜsᴇʀɴᴀᴍᴇ:</b> {username}
├•️ <b>ᴅᴄ ɪᴅ:</b> <code>{dc_id}</code>
├• <b>ɪs ʙᴏᴛ:</b> {user.is_bot}
├• <b>ɪs sᴄᴀᴍ:</b> {user.is_scam}
├• <b>ʀᴇsᴛʀɪᴄᴛᴇᴅ:</b> {user.is_restricted}
├• <b>ᴠᴇʀɪғɪᴇᴅ:</b> {user.is_verified}
├• <b>ᴘʀᴇᴍɪᴜᴍ:</b> {user.is_premium}
╰• <b>ᴜsᴇʀ ʙɪᴏ:</b> {bio}

❏ <b>sᴀᴍᴇ ɢʀᴏᴜᴘ sᴇᴇɴ:</b> {len(common)}
├•️ <bʟᴀsᴛ sᴇᴇɴ:<b> {status}
╰• <b>ᴜsᴇʀ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ:</b> <a href=tg://user?id={user.id}>{fullname}</a><b></blockquote>
"""
        photo_id = user.photo.big_file_id if user.photo else None
        if photo_id:
            photo = await client.download_media(photo_id)
            await gather(
                Tm.delete(),
                client.send_photo(
                    message.chat.id,
                    photo,
                    caption=out_str,
                    reply_to_message_id=message.id,
                ),
            )
            remove(photo)
        else:
            await Tm.edit(out_str, disable_web_page_preview=True)
    except Exception as e:
        return await Tm.edit(f"info: {e}")


async def cinfo_cmd(client, message):
    Tm = await message.reply("</b><emoji id=6010111371251815589>⏳</emoji> processing . . .</b>")
    try:
        if len(message.text.split()) > 1:
            chat_u = message.text.split()[1]
            chat = await client.get_chat(chat_u)
        else:
            if message.chat.type == ChatType.PRIVATE:
                return await Tm.edit(
                    f"<emoji id =5929358014627713883>❌</emoji> gunakan perintah ini di dalam grup atau gunakan {PREFIX[0]}cinfo [group username atau id]"
                )
            else:
                chatid = message.chat.id
                chat = await client.get_chat(chatid)
        h = f"{chat.type}"
        if h.startswith("ChatType"):
            y = h.replace("ChatType.", "")
            type = y.capitalize()
        else:
            type = "Private"
        username = f"@{chat.username}" if chat.username else "-"
        description = f"{chat.description}" if chat.description else "-"
        dc_id = f"{chat.dc_id}" if chat.dc_id else "-"
        out_str = f"""
<b>chat information:</b>

🆔 <b>chat id:</b> <code>{chat.id}</code>
👥 <b>title:</b> {chat.title}
👥 <b>username:</b> {username}
📩 <b>type:</b> <code>{type}</code>
🏛️ <b>dc id:</b> <code>{dc_id}</code>
🗣️ <b>is scam:</b> <code>{chat.is_scam}</code>
🎭 <b>is fake:</b> <code>{chat.is_fake}</code>
✅ <b>verified:</b> <code>{chat.is_verified}</code>
🚫 <b>restricted:</b> <code>{chat.is_restricted}</code>
🔰 <b>protected:</b> <code>{chat.has_protected_content}</code>

🚻 <b>total members:</b> <code>{chat.members_count}</code>
📝 <b>description:</b> <code>{description}</code>
"""
        photo_id = chat.photo.big_file_id if chat.photo else None
        if photo_id:
            photo = await client.download_media(photo_id)
            await gather(
                Tm.delete(),
                client.send_photo(
                    message.chat.id,
                    photo,
                    caption=out_str,
                    reply_to_message_id=message.id,
                ),
            )
            remove(photo)
        else:
            await Tm.edit(out_str, disable_web_page_preview=True)
    except Exception as e:
        return await Tm.edit(f"info: `{e}`")
