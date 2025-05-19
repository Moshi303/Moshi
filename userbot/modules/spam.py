from userbot import *

__MODULE__ = "spam"
__HELP__ = f"""
<blockquote>『 bantuan untuk spam 』

  <b>• perintah:</b> <code>{PREFIX[0]}spam</code> [jumlah_pesan - pesan_spam]
  <b>• penjelasan:</b> untuk spam pesan

  <b>• perintah:</b> <code>{PREFIX[0]}dspam</code> [jumlah_pesan - jumlah_delay_detik - pesan_spam]
  <b>• penjelasan:</b> untuk spam pesan delay.<b></blockquote>
"""

@CB.UBOT("spam|dspam")
async def _(client, message):
    if message.command[0] == "spam":
        await spam_cmd(client, message)
    if message.command[0] == "dspam":
        await dspam_cmd(client, message)

@CB.UBOT("spamg")
async def _(client, message):
    if message.command[0] == "spamg":
        await spam_broadcast_cmd(client, message)
