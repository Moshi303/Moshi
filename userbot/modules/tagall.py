
__MODULE__ = "tagall"
__HELP__ = f"""
<blockquote><b>『 bantuan untuk tagall 』

  <b>• perintah:</b> <code>tagall</code> [pesan - rep_pesan]
  <b>• penjelasan:</b> untuk tagall kesemua member grup

  <b>• perintah:</b> <code>batal</code>
  <b>• penjelasan:</b> untuk menghentikan tagall.<b></blockquote>
"""

import asyncio
from random import shuffle

from userbot import *

tagallgcid = []

emoji_categories = {
    "smileys": [
        "😀",
        "😃",
        "😄",
        "😁",
        "😆",
        "😅",
        "😂",
        "🤣",
        "😊",
        "😍",
        "🥰",
        "😘",
        "😎",
        "🥳",
        "😇",
        "🙃",
        "😋",
        "😛",
        "🤪",
    ],
    "animals": [
        "🐶",
        "🐱",
        "🐰",
        "🐻",
        "🐼",
        "🦁",
        "🐸",
        "🦊",
        "🦔",
        "🦄",
        "🐢",
        "🐠",
        "🐦",
        "🦜",
        "🦢",
        "🦚",
        "🦓",
        "🐅",
        "🦔",
    ],
    "food": [
        "🍎",
        "🍕",
        "🍔",
        "🍟",
        "🍩",
        "🍦",
        "🍓",
        "🥪",
        "🍣",
        "🍔",
        "🍕",
        "🍝",
        "🍤",
        "🥗",
        "🥐",
        "🍪",
        "🍰",
        "🍫",
        "🥤",
    ],
    "nature": [
        "🌲",
        "🌺",
        "🌞",
        "🌈",
        "🌊",
        "🌍",
        "🍁",
        "🌻",
        "🌸",
        "🌴",
        "🌵",
        "🍃",
        "🍂",
        "🌼",
        "🌱",
        "🌾",
        "🍄",
        "🌿",
        "🌳",
    ],
    "travel": [
        "✈️",
        "🚀",
        "🚲",
        "🚗",
        "⛵",
        "🏔️",
        "🚁",
        "🚂",
        "🏍️",
        "🚢",
        "🚆",
        "🛴",
        "🛸",
        "🛶",
        "🚟",
        "🚈",
        "🛵",
        "🛎️",
        "🚔",
    ],
    "sports": [
        "⚽",
        "🏀",
        "🎾",
        "🏈",
        "🎱",
        "🏓",
        "🥊",
        "⛳",
        "🏋️",
        "🏄",
        "🤸",
        "🏹",
        "🥋",
        "🛹",
        "🥏",
        "🎯",
        "🥇",
        "🏆",
        "🥅",
    ],
    "music": ["🎵", "🎶", "🎤", "🎧", "🎼", "🎸", "🥁", "🎷", "🎺", "🎻", "🪕", "🎹", "🔊"],
    "celebration": ["🎉", "🎊", "🥳", "🎈", "🎁", "🍰", "🧁", "🥂", "🍾", "🎆", "🎇"],
    "work": ["💼", "👔", "👓", "📚", "✏️", "📆", "🖥️", "🖊️", "📂", "📌", "📎"],
    "emotions": ["❤️", "💔", "😢", "😭", "😠", "😡", "😊", "😃", "🙄", "😳", "😇", "😍"],
}

def emoji_random():
    random_category = random.choice(tuple(emoji_categories.keys()))
    return random.choice(emoji_categories[random_category])


@CB.UBOT("tagall")
async def _(client, message):
    if message.chat.id in tagallgcid:
        return
    tagallgcid.append(message.chat.id)
    text = message.text.split(None, 1)[1] if len(message.text.split()) != 1 else ""
    users = [
        f"<blockquote><b><a href=tg://user?id={member.user.id}>{emoji_random()}</a></b></blockquote>"
        async for member in message.chat.get_members()
        if not (member.user.is_bot or member.user.is_deleted)
    ]
    shuffle(users)
    m = message.reply_to_message or message
    for output in [users[i : i + 5] for i in range(0, len(users), 5)]:
        if message.chat.id not in tagallgcid:
            break
        await m.reply_text(
            f"<blockquote><b>{text}</b></blockquote>\n<blockquote><b>{' '.join(output)}</b></blockquote>", quote=bool(message.reply_to_message)
        )
        await asyncio.sleep(2)
    try:
        tagallgcid.remove(message.chat.id)
    except Exception:
        pass


@CB.UBOT("batal")
async def _(client, message):
    if message.chat.id not in tagallgcid:
        return await message.reply_text(
            "<b>ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘᴇʀɪɴᴛᴀʜ: <code>tagall</code> ʏᴀɴɢ ᴅɪɢᴜɴᴀᴋᴀɴ</b>"
        )
    try:
        tagallgcid.remove(message.chat.id)
    except Exception:
        pass
    await message.reply_text("<b>ᴛᴀɢᴀʟʟ ʙᴇʀʜᴀsɪʟ ᴅɪʙᴀᴛᴀʟᴋᴀɴ</b>")
