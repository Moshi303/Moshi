from userbot import *

__MODULE__ = "search"
__HELP__ = f"""
<blockquote><b>『 bantuan untuk search 』

  <b>• perintah:</b> <code>{PREFIX[0]}bing</code> or <code>{PREFIX[0]}pic</code> [query]
  <b>• penjelasan:</b> untuk mencari photo random dari google

  <b>• perintah:</b> <code>{PREFIX[0]}gif</code> [query]
  <b>• penjelasan:</b> untuk mencari gift/animation random dari google.<b></blockquote>
"""


@CB.UBOT("bing|pic")
async def _(client, message):
    await pic_bing_cmd(client, message)


@CB.UBOT("gif")
async def _(client, message):
    await gif_cmd(client, message)
