from userbot import *


async def setprefix(client, message):
    Tm = await message.reply("ᴘʀᴏsᴇs...", quote=True)
    if len(message.command) < 2:
        return await reply_to_message(f"<blockquote><b><code>{message.text}</code> sɪᴍʙᴏʟ ᴘʀᴇғɪx<b></blockquote>")
    else:
        ub_prefix = []
        for prefix in message.command[1:]:
            if prefix.lower() == "none":
                ub_prefix.append("")
            else:
                ub_prefix.append(prefix)
        try:
            client.set_prefix(message.from_user.id, ub_prefix)
            await set_pref(message.from_user.id, ub_prefix)
            parsed_prefix = " ".join(f"<blockquote><b><code>{prefix}</code><b></blockquote>" for prefix in ub_prefix)
            return await Tm.edit(f"<blockquote><b>ᴇʜ ᴊᴇᴍʙᴜᴛ ᴘʀᴇғɪx ʟᴜ ᴜᴅᴀʜ ʙᴇʀᴜʙᴀʜ ᴋᴇ: {parsed_prefix} ✅<b></blockquote>")
        except Exception as error:
            return await message.reply(str(error))


async def change_emot(client, message):
    try:
        msg = await message.reply("ᴘʀᴏsᴇs...", quote=True)

        if not client.me.is_premium:
            return await message.reply(
                "<blockquote><b>ʟᴜ ᴋᴀʟᴏ ᴍᴀᴜ ᴘᴀᴋᴇ ᴍᴏᴅᴜʟᴇ ɪɴɪ ᴀᴋᴜɴ ʟᴜ ᴛᴜʜ ʜᴀʀᴜs ᴘʀᴇᴍɪᴜᴍ ᴅᴜʟᴜ.<b></blockquote>"
            )

        if len(message.command) < 3:
            return await message.reply("<blockquote><b>ᴍᴀsᴜᴋɪɴ ǫᴜᴇʀʏ ᴅᴀɴ ᴠᴀʟᴜᴇ ʏɢ ʙᴇɴᴇʀ.<b></blockquote>")

        query_mapping = {"ᴘᴏɴɢ": "EMOJI_PING", "ᴜʙᴏᴛ": "EMOJI_UPTIME", "ᴍᴇɴᴛɪᴏɴ": "EMOJI_MENTION"}
        command, mapping, value = message.command[:3]

        if mapping.lower() in query_mapping:
            query_var = query_mapping[mapping.lower()]
            emoji_id = None
            if message.entities:
                for entity in message.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break

            if emoji_id:
                await set_vars(client.me.id, query_var, emoji_id)
                await message.reply(
                    f"<blockquote><b>✅ <code>{query_var}</code> ʙᴇʀʜᴀsɪʟ sᴇᴛᴛɪɴɢ ᴋᴇ:</b> <emoji id={emoji_id}>{value}</emoji><b></blockquote>"
                )
            else:
                await msg.edit("<blockquote><b>ɢᴀ ᴀᴅᴀ ᴇᴍᴏᴊɪ ᴘʀᴇᴍ ɴɪʜ.<b></blockquote>")
        else:
            await msg.edit("<blockquote>ᴍᴀᴘᴘɪɴɢ ɢᴀ ᴅɪᴛᴇᴍᴜɪɴ ɴɪʜ.<b></blockquote>")

    except Exception as error:
        return await msg.edit(str(error))
