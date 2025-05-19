import os
from io import BytesIO

from userbot import bot
from userbot.config import DEVS, OWNER_ID
from userbot.core.helpers import CM, quotly

KOLOR = "#292232"


async def q_cmd(client, message):
    await process_quote_regular(client, message)


async def qf_cmd(client, message):
    await process_quote_fake(client, message)


async def process_quote_regular(client, message):
    args = message.text.split(maxsplit=3)
    rep = message.reply_to_message
    max_m = 5
    warna = KOLOR
    messages = []
    if len(args) == 1 and rep:
        messages = [rep]
    elif len(args) == 2:
        if args[1].isdigit() and rep:
            count = int(args[1])
            if count > max_m:
                return await message.reply(
                    f"<blockquote><b>Batas maksimal pesan adalah {max_m}.</b></blockquote>"
                )
            messages = [
                i
                for i in await client.get_messages(
                    chat_id=message.chat.id, message_ids=range(rep.id, rep.id + count)
                )
                if not (i.empty and i.media)
            ]
        elif CM.is_color(args[1]) and rep:
            warna = CM.get_colors(args[1])
            messages = [rep]
        else:
            msg = [message]
            msg.text = args[1]
            messages = [message]
    elif len(args) == 3:
        if args[1].isdigit() and CM.is_color(args[2]) and rep:
            count = int(args[1])
            if count > max_m:
                return await message.reply(
                    f"<blockquote><b>Batas maksimal pesan adalah {max_m}.</b></blockquote>"
                )
            warna = CM.get_colors(args[2])
            messages = [
                i
                for i in await client.get_messages(
                    message.chat.id, message_ids=range(rep.id, rep.id + count)
                )
                if not (i.empty and i.media)
            ]
        else:
            warna = CM.get_colors(args[1])
            msg = [message]
            msg.text = args[2]
            messages = [msg]

    if not messages:
        return await message.reply(
            "<blockquote><b>Tidak ada pesan valid untuk diproses.</b></blockquote>"
        )

    await process_message_to_sticker(client, message, messages, warna)


async def process_quote_fake(client, message):
    args = message.text.split(maxsplit=3)
    rep = message.reply_to_message

    if len(args) < 2:
        return await message.reply(
            """
<blockquote><b>Gunakan perintah seperti contoh berikut:

• <code>qf [username/user id] [pesan/balas pesan]</code>
Penjelasan: Untuk Memanipulasi pengguna dengan warna Default.

• <code>qf [username/user id] [warna] [pesan/balas pesan]</code>
Penjelasan: Untuk Memanipulasi pengguna dengan warna yang ditentukan.</b></blockquote>"""
        )

    dia = args[1]
    if not dia.startswith("@") and not dia.isdigit():
        return await message.reply(
            "<blockquote><b>Argumen pertama wajib berupa Username/User ID yang akan dimanipulasi.</b></blockquote>"
        )

    try:
        user = await client.get_users(dia)
        if user.id in [OWNER_ID, bot.me.id, client.me.id, *DEVS]:
            role = (
                "Pemilik"
                if user.id == OWNER_ID
                else "Diri Sendiri" if user.id == client.me.id else "Developer"
            )
            return await message.reply(
                f"<blockquote><b>Dilarang Memanipulasi {role}!</b></blockquote>"
            )
    except Exception as e:
        return await message.reply(
            f"<blockquote><b>Terjadi Kesalahan:</b>\n<code>{e}</code></blockquote>"
        )

    warna = KOLOR
    messages = []

    if rep and len(args) == 2:
        msg = await client.get_messages(message.chat.id, message_ids=rep.id)
        msg.from_user = user
        messages = [msg]
    elif len(args) == 3:
        if CM.is_color(args[2]) and rep:
            warna = CM.get_colors(args[2])
            msg = await client.get_messages(message.chat.id, message_ids=rep.id)
            msg.from_user = user
            messages = [msg]
        else:
            messages = [message]
            message.text = args[2]
    elif len(args) == 4:
        warna = CM.get_colors(args[2])
        msg = [message]
        msg.text = args[3]
        messages = [msg]

    if not messages:
        return await message.reply(
            "<blockquote><b>Tidak ada pesan valid untuk diproses.</b></blockquote>"
        )

    await process_message_to_sticker(client, message, messages, warna)


async def process_message_to_sticker(client, message, messages, warna):

    if not messages:
        return await message.reply(
            "<blockquote><b>Tidak ada pesan valid untuk diproses.</b></blockquote>"
        )

    pros = await message.reply(
        "<blockquote><b>Memproses menjadi stiker Quote...</b></blockquote>"
    )
    try:
        hasil = await quotly(messages, warna)
        bio_sticker = BytesIO(hasil)
        bio_sticker.name = "quote.webp"
        await message.reply_sticker(bio_sticker)
    except Exception as e:
        await message.reply(
            f"<blockquote><b>Error:</b>\n<code>{e}</code></blockquote>"
        )
    finally:
        await pros.delete()


async def qcolor_cmd(client, message):
    pros = await message.reply(
        "<blockquote><b>Proses mengambil daftar warna yang tersedia...</b></blockquote>"
    )
    list_colors = CM.get_list_colors("id")
    text = "<b>Daftar Warna:</b>\n\n" + "\n".join(
        f"{num}) <code>{color}</code>" for num, color in enumerate(list_colors, 1)
    )

    try:
        if len(text) > 4096:
            with open("DaftarWarna.txt", "w") as file:
                file.write(text)
            await message.reply_document("DaftarWarna.txt", caption="Daftar Warna.")
        else:
            await message.reply(f"<blockquote>{text}</blockquote>")
    except Exception as e:
        await message.reply(
            f"<blockquote><b>Terjadi Kesalahan:</b>\n<code>{e}</code></blockquote>"
        )
    finally:
        if os.path.exists("DaftarWarna.txt"):
            os.remove("DaftarWarna.txt")
        await pros.delete()
