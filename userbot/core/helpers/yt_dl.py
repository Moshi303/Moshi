from asyncio import get_event_loop
from functools import partial

from yt_dlp import YoutubeDL


def run_sync(func, *args, **kwargs):
    return get_event_loop().run_in_executor(None, partial(func, *args, **kwargs))

mycookies = "ryn_cookies.txt"

async def YoutubeDownload(url, as_video=False):
    if as_video:
        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "format": "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "nocheckcertificate": True,
            "cookiefile": mycookies,
            "geo_bypass": True,
        }
    else:
        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "cookiefile": mycookies,
            "format": "bestaudio[ext=m4a]",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "nocheckcertificate": True,
            "geo_bypass": True,
        }
    data_ytp = "<blockquote><b>💡 informasi {}</b>\n\n<b>🏷 nama:</b> {}<b>\n<b>🧭 durasi:</b> {}\n<b>👀 dilihat:</b> {}\n<b>📢 channel:</b> {}\n<b>🔗 tautan:</b> <a href={}>youtube</a>\n\n<b>⚡ powered by: {}<b></blockquote>"
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
