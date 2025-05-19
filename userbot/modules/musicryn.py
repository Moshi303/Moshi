import os
import re
import asyncio
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from userbot import *
from pytgcalls.exceptions import NotInCallError
from pyrogram.types import Message
from pytgcalls import filters as fl
from pytgcalls import PyTgCalls
from pytgcalls.types import ChatUpdate
from pytgcalls.types import GroupCallParticipant
from pytgcalls.types import MediaStream
from pytgcalls.types import AudioQuality
from pytgcalls.types import MediaStream
from pytgcalls.types import VideoQuality
from pytgcalls.types import Update
from youtubesearchpython import VideosSearch
from yt_dlp import YoutubeDL
from functools import partial


__MODULE__ = "ᴍᴜsɪᴄ"
__HELP__ = """<blockquote><b>
cmd : <code>{0}play</code>
    untuk memutar music

cmd : <code>{0}end</code>
    untuk menghentikan music

cmd : <code>{0}skip</code>
    untuk mengskip music

cmd : <code>{0}pause</code>
    untuk menjeda music

cmd : <code>{0}resume</code>
    untuk menjeda music</b></blockquote>
"""

mycookies = "ryn_cookies.txt"

def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1)
        for r in search.result()["result"]:
            ytid = r['id']
            if len(r['title']) > 34:
                songname = r['title'][:35] + "..."
            else:
                songname = r['title']
            url = f"https://www.youtube.com/watch?v={ytid}"
        return [songname, url]
    except Exception as e:
        print(e)
        return 0


async def run_sync(func, *args, **kwargs):
    loop = asyncio.get_event_loop()
    p_func = partial(func, *args, **kwargs)
    return await loop.run_in_executor(None, p_func)


async def YoutubeDownload(url, as_video=False):
    if as_video:
        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "format": "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "nocheckcertificate": True,
            "geo_bypass": True,
            "cookiefile": mycookies,
        }
    else:
        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "format": "bestaudio[ext=m4a]",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "nocheckcertificate": True,
            "geo_bypass": True,
            "cookiefile": mycookies,
        }
    data_ytp = "<blockquote><b>🗯 ɪɴꜰᴏʀᴍᴀsɪ {}</b>\n\n<b>💠 ɴᴀᴍᴀ:</ʙ> {}<b>\n<b>⏲ ᴅᴜʀᴀsɪ:</b> {}\n<b>🎑 ᴅɪʟɪʜᴀᴛ:</b> {}\n<b>🌍 ᴄʜᴀɴɴᴇʟ:</b> {}\n<b>🔗 ᴛᴀᴜᴛᴀɴ:</b> <a href={}>ʏᴏᴜᴛᴜʙᴇ</a>\n\n<b> ᴘʟᴀʏ ʙʏ : {}<b></blockquote>"
    ydl = YoutubeDL(ydl_opts)
    ytdl_data = await run_sync(ydl.extract_info, url, download=True)
    file_name = ydl.prepare_filename(ytdl_data)
    videoid = ytdl_data["id"]
    title = ytdl_data["title"]
    url = f"https://youtu.be/{videoid}"
    duration = ytdl_data["duration"]
    channel = ytdl_data["uploader"]
    views = f"{ytdl_data['view_count']:,}".replace(",", ".")
    thumb = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg"
    return file_name, title, url, duration, views, channel, thumb, data_ytp


@CB.UBOT("play")
async def play(client, m: Message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    replied = m.reply_to_message
    chat_id = m.chat.id
    if replied:
        if replied.audio or replied.voice:
            huehue = await replied.reply(f"{brhsl}<b>ᴘʀᴏᴄᴄᴇsɪɴɢ...</b>")
            dl = await replied.download()
            link = replied.link
            if replied.audio:
                if replied.audio.title:
                    songname = replied.audio.title[:35] + "..."
                else:
                    if replied.audio.file_name:
                        songname = replied.audio.file_name[:35] + "..."
                    else:
                        songname = "Audio"
            elif replied.voice:
                songname = "Voice Note"
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await huehue.edit(f"{brhsl} ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ᴀɴᴛʀɪᴀɴ #{pos}")
            else:
                try:
                    await client.call_py.play(
                        chat_id,
                        MediaStream(
                        dl,
                        AudioQuality.STUDIO,
                        ),
                    )
                    add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                    await huehue.edit(f"<blockquote><b>**<emoji id=5895705279416241926>▶</emoji> ᴍᴇᴍᴜʟᴀɪ ᴍᴜsɪᴄ** \n**<emoji id=6026256492619895014>🎵</emoji> ᴊᴜᴅᴜʟ ʟᴀɢᴜ** : [{songname}]({link})\nʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ : <b href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</b> \n\nᴄʀᴇᴀᴛᴇᴅ ʙʏ : {bot.me.mention} <b></blockquote>", disable_web_page_preview=True)
                    os.remove(dl)
                except Exception as hmme:
                    await huehue.edit(hmme)
        else:
            if len(m.command) < 2:
                await m.reply(f"<blockquote><b>{ggl} ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ᴀᴜᴅɪᴏ ғɪʟᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇᴛʜɪɴɢ ᴛᴏ sᴇᴀʀᴄʜ** <b></blockquote>")
            else:
                huehue = await m.reply("**Getting...**")
                query = m.text.split(None, 1)[1]
                search = ytsearch(query)
                if search == 0:
                    await huehue.edit(f"<blockquote><b>{ggl} ғᴏᴜɴᴅ ɴᴏᴛʜɪɴɢ ғᴏʀ ᴛʜᴇ ɢɪᴠᴇɴ ǫᴜᴇʀʏ ! <b></blockquote>")
                else:
                    songname = search[0]
                    url = search[1]
                    try:
                        file_name, title, yt_url, duration, views, channel, thumb, data_ytp = await YoutubeDownload(url)
                        if chat_id in QUEUE:
                            pos = add_to_queue(chat_id, songname, file_name, yt_url, "Audio", 0)
                            await huehue.edit(f"{brhsl} ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ᴀɴᴛʀɪᴀɴ #{pos}")
                        else:
                            try:
                                await client.call_py.play(
                                    chat_id,
                                    MediaStream(
                                    file_name,
                                    AudioQuality.STUDIO,
                                    ),
                                )                                
                                add_to_queue(chat_id, songname, file_name, yt_url, "Audio", 0)
                                await huehue.edit(f"<blockquote><b>**<emoji id=5895705279416241926>▶</emoji> ᴍᴇᴍᴜʟᴀɪ ᴍᴜsɪᴄ** \n**<emoji id=6026256492619895014>🎵</emoji> ᴊᴜᴅᴜʟ ʟᴀɢᴜ** : [{songname}]({link})\nʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ : <b href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</b> \n\nᴄʀᴇᴀᴛᴇᴅ ʙʏ : {bot.me.mention} <b></blockquote>", disable_web_page_preview=True)
                                os.remove(file_name)
                            except Exception as ep:
                                await huehue.edit(f"`{ep}`")
                    except Exception as e:
                        await huehue.edit(f"**YTDL ERROR ⚠️** \n\n`{str(e)}`")
    else:
        if len(m.command) < 2:
            await m.reply(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ᴀᴜᴅɪᴏ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ <code>play judul lagu</code><b></blockquote>")
        else:
            huehue = await m.reply(f"{prs} sᴇᴀʀᴄʜɪɴɢ...")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            if search == 0:
                await huehue.edit(f"{ggl} ғᴏᴜɴᴅ ɴᴏᴛʜɪɴɢ ғᴏʀ ᴛʜᴇ ɢɪᴠᴇɴ ǫᴜᴇʀʏ !")
            else:
                songname = search[0]
                url = search[1]
                try:
                    file_name, title, yt_url, duration, views, channel, thumb, data_ytp = await YoutubeDownload(url)
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, file_name, yt_url, "Audio", 0)
                        await huehue.edit(f"{brhsl} ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ᴀɴᴛʀɪᴀɴ #{pos}")
                    else:
                        try:
                            await client.call_py.play(
                                chat_id,
                                MediaStream(
                                file_name,
                                AudioQuality.STUDIO,
                                ),
                            )
                            add_to_queue(chat_id, songname, file_name, yt_url, "Audio", 0)
                            await huehue.edit(f"<blockquote><b>**<emoji id=5895705279416241926>▶</emoji> ᴍᴇᴍᴜʟᴀɪ ᴍᴜsɪᴄ** \n**<emoji id=6026256492619895014>🎵</emoji> ᴊᴜᴅᴜʟ ʟᴀɢᴜ** : [{songname}]({url}) \n**ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** <b href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</b> \n\n ᴄʀᴇᴀᴛᴇᴅ ʙʏ : {bot.me.mention}<b></blockquote>", disable_web_page_preview=True)
                            os.remove(file_name)
                        except Exception as ep:
                            await huehue.edit(f"`{ep}`")
                except Exception as e:
                    await huehue.edit(f"**YTDL ERROR ⚠️** \n\n`{str(e)}`")

async def lanjut_current_song(client, chat_id):
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        if len(chat_queue) == 1:
            try:
                await client.call_py.leave_call(chat_id)
            except NotInCallError:
                pass
            clear_queue(chat_id)
            return 1
        else:
            try:
                songname = chat_queue[1][0]
                url = chat_queue[1][1]
                link = chat_queue[1][2]
                type = chat_queue[1][3]
                Q = chat_queue[1][4]
                if type == "Audio":
                    await client.call_py.play(
                        chat_id,
                        MediaStream(
                            url,
                            AudioQuality.STUDIO,
                        ),
                    )
                elif type == "Video":
                    await client.call_py.play(
                        chat_id,
                        MediaStream(
                            url,
                        ),
                    )
                pop_an_item(chat_id)
                return [songname, link, type]
            except:
                await client.call_py.leave_call(chat_id)
                clear_queue(chat_id)
                return 2
    else:
        return 0

@CB.UBOT("skip")
async def skip(client, m: Message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await lanjut_current_song(client, chat_id)
        if op == 0:
            await m.reply(f"{ggl} <u>ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘᴇᴍᴜᴛᴀʀᴀɴ ᴍᴜsɪᴄ ʟᴀɪɴɴʏᴀ.</u>")
        elif op == 1:
            await m.reply(f"{ggl} <u>Qᴜᴇᴜᴇ ɪs Eᴍᴘᴛʏ, Lᴇᴀᴠɪɴɢ Vᴏɪᴄᴇ Cʜᴀᴛ...</u>")
        elif op == 2:
            await m.reply(f"{ggl} <b>Some Error Occurred</b> \n<b>Clearing the Queues and Leaving the Voice Chat...</b>")
        else:
            await m.reply(f"<blockquote><b><emoji id=6005994005148471369>⏩</emoji> **sᴋɪᴘᴘᴇᴅ ʙʏ :** <b href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</b> \n<emoji id=5895705279416241926>▶</emoji> ᴘᴇᴍᴜᴛᴀʀᴀɴ sᴇᴋᴀʀᴀɴɢ - {op[0]} \n\n ᴄʀᴇᴀᴛᴇᴅ ʙʏ : {bot.me.mention}<b></blockquote>", disable_web_page_preview=True)

    else:
        skip = m.text.split(None, 1)[1]
        OP = "**Removed the following songs from Queue:-**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)        

@CB.UBOT("end")
async def stop(client, m: Message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await client.call_py.leave_call(chat_id)
            clear_queue(chat_id)
            await m.reply(f"{brhsl} sᴛʀᴇᴀᴍɪɴɢ sᴇʟᴇsᴀɪ. !")
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply(f"<blockquote><b>{ggl} ᴛɪᴅᴀᴋ ᴀᴅᴀ sᴛʀᴇᴀᴍɪɴɢ ʏɢ ʙᴇʀᴊᴀʟᴀɴ.\nsɪʟᴀʜᴋᴀɴ ᴍᴇᴍᴜʟᴀɪ sᴛʀᴇᴀᴍ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ ᴜɴᴛᴜᴋ ᴍᴇᴍᴜʟᴀɪ ᴍᴜsɪᴄ !.<b></blockquote>")
   
@CB.UBOT("pause")
async def pause(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await client.call_py.pause_stream(chat_id)
            await m.reply(f"<blockquote><b><emoji id=6005824650293022970>⏸️</emoji> ᴍᴜsɪᴄ ᴅɪ ᴘᴀᴜsᴇ ᴏʟᴇʜ : <b href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</b> \n\n ᴄʀᴇᴀᴛᴇᴅ ʙʏ : {bot.me.mention}<b></blockquote>")
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply(f"<u>ᴛɪᴅᴀᴋ ᴀᴅᴀ sᴛʀᴇᴀᴍɪɴɢ ʏɢ ʙᴇʀᴊᴀʟᴀɴ.</u>")
      
@CB.UBOT("resume")
async def resume(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await client.call_py.resume_stream(chat_id)
            await m.reply(f"<blockquote><b>**<emoji id=5895705279416241926>▶</emoji> ᴘᴇᴍᴜᴛᴀʀᴀɴ ᴛᴇʟᴀʜ ᴅɪ ʟᴀɴᴊᴜᴛᴋᴀɴ ᴏʟᴇʜ :** <b href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</b> \n\n ᴄʀᴇᴀᴛᴇᴅ ʙʏ : {bot.me.mention}<b></blockquote>")
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply(f"<u>ᴛɪᴅᴀᴋ ᴀᴅᴀ sᴛʀᴇᴀᴍɪɴɢ ʏɢ ʙᴇʀᴊᴀʟᴀɴ.</u>")
          
