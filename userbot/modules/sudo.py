__MODULE__ = "sudo"
__HELP__ = """
<blockquote><b>bantuan untuk sudo

• perintah: <code>{0}addsudo</code> [reply/username/id]
• penjelasan: tambah pengguna sudo.

• perintah: <code>{0}delsudo</code> [reply/username/id]
• penjelasan: hapus pengguna sudo.

• perintah: <code>{0}sudolist</code>
• penjelasan: cek pengguna sudo.<b></blockquote>
"""


import asyncio

from pyrogram.enums import *
from pyrogram.errors import FloodWait
from pyrogram.types import *

from userbot import *

@CB.UBOT("addsudo")
async def _(client, message):
    msg = await message.reply(f"<blockquote><b>Processing...<b></blockquote>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(f"<blockquote><b>**Silakan balas pesan pengguna/username/user id**<b></blockquote>")

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_users = await ambil_list_vars(client.me.id, "SUDO_USER", "ID_NYA")

    if user.id in sudo_users:
        return await msg.edit(
            f"<blockquote><b>[{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) **Sudah menjadi pengguna sudo.**<b></blockquote>"
        )

    try:
        await add_vars(client.me.id, "SUDO_USER", user.id, "ID_NYA")
        return await msg.edit(
            f"<blockquote><b>[{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) **Ditambahkan ke pengguna sudo.**<b></blockquote>"
        )
    except Exception as error:
        return await msg.edit(error)


@CB.UBOT("delsudo")
async def _(client, message):
    msg = await message.reply(f"<blockquote><b>Processing...<b></blockquote>")
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply(
            f"<blockquote><b>**Silakan balas pesan penggjna/username/user id.**<b></blockquote>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_users = await ambil_list_vars(client.me.id, "SUDO_USER", "ID_NYA")

    if user.id not in sudo_users:
        return await msg.edit(
            f"<blockquote><b>{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) **Bukan bagian pengguna sudo.**<b></blockquote>"
        )

    try:
        await rem_vars(client.me.id, "SUDO_USER", user.id, "ID_NYA")
        return await msg.edit(
            f"<blockquote><b>[{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) **Dihapus dari pengguna sudo.**<b></blockquote>"
        )
    except Exception as error:
        return await msg.edit(error)


@CB.UBOT("sudolist")
async def _(client, message):
    msg = await message.reply(f"<blockquote><b>Processing...<b></blockquote>")
    sudo_users = await ambil_list_vars(client.me.id, "SUDO_USER", "ID_NYA")

    if not sudo_users:
        return await msg.edit(f"<blockquote>**Tidak ada pengguna sudo ditemukan.**<b></blockquote>")

    sudo_list = []
    for user_id in sudo_users:
        try:
            user = await client.get_users(int(user_id))
            sudo_list.append(
                f"<blockquote><b> • [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | <code>{user.id}</code><b></blockquote>"
            )
        except:
            continue

    if sudo_list:
        response = (
            f"<blockquote><b>Daftar Pengguna:<b></blockquote>\n"
            + "\n".join(sudo_list)
            + f"<blockquote><b>\n • </b> <code>{len(sudo_list)}</code><b></blockquote>"
        )
        return await msg.edit(response)
    else:
        return await msg.edit("<b>Eror</b>")
