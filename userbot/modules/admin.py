
__MODULE__ = "ᴀᴅᴍɪɴ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀᴅᴍɪɴ 』

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}kick</code> [user_id/username/reply user]
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴇɴᴅᴀɴɢ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ 

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ban</code> [user_id/username/reply user]
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙʟᴏᴋɪʀ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ 

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}mute</code> [user_id/username/reply user]
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙɪsᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ 

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}unmute</code> [user_id/username/reply user]
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟᴇᴘᴀs ᴘᴇᴍʙʟᴏᴋɪʀᴀɴ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ 

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}unban</code> [user_id/username/reply user]
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟᴇᴘᴀs ᴘᴇᴍʙɪsᴜᴀɴ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ<b></blockquote>
"""

import asyncio

from asyncio import sleep

from pyrogram import Client, filters
from importlib import import_module
from userbot.modules import loadModule
from userbot.core.helpers.misc import *
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, ChatPrivileges, Message

from userbot import *

unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)


@CB.UBOT("ban|dban")
async def member_ban(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    ky = await message.reply("Processing...")
    if not user_id:
        return await ky.reply_to_message("<blockquote><b>Tidak dapat menemukan pengguna.<b></blockquote>")
    if user_id == client.me.id:
        return await ky.reply_to_message("<blockbquote><b></blockquote>Tidak bisa banned diri sendiri.")
    if user_id == OWNER_ID:
        return await ky.reply_to_message("<blockquote><b>Tidak bisa banned Devs!<b></blockquote>")
    if user_id in (await list_admins(message)):
        return await ky.reply_to_message("<blockquote><b>Tidak bisa banned admin.<b></blockquote>")
    try:
        # await ky.delete()
        mention = (await client.get_users(user_id)).mention
    except IndexError:
        mention = (
            message.reply_to_message.sender_chat.title
            if message.reply_to_message
            else "anon"
        )
    if message.command[0][0] == "d":
        await message.reply_to_message()
    msg = f"<blockquote><b>Banned User: {mention}\nBanned By: {message.from_user.mention}\n\nᴍᴀᴅᴇ ʙʏ : {bot.me.mention}<b></blockquote>\n"
    if reason:
        msg += f"<blockquote><b>Reason {reason}<b></blockquote>"
    try:
        await message.chat.ban_member(user_id)
        await ky.edit(msg)
    except ChatAdminRequired:
        await ky.reply_to_message(f"<blockquote><u>**anda bukan admin di grup ini !**</u></blockquote>")
 



@CB.UBOT("unban")
async def member_unban(client: Client, message: Message):
    reply = message.reply_to_message
    zz = await message.reply("Processing...")
    if reply and reply.sender_chat and reply.sender_chat != message.chat.id:
        return await zz.reply_to_message(f"<blockquote><b>**Tidak bisa unban ch**<b></blockquote>")

    if len(message.command) == 2:
        user = message.text.split(None, 1)[1]
    elif len(message.command) == 1 and reply:
        user = message.reply_to_message.from_user.id
    else:
        return await zz.reply_to_message(f"<blockquote><b>Berikan username, atau reply pesannya.<b></blockquote>")
    try:
        await message.chat.unban_member(user)
        umention = (await client.get_users(user)).mention
        await zz.edit(f"<blockquote><b>Unbanned! {umention}<b></blockquote>")
    except ChatAdminRequired:
        await zz.reply_to_message(f"<blockquote><u>**anda bukan admin di group ini !**</u></blockquote>")
       
@CB.UBOT("pin|unpin")
async def pin_message(client, message):
    if not message.reply_to_message:
        return await message.edit(f"<blockquote><b>Balas ke pesan untuk pin/unpin.<b></blockquote>")
    r = message.reply_to_message
    await message.reply("Processing...")
    if message.command[0][0] == "u":
        await r.unpin()
        return await message.reply_to_message(
            f"<blockquote><b>Unpinned [this]({r.link}) message.<b></blockquote>",
            disable_web_page_preview=True,
        )
    try:
        await r.pin(disable_notification=True)
        await message.reply_to_message(
            f"<blockquote><b>Pinned [this]({r.link}) message.<b></blockquote>",
            disable_web_page_preview=True,
        )
    except ChatAdminRequired:
        await message.edit(f"<blockquote><u>**anda bukan admin di grup ini!**</u></blockquote>")
        await message.delete()

@CB.UBOT("mute|dmute")
async def mute(client, message):
    user_id, reason = await extract_user_and_reason(message)
    nay = await message.reply("Processing...")
    if not user_id:
        return await nay.reply_to_message(f"<blockquote><b>Pengguna tidak ditemukan.<b></blockquote>")
    if user_id == client.me.id:
        return await nay.reply_to_message(f"<blockquote><b>Tidak bisa mute diri sendiri.<b></blockquote>")
    if user_id == OWNER_ID:
        return await nay.reply_to_message(f"<blockquote><b>Tidak bisa mute dev!<b></blockquote>")
    if user_id in (await list_admins(message)):
        return await nay.reply_to_message(f"<blockquote><b>Tidak bisa mute admin.<b></blockquote>")
    # await nay.delete()
    mention = (await client.get_users(user_id)).mention
    msg = f"""
        f"<blockquote><b>**Muted User:** {mention}\n<b></blockquote>"
        f"<blockquote><b>**Muted By:** {message.from_user.mention if message.from_user else 'anon'}<b></blockquote>"""
    if message.command[0][0] == "d":
        await message.reply_to_message()  
    if reason:
        msg += f"<blockquote><b>**Reason:** {reason}<b></blockquote>"
    try:
        await message.chat.restrict_member(user_id, permissions=ChatPermissions())
        await nay.edit(msg)
    except ChatAdminRequired:
        await nay.reply_to_message("<blockquote><b>**anda bukan admin di group ini !**<b></blockquote>")
        
       
        
@CB.UBOT("unmute")
async def unmute(client: Client, message: Message):
    user_id = await extract_user(message)
    kl = await message.reply("Processing...")
    if not user_id:
        return await kl.reply_to_message(f"<blockquote><u>Pengguna tidak ditemukan.</u></blockquote>")
    try:
        await message.chat.restrict_member(user_id, permissions=unmute_permissions)
        # await kl.delete()
        umention = (await client.get_users(user_id)).mention
        await kl.edit(f"<blockquote><b>Unmuted! {umention}<b></blockquote>")        
        await kl.edit(msg)
    except ChatAdminRequired:
        await kl.reply_to_message(f"<blockquote><u>**anda bukan admin di group ini !**</u></blockquote>")
        
       


@CB.UBOT("kick|dkick")
async def kick_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    ny = await message.reply("Processing...")
    if not user_id:
        return await ny.reply_to_message(f"<blockquote><u>**Pengguna tidak ditemukan.**</u></blockquote>")
    if user_id == client.me.id:
        return await ny.reply_to_message(f"<blockquote><b>Tidak bisa kick diri sendiri.<b></blockquote>")
    if user_id == OWNER_ID:
        return await ny.reply_to_message(f"<blockquote><b>Tidak bisa kick dev!.<b></blockquote>")
    if user_id in (await list_admins(message)):
        return await ny.reply_to_message(f"<blockquote><b>Tidak bisa kick admin.<b></blockquote>")
    # await ny.delete()
    mention = (await client.get_users(user_id)).mention
    msg = f"""
<blockquote><b>**Kicked User:** {mention}
**Kicked By:** {message.from_user.mention if message.from_user else 'anon'}<b></blockquote>"""
    if message.command[0][0] == "d":
        await message.reply_to_message()
    if reason:
        msg += f"\n<blockquote><b>**Reason:** `{reason}`<b></blockquote>"
    try:
        await message.chat.ban_member(user_id)
        await ny.edit(msg)
        await message.chat.unban_member(user_id)
    except ChatAdminRequired:
        await ny.edit(f"<blockquote><u>**anda bukan admin di group ini !**</u></blockquote>")
        

@CB.UBOT("promote")
async def promotte(client: Client, message: Message):
    user_id = await extract_user(message)
    biji = await message.reply("Processing...")
    if not user_id:
        return await biji.reply_to_message(f"<blockquote><u>**Pengguna tidak ditemukan.**</u></blockquote>")
    (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    try:
        if message.command[0][0] == "f":
            await message.chat.promote_member(
                user_id,
                privileges=ChatPrivileges(
                    can_manage_chat=True,
                    can_delete_messages=True,
                    can_manage_video_chats=True,
                    can_restrict_members=True,
                    can_change_info=True,
                    can_invite_users=True,
                    can_pin_messages=True,
                    can_promote_members=True,
                ),
            )
            # await biji.delete()
            umention = (await client.get_users(user_id)).mention
            return await biji.reply_to_message(f"<blockquote><b>Fully Promoted! {umention}<b></blockquote>")

        await message.chat.promote_member(
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_change_info=False,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=False,
            ),
        )
        # await biji.delete()
        umention = (await client.get_users(user_id)).mention
        await biji.edit(f"Promoted! {umention}")
        await biji.edit(biji)
    except ChatAdminRequired:
        await biji.reply_to_message(f"<blockquote><u>**anda bukan admin di group ini !**</u></blockquote>")
      
 
@CB.UBOT("demote")
async def demote(client: Client, message: Message):
    user_id = await extract_user(message)
    sempak = await eor(message, "Processing...")
    if not user_id:
        return await sempak.reply_to_message(f"<blockquote><b>Pengguna tidak ditemukan<b></blockquote>")
    if user_id == client.me.id:
        return await sempak.reply_to_message(f"<blockquote><b>Tidak bisa demote diri sendiri.<b></blockquote>")
    await message.chat.promote_member(
        user_id,
        privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
        ),
    )
    umention = (await client.get_users(user_id)).mention
    await sempak.edit(f"Demoted! {umention}")
    await sempak.edit(sempak)
