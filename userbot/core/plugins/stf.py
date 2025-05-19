import os
from userbot import *


async def staff_cmd(client, message):
    chat_title = message.chat.title
    creator = []
    co_founder = []
    admin = []
    async for x in message.chat.get_members():
        mention = f"<a href=tg://user?id={x.user.id}>{x.user.first_name} {x.user.last_name or ''}</a>"
        if (
            x.status.value == "administrator"
            and x.privileges
            and x.privileges.can_promote_members
        ):
            if x.custom_title:
                co_founder.append(f"<blockquote><b> ├  {mention} ➻ {x.custom_title}<b></blockquote>")
            else:
                co_founder.append(f"<blockquote><b> ├  {mention}<b></blockquote>")
        elif x.status.value == "administrator":
            if x.custom_title:
                admin.append(f"<blockquote><b> ├  {mention} ➻ {x.custom_title}<b></blockquote>")
            else:
                admin.append(f"<blockquote><b> ├  {mention}<b></blockquote>")
        elif x.status.value == "owner":
            if x.custom_title:
                creator.append(f"<blockquote><b> ╰  {mention} ➻ {x.custom_title}<b></blockquote>")
            else:
                creator.append(f"<blockquote><b> ╰  {mention}<b></blockquote>")
    if not co_founder and not admin:
        result = f"""
<b>Sᴛᴀғғ Gʀᴏᴜᴘ
{chat_title}

❏ Oᴡɴᴇʀ:
{creator[0]}</b>"""
    elif not co_founder:
        adm = admin[-1].replace("├ ", "╰ ")
        admin.pop(-1)
        admin.append(adm)
        result = f"""
Sᴛᴀғғ Gʀᴏᴜᴘ
{chat_title}

❏ Oᴡɴᴇʀ:
{creator[0]}

❏ Aᴅᴍɪɴ:
""" + "\n".join(
            admin
        )
    elif not admin:
        cof = co_founder[-1].replace("├ ", "╰ ")
        co_founder.pop(-1)
        co_founder.append(cof)
        result = f"""
Sᴛᴀғғ Gʀᴏᴜᴘ
{chat_title}

❏ Oᴡɴᴇʀ:
{creator[0]}

❏ CO-Fᴏᴜɴᴅᴇʀ:
""" + "\n".join(
            co_founder
        )
    else:
        adm = admin[-1].replace("├ ", "╰ ")
        admin.pop(-1)
        admin.append(adm)
        cof = co_founder[-1].replace("├ ", "╰ ")
        co_founder.pop(-1)
        co_founder.append(cof)
        result = (
            (
                f"""
Sᴛᴀғғ Gʀᴏᴜᴘ
{chat_title}

❏ Oᴡɴᴇʀ:
{creator[0]}

❏ CO-Fᴏᴜɴᴅᴇʀ:
"""
                + "\n".join(co_founder)
                + """

❏ Aᴅᴍɪɴ:
"""
            )
            + "\n".join(admin)
        )


    await message.reply(result)
