from time import time
import asyncio
from userbot import *

__MODULE__ = "ᴀғᴋ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀғᴋ 』

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}afk</code></code>
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴀғᴋ

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}unafk</code></code>
  <b>➢ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ᴀғᴋ<b></blockquote>
"""


class awayFromKeyboard:
    def __init__(self, client, message, reason=""):
        self.client = client
        self.message = message
        self.reason = reason

    async def set_afk(self):
        db_afk = {"<blockquote><b>time<b></blockquote>": time(), "reason": self.reason}
        msg_afk = (
            f"<blockquote><b>❏ sedang afk\n╰ alasan: {self.reason}<b></blockquote>"
            if self.reason
            else "<blockquote><b>❏ sedang afk<b></blockquote>"
        )
        await set_vars(self.client.me.id, "AFK", db_afk)
        ae = await self.message.reply(msg_afk, disable_web_page_preview=True)
        await asyncio.sleep(3)
        return await ae.delete()

    async def get_afk(self):
        vars = await get_vars(self.client.me.id, "AFK")
        if vars:
            afk_time = vars.get(f"<blockquote><b>time<b></blockquote>")
            afk_reason = vars.get(f"<blockquote><b>reason<b></blockquote>")
            afk_runtime = await get_time(time() - afk_time)
            afk_text = (
                f"<blockquote<b>❏ sedang afk\n├ waktu: {afk_runtime}\n ╰ alasan: {afk_reason}<b></blockquote>>"
                if afk_reason
                else f"<blockquote><b>❏ sedang afk\n╰ waktu: {afk_runtime}<b></blockquote>"
            )
            ae = await self.message.reply(afk_text, disable_web_page_preview=True)
            await asyncio.sleep(3)
            return await ae.delete()

    async def unset_afk(self):
        vars = await get_vars(self.client.me.id, "AFK")
        if vars:
            afk_time = vars.get("<blockquote><b>time<b></blockquote>")
            afk_runtime = await get_time(time() - afk_time)
            afk_text = f"<blockquote><b>❏ kembali online\n╰ afk selama: {afk_runtime}<b></blockquote>"
            await remove_vars(self.client.me.id, "AFK")
            ae = await self.message.reply(afk_text)
            await asyncio.sleep(3)
            return await ae.delete()


@CB.UBOT("afk")
async def _(client, message):
    reason = get_arg(message)
    afk_handler = awayFromKeyboard(client, message, reason)
    await afk_handler.set_afk()


@CB.NOCMD("AFK", ubot)
async def _(client, message):
    afk_handler = awayFromKeyboard(client, message)
    await afk_handler.get_afk()


@CB.UBOT("unafk")
async def _(client, message):
    afk_handler = awayFromKeyboard(client, message)
    return await afk_handler.unset_afk()
