from userbot import *

__MODULE__ = "profiles"
__HELP__ = f"""
<blockquote><b>『 bantuan untuk profile 』

  <b>• perintah:</b> <code>{PREFIX[0]}setbio</code> [text]
  <b>• penjelasan:</b> untuk mengubah bio anda

  <b>• perintah:</b> <code>{PREFIX[0]}setname</code> [text]
  <b>• penjelasan:</b> untuk mengubah nama anda

  <b>• perintah:</b> <code>{PREFIX[0]}block</code> [reply to user]
  <b>• penjelasan:</b> untuk memblokir pengguna

  <b>• perintah:</b> <code>{PREFIX[0]}unblock</code> [reply to user]
  <b>• penjelasan:</b> untuk membuka blokir pengguna.<b></blockquote>
"""


@CB.UBOT("setbio")
async def _(client, message):
    await set_bio(client, message)


@CB.UBOT("setname")
async def _(client, message):
    await setname(client, message)


@CB.UBOT("block")
async def _(client, message):
    await block_user_func(client, message)


@CB.UBOT("unblock")
async def _(client, message):
    await unblock_user_func(client, message)