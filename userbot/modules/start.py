from .. import *


@CB.UBOT("ping")
async def _(client, message):
    await ping_cmd(client, message)


@CB.BOT("start")
async def _(client, message):
    await start_cmd(client, message)