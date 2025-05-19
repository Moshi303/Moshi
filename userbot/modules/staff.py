from userbot import *

__MODULE__ = "staff"
__HELP__ = f"""
<blockquote><b>『 bantuan untuk staff 』

  <b>• perintah:</b> <code>{PREFIX[0]}staff</code> [ip addreꜱ]
  <b>• penjelasan:</b> untuk mendapatkan informasi seluruh staff grup.<b></blockquote>
  """


@CB.UBOT("staff")
async def _(client, message):
    await staff_cmd(client, message)