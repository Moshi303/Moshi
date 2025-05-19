from userbot import *

__MODULE__ = "pmpermit"
__HELP__ = """
<blockquote><b>bantuan untuk pmpermit

• perintah: <code>{0}antipm</code> [on atau off]
• penjelasan: untuk menghidupkan atau mematikan antipm

• perintah: <code>{0}setmsg</code> [balas atau berikan pesan]
• penjelasan: untuk mengatur pesan antipm.

• perintah: <code>{0}setlimit</code> [angka]
• penjelasan: untuk mengatur peringatan pesan blokir.

• perintah: <code>{0}ok</code>
• penjelasan: untuk menyetujui pesan.

• perintah: <code>{0}no</code>
• penjelasan: untuk menolak pesan.<b></blockquote>
"""



@CB.UBOT("antipm|pmpermit")
async def _(client, message):
    await permitpm(client, message)


@CB.UBOT("ok|a")
async def _(client, message):
    await approve(client, message)


@CB.UBOT("da|no")
async def _(client, message):
    await disapprove(client, message)


@CB.UBOT("setmsg")
async def _(client, message):
    await set_msg(client, message)


@CB.UBOT("setlimit")
async def _(client, message):
    await set_limit(client, message)


@CB.NOCMD("PMPERMIT", ubot)
async def _(client, message):
    await handle_pmpermit(client, message)
