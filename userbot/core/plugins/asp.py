import random

from pyrogram.enums import MessagesFilter
from userbot.core.function.emoji import emoji
from userbot import *


async def video_asupan(client, message):
    y = await message.reply_text(f"ᴘʀᴏᴄᴇssɪɴɢ...")
    try:
        await client.join_chat("@AsupannyaRyn")
    except:
        pass
    try:
        asupannya = []
        async for asupan in client.search_messages(
            "@AsupannyaRyn", filter=MessagesFilter.VIDEO
        ):
            asupannya.append(asupan)
        video = random.choice(asupannya)
        await video.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(f"<b>ᴅᴜʜ ᴏʀᴀ ᴀᴅᴀ ʟᴀɢɪ ᴅᴀʜ ᴀsᴜᴘᴀɴɴʏᴀ ɴᴀɴᴛɪ ʟᴀɢɪ ʙᴀᴇ ʟᴜ ɴʏᴀʀɪ ᴀsᴜᴘᴀɴɴʏᴀ.</b>")


async def photo_cewek(client, message):
    y = await message.reply_text(f"ᴘʀᴏᴄᴇssɪɴɢ...")
    try:
        await client.join_chat("@AyangnyaRyn")
    except:
        pass
    try:
        ayangnya = []
        async for ayang in client.search_messages(
            "@ayangnyaryn", filter=MessagesFilter.PHOTO
        ):
            ayangnya.append(ayang)
        photo = random.choice(ayangnya)
        await photo.copy(
            message.chat.id,
            caption=f"<b>ɴɪʜ ᴄᴇᴡᴇ ʟᴜ <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a></b>",
            reply_to_message_id=message.id,
        )
        await y.delete()
    except Exception as error:
        await y.edit(f"<b>ᴄᴇᴡᴇ ʟᴜ ᴏʀᴀ ᴀᴅᴀ ɴɪʜ ɴᴀɴᴛɪ ʟᴀɢɪ ʙᴀᴇ ɢᴜᴀ ᴄᴀʀɪɪɴ ʏɢ ʙᴀʀᴜ.</b>")


async def photo_cowok(client, message):
    y = await message.reply_text(f"ᴘʀᴏᴄᴇssɪɴɢ...")
    try:
        await client.join_chat("@Ayang2Ryn")
    except:
        pass
    try:
        ayang2nya = []
        async for ayang2 in client.search_messages(
            "@Ayang2Ryn", filter=MessagesFilter.PHOTO
        ):
            ayang2nya.append(ayang2)
        photo = random.choice(ayang2nya)
        await photo.copy(
            message.chat.id,
            caption=f"<b>ɴɪʜ ᴄᴏᴡᴏ ʟᴜ <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a></b>",
            reply_to_message_id=message.id,
        )
        await y.delete()
    except Exception as error:
        await y.edit("<b>ᴄᴏᴡᴏ ʟᴜ ᴏʀᴀ ᴀᴅᴀ ɴɪʜ ɴᴀɴᴛɪ ʟᴀɢɪ ʙᴀᴇ ɢᴜᴀ ᴄᴀʀɪɪɴ ʏɢ ʙᴀʀᴜ.</b>")


async def photo_anime(client, message):
    y = await message.reply_text(f"ᴘʀᴏᴄᴇssɪɴɢ...")
    anime_channel = random.choice(["@animehikarixa", "@anime_WallpapersHD"])
    try:
        animenya = []
        async for anime in client.search_messages(
            anime_channel, filter=MessagesFilter.PHOTO
        ):
            animenya.append(anime)
        photo = random.choice(animenya)
        await photo.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)

async def video_bokep(client, message):
    y = await message.reply_text(f"ᴘʀᴏᴄᴇssɪɴɢ...")
    try:
        await client.join_chat("https://t.me/+x9K2CHUf5m8wMDk8")
    except:
        pass
    try:
        bokepnya = []
        async for bokep in client.search_messages(
            -1002475671392, filter=MessagesFilter.VIDEO
        ):
            bokepnya.append(bokep)
        video = random.choice(bokepnya)
        await video.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(f"<u>ᴛᴏʙᴀᴛ ᴛᴏʟᴏʟ ᴊᴀɴɢᴀɴ ɴᴏɴᴛᴏɴ ʙᴏᴋᴇᴘ ᴍᴜʟᴜ ɪᴅɪᴏᴛ !.</u>")
    if client.me.id == OWNER_ID:
        return
    await client.leave_chat(-1002475671392)
