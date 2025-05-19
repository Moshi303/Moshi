from pyrogram import *
from pyrogram.types import *
from userbot.core.function.emoji import emoji
from userbot import *

PM_GUARD_WARNS_DB = {}
PM_GUARD_MSGS_DB = {}

FLOOD = {}
FLOOD2 = {}

DEFAULT_TEXT = f"<blockquote><b>Pᴇʀᴋᴇɴᴀʟᴋᴀɴ sᴀʏᴀ ᴀᴅᴀʟᴀʜ ᴘᴍ-sᴇᴄᴜʀɪᴛʏ ᴅɪsɪɴɪ, Sɪʟᴀʜᴋᴀɴ ᴛᴜɴɢɢᴜ ᴍᴀᴊɪᴋᴀɴ sᴀʏᴀ ᴍᴇᴍʙᴀʟᴀs ᴘᴇsᴀɴ ᴋᴀᴍᴜ, Jᴀɴɢᴀɴ sᴘᴀᴍ ᴀᴛᴀᴜ ᴋᴀᴍᴜ ᴀᴋᴀɴ ᴅɪ ʙʟᴏᴋɪʀ sᴇᴄᴀʀᴀ ᴏᴛᴏᴍᴀᴛɪs.\n\n⚠️ ᴘᴇʀɪɴɢᴀᴛᴀɴ<b></blockquote>"

PM_WARN = """
<blockquote><b>🙋🏻‍♂ Hᴀʟᴏ, Aᴅᴀ ʏɢ ʙɪsᴀ sᴀʏᴀ ʙᴀɴᴛᴜ?

<b>I'ᴍ {}</b>

{} {} ʜᴀᴛɪ - ʜᴀᴛɪ !!<b></blockquote>
"""

LIMIT = 5


async def permitpm(client, message):
    user_id = client.me.id
    babi = await message.reply(f"<blockquote><b>**Processing...**<b></blockquote>")
    bacot = get_arg(message)
    if not bacot:
        return await babi.edit(f"<blockquote><b>**Gunakan Format : {PREFIX[0]}pmpermit on or off**<b></blockquote>" + emoji("gagal"))
    is_already = await get_vars(user_id, "ENABLE_PM_GUARD")
    if bacot.lower() == "on":
        if is_already:
            return await babi.edit(f"<blockquote><b>ᴘᴍᴘᴇʀᴍɪᴛ ᴜᴅᴀʜ ᴀᴋᴛɪғ.<b></blockquote>")
        await set_vars(user_id, "ENABLE_PM_GUARD", True)
        await babi.edit(emoji("done") + "<blockquote><b>**ᴘᴍᴘᴇʀᴍɪᴛ ᴜᴅᴀʜ ᴀᴋᴛɪғ.**<b></blockquote>")
    elif bacot.lower() == "off":
        if not is_already:
            return await babi.edit(f"<blockquote><b>**ᴘᴍᴘᴇʀᴍɪᴛ ᴜᴅᴀʜ ᴍᴀᴛɪ.**<b></blockquote>" + emoji("gagal"))
        await set_vars(user_id, "ENABLE_PM_GUARD", False)
        await babi.edit(f"<blockquote><b>**ᴘᴍᴘᴇʀᴍɪᴛ ᴜᴅᴀʜ ᴍᴀᴛɪ.**<b></blockquote>" + emoji("gagal"))
    else:
        await babi.edit(f"<blockquote><b>**Gunakan Format : {PREFIX[0]}pmpermit on or off**<b></blockquote>" + emoji("gagal"))


async def approve(client, message):
    babi = await message.reply(f"<blockquote><b>**Processing...**<b></blockquote>")
    chat_type = message.chat.type
    client.me.id
    if chat_type == "me":
        return await babi.edit(f"<blockquote><b>**apakah anda sudah gila ?**<b></blockquote>" + emoji("bintang"))
    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        if not message.reply_to_message:
            return await babi.edit(f"<blockquote><b>Balas ke pesan pengguna, untuk disetujui.**<b></blockquote>" + emoji("gagal"))
        user_id = message.reply_to_message.from_user.id
    elif chat_type == enums.ChatType.PRIVATE:
        user_id = message.chat.id
    else:
        return
    already_apprvd = await check_user_approved(user_id)
    if already_apprvd:
        return await babi.edit(f"<blockquote><b>**Pengguna ini sudah disetujui.**<b></blockquote>" + emoji("done"))
    if user_id in PM_GUARD_WARNS_DB:
        PM_GUARD_WARNS_DB.pop(user_id)
        try:
            await client.delete_messages(
                chat_id=user_id, message_ids=PM_GUARD_MSGS_DB[user_id]
            )
        except BaseException:
            pass
    await add_approved_user(user_id)
    await babi.edit(f"<blockquote><b>**Baiklah, pengguna ini disetujui untuk mengirim pesan.**<b></blockquote>" + emoji("done"))


async def disapprove(client, message):
    babi = await message.reply(f"<blockquote><b>**Processing...**<b></blockquote>")
    client.me.id
    chat_type = message.chat.type
    if chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        if not message.reply_to_message.from_user:
            return await babi.edit(f"<blockquote><b>**Balas ke pesan pengguna, untuk ditolak.**<b></blockquote>")
        user_id = message.reply_to_message.from_user.id
    elif chat_type == enums.ChatType.PRIVATE:
        user_id = message.chat.id
    else:
        return
    already_apprvd = await check_user_approved(user_id)
    if not already_apprvd:
        return await babi.edit(
            f"<blockquote><b>**Pengguna ini memang belum disetujui untuk mengirim pesan.**<b></blockquote>"
        )
    await rm_approved_user(user_id)
    await babi.edit(f"<blockquote><b>**Baiklah, pengguna ini ditolak untuk mengirim pesan.**<b></blockquote>" + emoji("gagal"))


async def set_msg(client, message):
    babi = await message.reply(f"<blockquote><b>**Processing...**<b></blockquote>")
    user_id = client.me.id
    r_msg = message.reply_to_message
    args_txt = get_arg(message)
    if r_msg:
        if r_msg.text:
            pm_txt = r_msg.text
        else:
            return await babi.edit(
                f"<blockquote><b>**Silakan balas ke pesan untuk dijadikan teks PMPermit !**<b></blockquote>" + emoji("gagal")
            )
    elif args_txt:
        pm_txt = args_txt
    else:
        return await babi.edit(
            f"<blockquote><b>**Silakan balas ke pesan atau berikan pesan untuk dijadikan teks PMPermit !.**\n`Contoh :` {0}setmsg Halo saya anuan<b></blockquote>"
        )
    await set_vars(user_id, "CUSTOM_PM_TEXT", pm_txt)
    await babi.edit(f"<blockquote><b>**Pesan PMPemit berhasil diatur menjadi :** `{pm_txt}`.`<b></blockquote>")


async def set_limit(client, message):
    babi = await message.reply(f"<blockquote><b>**Processing...**<b></blockquote>")
    user_id = client.me.id
    args_txt = get_arg(message)
    if args_txt:
        if args_txt.isnumeric():
            pm_warns = int(args_txt)
        else:
            return await babi.edit(f"<blockquote><b>**Kasih Angka Limitnya Ngentot !.**<b></blockquote>")
    else:
        return await babi.edit(
            f"<blockquote><b>**Silakan berikan pesan untuk dijadikan angka limit !**\n`Contoh :` {0}setlimit 5`<b></blockquote>"
        )
    await set_vars(user_id, "CUSTOM_PM_WARNS_LIMIT", pm_warns)
    await babi.edit(f"<blockquote><b>**Pesan Limit berhasil diatur menjadi :** `{args_txt}`.`<b></blockquote>")


async def handle_pmpermit(client, message):
    user_id = client.me.id
    siapa = message.from_user.id
    biji = message.from_user.mention
    chat_id = message.chat.id
    in_user = message.from_user
    fsdj = await check_user_approved(chat_id)
    is_pm_guard_enabled = await get_vars(user_id, "ENABLE_PM_GUARD")
    if not is_pm_guard_enabled:
        return

    if fsdj:
        return

    if in_user.is_fake or in_user.is_scam:
        await message.reply(f"<blockquote><b>**Sepertinya anda mencurigakan...**<b></blockquote>")
        return await client.block_user(in_user.id)
    if in_user.is_support or in_user.is_verified or in_user.is_self:
        return
    if siapa in DEVS:
        try:
            await add_approved_user(chat_id)
            await client.send_message(
                chat_id,
                f"<blockquote><b>Menerima Pesan Dari {biji} !!\nTerdeteksi Founder Dari {bot.me.first_name}.<b></blockquote>" + emoji("done"),
                parse_mode=enums.ParseMode.HTML,
            )
        except BaseException:
            pass
        return
    if siapa in await get_seles():
        try:
            await add_approved_user(chat_id)
            await client.send_message(
                chat_id,
                f"<blockquote><b>Menerima Pesan Dari {biji} !!\nTerdeteksi admin Dari {bot.me.first_name}.<b></blockquote>" + emoji("done"),
                parse_mode=enums.ParseMode.HTML,
            )
        except BaseException:
            pass
        return

    master = await client.get_me()
    getc_pm_txt = await get_vars(user_id, "CUSTOM_PM_TEXT")
    getc_pm_warns = await get_vars(user_id, "CUSTOM_PM_WARNS_LIMIT")
    custom_pm_txt = getc_pm_txt if getc_pm_txt else DEFAULT_TEXT
    custom_pm_warns = getc_pm_warns if getc_pm_warns else LIMIT
    if in_user.id in PM_GUARD_WARNS_DB:
        try:
            if message.chat.id in PM_GUARD_MSGS_DB:
                await client.delete_messages(
                    chat_id=message.chat.id,
                    message_ids=PM_GUARD_MSGS_DB[message.chat.id],
                )
        except BaseException:
            pass
        PM_GUARD_WARNS_DB[in_user.id] += 1
        if PM_GUARD_WARNS_DB[in_user.id] >= custom_pm_warns:
            await message.reply(
                f"<blockquote><b>**Saya sudah memberi tahu {custom_pm_warns} peringatan\nTunggu tuan saya menyetujui pesan anda, atau anda akan diblokir !**<b></blockquote>" + emoji("gagal")
            )
            return await client.block_user(in_user.id)
        else:
            rplied_msg = await message.reply(
                PM_WARN.format(
                    master.first_name,
                    custom_pm_txt.format(bot.me.first_name),
                    PM_GUARD_WARNS_DB[in_user.id],
                    custom_pm_warns,
                )
            )
    else:
        PM_GUARD_WARNS_DB[in_user.id] = 1
        rplied_msg = await message.reply(
            PM_WARN.format(
                master.first_name,
                custom_pm_txt.format(bot.me.first_name),
                PM_GUARD_WARNS_DB[in_user.id],
                custom_pm_warns,
            )
        )
    PM_GUARD_MSGS_DB[message.chat.id] = rplied_msg.id
