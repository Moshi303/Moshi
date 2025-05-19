from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from userbot.config import LOGS_MAKER_UBOT, OWNER_ID
from userbot import bot, ubot
from userbot.core.database import get_expired_date

class MSG:
    def DEAK(X):
        return f"""
<b>❏ pemberitahuan</b>
<b>├ akun:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ id:</b> <code>{X.me.id}</code>
<b>╰ telah berhasil di hapus dari telegram</b>
"""
            
    def EXPIRED_MSG_BOT(X):
        return f"""
<b>❏ pemberitahuan</b>
<b>├ akun:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ id:</b> <code>{X.me.id}</code>
<b>╰ masa aktif telah habis</b>
"""

    
    def START(message):
        return f"""
<blockquote>👻 <u>sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ</u> <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>

🤖 <u>sᴀʏᴀ ᴀᴅᴀʟᴀʜ</u> {bot.me.mention} <u>sᴀʏᴀ ᴍᴇɴʏᴇᴅɪᴀᴋᴀɴ ʙᴀɴʏᴀᴋ ᴍᴏᴅᴜʟᴇ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴀɴᴅᴀ ʟᴇʙɪʜ ɢᴀᴍᴘᴀɴɢ ᴍᴇɴᴊᴀʟᴀɴᴋᴀɴ ᴀᴋᴛɪғɪᴛᴀs ᴅɪ ᴛᴇʟᴇɢʀᴀᴍ.</u>

▢ <u>ᴊɪᴋᴀ ᴀᴅᴀ ʏɢ ɪɴɢɪɴ ᴅɪ ᴛᴀɴʏᴀᴋᴀɴ ʙɪsᴀ ʟᴀɴɢsᴜɴɢ ᴘᴄ ᴋᴇ</u> @QueenAmi01</blockquote>
"""

    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
<blockquote><u>Sɪʟᴀᴋᴀɴ Lᴀᴋᴜᴋᴀɴ Pᴇᴍʙᴀʏᴀʀᴀɴ Tᴇʀʟᴇʙɪʜ Dᴀʜᴜʟᴜ.</u>

<u>Hᴀʀɢᴀ Pᴇʀʙᴜʟᴀɴ:</u> <i>{harga}.000</i>

💳 <u>Mᴇᴛᴏᴅᴇ Pᴇᴍʙᴀʏᴀʀᴀɴ:</u>
 ├──• <u><i>DANA</u></i>
 ├─• <u><i>085353476724</u></i> <u><i>A/N Sun***</u></i>


🔖 <u>Tᴏᴛᴀʟ Hᴀʀɢᴀ:</u> <i>Rp {total}.000</i>
🗓️ <u>Tᴏᴛᴀʟ Bᴜʟᴀɴ:</u> <i>{bulan}</i>

✅ <u>Kʟɪᴋ Tᴏᴍʙᴏʟ Dɪ Bᴀᴡᴀʜ Iɴɪ Uɴᴛᴜᴋ Mᴇɴɢɪʀɪᴍᴋᴀɴ Bᴜᴋᴛɪ Pᴇᴍʙᴀʏᴀʀᴀɴ.</u></blockquote>
"""

    async def USERBOT(count):
        expired_date = await get_expired_date(ubot._ubot[int(count)].me.id)
        return f"""
<blockquote><b>❏ userbot ke</b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b> ├ akun:</b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
<b> ├ id:</b> <code>{ubot._ubot[int(count)].me.id}</code>
<b> ╰ expired</b> <code>{expired_date.strftime('%d-%m-%Y')}<b></blockquote>
"""

    def POLICY():
        return """
<blockquote><u>Sᴀʏᴀ sᴀɴɢᴀᴛ ᴍᴇɴʏᴀʀᴀɴᴋᴀɴ ᴊɪᴋᴀ ɪɴɢɪɴ ᴍᴇᴍᴀsᴀɴɢ ᴜsᴇʀʙᴏᴛ ᴘᴀᴅᴀ ID 𝟼, 𝟽 ɴᴏᴍᴏʀ Iɴᴅᴏɴᴇsɪᴀ, ᴜsᴀʜᴀᴋᴀɴ Aᴋᴜɴ ᴛᴇʀsᴇʙᴜᴛ ᴛᴇʟᴀʜ ᴀᴋᴛɪғ ᴀᴛᴀᴜ ʟᴏɢɪɴ sᴇʟᴀᴍᴀ 𝟷 ʙᴜʟᴀɴ.</u>

<u>Dᴜᴋᴜɴɢᴀɴ:</u>

<u>Uɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ʙᴀɴᴛᴜᴀɴ ᴀᴛᴀᴜ ᴅᴜᴋᴜɴɢᴀɴ,</u> 
<u>ᴀɴᴅᴀ ᴅᴀᴘᴀᴛ ᴍᴇɴɢʜᴜʙᴜɴɢɪ ᴀᴅᴍɪɴ ᴅɪ ʙᴀᴡᴀʜ ɪɴɪ ᴀᴛᴀᴜ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ</u> @QueenAmi01 <u>ᴅɪ Tᴇʟᴇɢʀᴀᴍ.</u> 
<u>Hᴀʀᴀᴘ ᴅɪɪɴɢᴀᴛ, ᴊᴀɴɢᴀɴ ᴍᴇɴɢʜᴜʙᴜɴɢɪ Dᴜᴋᴜɴɢᴀɴ Tᴇʟᴇɢʀᴀᴍ ᴀᴛᴀᴜ </u>
<u>Dᴜᴋᴜɴɢᴀɴ Bᴏᴛ ᴜɴᴛᴜᴋ ᴍᴀsᴀʟᴀʜ ᴛᴇʀᴋᴀɪᴛ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ʏᴀɴɢ ᴅɪʟᴀᴋᴜᴋᴀɴ ᴅɪ ʙᴏᴛ ɪɴɪ.</u>

<u>Sɪʟᴀʜᴋᴀɴ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ Sᴇᴛᴜᴊᴜ ᴊɪᴋᴀ sᴇᴛᴜᴊᴜ, ᴀᴛᴀᴜ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ Tɪᴅᴀᴋ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋʜɪʀɪ ɪɴɪ.</u></blockquote>
"""


async def sending_user(user_id):
    try:
        if bot and bot.me and bot.me.username:
            await bot.send_message(
                user_id,
                "<blockquote><b>💬 silahkan buat ulang userbot anda<b></blockquote>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "buat userbot",
                                callback_data="bahan",
                            )
                        ],
                    ]
                ),
                disable_web_page_preview=True,
            )
            await bot.send_message(
                LOGS_MAKER_UBOT,
                f"""
<blockquote><b>➡️ yang merasa memiliki id: {user_id}

✅ silahkan buat ulang userbot nya di: @{bot.me.username}<b></blockquote>
        """,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "📁 cek masa aktif 📁",
                                callback_data=f"cek_masa_aktif {user_id}",
                            )
                        ],
                    ]
                ),
                disable_web_page_preview=True,
            )
        else:
            print("<blockquote><b>Bot belum diinisialisasi dengan benar atau atribut 'me' tidak tersedia.<b></blockquote>")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
        # Lakukan penanganan kesalahan sesuai kebutuhan anda
