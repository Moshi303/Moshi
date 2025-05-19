import asyncio

from pyrogram import filters
from pyrogram.types import Message

from userbot import *
from userbot.core.helpers.basic import ReplyCheck, extract_user, ReplyCheck

@CB.UBOT("p")
async def ngep(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await message.reply(
             "<blockquote><b>**Perintah ini Dilarang digunakan Kepada Developer Saya**<b></blockquote>"
        )
    xx = await message.reply("<blockquote><b>**NI GW KASIH TAU YA...**<b></blockquote>")
    await asyncio.sleep(1.5)
    await xx.edit("<blockquote><b>**LU PA PE PA PE AJA GOBLOK**<b></blockquote>")
    await asyncio.sleep(1.5)
    await xx.edit("<blockquote><b>**MINIMAL SALAM YA ANJING**<b></blockquote>")
    await asyncio.sleep(1.5)
    await xx.edit("<blockquote><b>**PUNYA OTAK DI PAKE**<b></blockquote>")
    await asyncio.sleep(1.5)
    await xx.edit("<blockquote><b>**LU PA PE PA PE GUA HANTAM PAKE P MAU LU?**<b></blockquote>")

@CB.UBOT("ah")
async def ngeah(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await message.reply(
            "<blockquote><b>**Perintah ini dilarang digunakan kepada Developer Saya**<b></blockquote>"
        )
    xx = await message.reply("<blockquote><b>**EH GOBLOK NIH DENGERIN YA...**<b></blockquote>")
    await asyncio.sleep(2)
    await xx.edit("<blockquote><b>**LU NGEDESAH KYAK BEGITU GA KEREN GOBLOK LU**<b></blockquote>")
    await asyncio.sleep(2)
    await xx.edit("<blockquote><b>**KALO MAU NGEDESAH BEGITU MENDING LU OPEN PICIES AJA GOBLOK**<b></blockquote>")
    await asyncio.sleep(2)
    await xx.edit("<blockquote><b>**BIKIN MALU ORANG TUA AJA LU MAH JADI ANAK BEGO**<b></blockquote>")
    await asyncio.sleep(2)
    await xx.edit("<blockquote><b>**OH IYA LUPA KAN LU GA PUNYA ORANG TUA MAKANNYA KELAKUANNYA BEGITU**<b></blockquote>")

@CB.UBOT("cntk")
async def ngecntk(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await message.reply(
            "<blockquote><b>**Perintah ini dilarang digunakan kepada Developer Saya**<b></blockquote>"
        )
    xx = await message.reply("<blockquote><b>**EH MONYET RAGUNAN BOGOR**<b></blockquote>")
    await asyncio.sleep(2)
    await xx.edit("<blockquote><b>**GAUSAH SOK KECANTIKAN DEH LU NYETT**<b></blockquote>")
    await asyncio.sleep(2)
    await xx.edit("<blockquote><b>**MUKA LU TUH KYA BERUK BEGITU GAUSAH SOK CANTIK MONYETT**<b></blockquote>")
    await asyncio.sleep(2)
    await xx.edit("<blockquote><b>**ULULULU MAAP KAK KETAMPAR FAKTA YA WLEOWLEO** 😝😝<b></blockquote>")

@CB.UBOT("frm")
async def ngefrm(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await message.reply(
            "<blockquote><b>**Perintah ini dilarang digunakan kepada Developer Saya**<b></blockquote>"
        )
    xx = await message.reply("<blockquote><b>**EH BUAT LU SEMUA NIH YA**<b></blockquote>")
    await asyncio.sleep(2)
    await xx.edit("<blockquote><b>**DARI PADA LU NIMBRUNG DISINI GA KENAL SIAPA-SIAPA**<b></blockquote>")
    await asyncio.sleep(2)
    await xx.edit("<blockquote><b>**MENDING LU JOIN KE GROUP GUA SINI GOBLOK**<b></blockquote>")
    await asyncio.sleep(2)
    await xx.edit("<blockquote><b>**UDAH PASTI BAKALAN BANYAK YG ASIK LEBIH ASIK DI GC BUSUK INI WKWKW**<b></blockquote>")
    await asyncio.sleep(2)
    await xx.edit("<blockquote><b>**NIH GC KEREN NYA NGENTOT !.\n❏ LU PENCET AJA TUH.\n╰• @AreaMutualanGrups**<b></blockquote>")

@CB.UBOT("pantun")
async def ngepantun(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await message.reply(
            "<blockquote><b>**Perintah ini dilarang digunakan kepada Developer Saya**<b></blockquote>"
        )
    xx = await message.reply("**EH JAMET GUA PUNYA PANTUN NI BUAT LU**")
    await asyncio.sleep(1)
    await xx.edit("**ORANG BUDHA IBADAH DI KUIL**")
    await asyncio.sleep(0.5)
    await xx.edit("**HABIS IBADAH NYANTI DI PANTAI**")
    await asyncio.sleep(0.5)
    await xx.edit("**KALO NYALI MASIH SECUIL**")
    await asyncio.sleep(0.5)
    await xx.edit("**SAMBIL MEREM PUN GUA BANTAI** 🥵😎")
    

__MODULE__ = "ᴛᴏxɪᴄ𝟹"
__HELP__ = f"""
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴛᴏxɪᴄ 𝟹 』
➢ ᴘᴇʀɪɴᴛᴀʜ: </b> <code>{0}p</code></code>
➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴄᴏʙᴀɪɴ sᴇɴᴅɪʀɪ ɴʏᴇᴛ ɢᴀᴜsᴀʜ ʙᴀɴʏᴀᴋ ᴛᴀɴʏᴀ.
➢ ᴘᴇʀɪɴᴛᴀʜ: </b> <code>{0}ah</code></code>
➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴄᴏʙᴀɪɴ sᴇɴᴅɪʀɪ ɴʏᴇᴛ ɢᴀᴜsᴀʜ ʙᴀɴʏᴀᴋ ᴛᴀɴʏᴀ.
➢ ᴘᴇʀɪɴᴛᴀʜ: </b> <code>{0}cntk</code></code>
➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴄᴏʙᴀɪɴ sᴇɴᴅɪʀɪ ɴʏᴇᴛ ɢᴀᴜsᴀʜ ʙᴀɴʏᴀᴋ ᴛᴀɴʏᴀ.
➢ ᴘᴇʀɪɴᴛᴀʜ: </b> <code>{0}pantun</code></code>
➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴄᴏʙᴀɪɴ sᴇɴᴅɪʀɪ ɴʏᴇᴛ ɢᴀᴜsᴀʜ ʙᴀɴʏᴀᴋ ᴛᴀɴʏᴀ.<b></blockquote>
"""
