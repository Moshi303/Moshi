from .http import http


class QuotlyException(Exception):
    pass


class ColorManager:
    def __init__(self):
        self.list_colors = [
            "white",
            "navy",
            "blue",
            "green",
            "teal",
            "aqua",
            "cyan",
            "royalblue",
            "steelblue",
            "darkblue",
            "lightskyblue",
            "skyblue",
            "lightgreen",
            "mediumseagreen",
            "forestgreen",
            "olive",
            "gray",
            "darkgray",
            "lightgray",
            "purple",
            "pink",
            "red",
            "orange",
            "yellow",
            "magenta",
            "violet",
            "crimson",
            "brown",
            "beige",
            "gold",
            "silver",
            "peachpuff",
            "coral",
            "lime",
            "springgreen",
            "mediumspringgreen",
            "deeppink",
            "indigo",
            "slateblue",
            "lightpink",
            "orangered",
            "darkorange",
            "lightsalmon",
            "darkolivegreen",
            "peru",
            "chocolate",
            "khaki",
            "lightsteelblue",
            "lavender",
            "powderblue",
            "mistyrose",
            "slategray",
            "honeydew",
            "mintcream",
            "wheat",
            "ivory",
            "floralwhite",
            "snow",
            "beige",
            "black",
        ]
        self.color_translations = {
            "white": "putih",
            "navy": "biru dongker",
            "blue": "biru",
            "green": "hijau",
            "teal": "toska",
            "aqua": "air",
            "cyan": "cyan",
            "royalblue": "biru kerajaan",
            "steelblue": "biru baja",
            "darkblue": "biru gelap",
            "lightskyblue": "biru langit muda",
            "skyblue": "biru langit",
            "lightgreen": "hijau muda",
            "mediumseagreen": "hijau laut sedang",
            "forestgreen": "hijau hutan",
            "olive": "zaitun",
            "gray": "abu-abu",
            "darkgray": "abu-abu gelap",
            "lightgray": "abu-abu muda",
            "purple": "ungu",
            "pink": "merah muda",
            "red": "merah",
            "orange": "oranye",
            "yellow": "kuning",
            "magenta": "magenta",
            "violet": "ungu tua",
            "crimson": "merah tua",
            "brown": "coklat",
            "beige": "krem",
            "gold": "emas",
            "silver": "perak",
            "peachpuff": "peach",
            "coral": "merah karang",
            "lime": "limau",
            "springgreen": "hijau musim semi",
            "mediumspringgreen": "hijau semi sedang",
            "deeppink": "merah jambu tua",
            "indigo": "nila",
            "slateblue": "biru batu tulis",
            "lightpink": "merah muda terang",
            "orangered": "merah jingga",
            "darkorange": "oranye gelap",
            "lightsalmon": "salem muda",
            "darkolivegreen": "hijau zaitun gelap",
            "peru": "peru",
            "chocolate": "coklat tua",
            "khaki": "kaki",
            "lightsteelblue": "biru baja terang",
            "lavender": "lavender",
            "powderblue": "biru bubuk",
            "mistyrose": "mawar berkabut",
            "slategray": "abu-abu batu tulis",
            "honeydew": "madu",
            "mintcream": "krim mint",
            "wheat": "gandum",
            "ivory": "gading",
            "floralwhite": "putih bunga",
            "snow": "salju",
            "black": "hitam",
        }

    def get_colors(self, name):
        name = name.lower()
        if name in self.list_colors:
            return name
        elif name in self.color_translations.values():
            return next(
                (eng for eng, indo in self.color_translations.items() if indo == name),
                None,
            )
        return None

    def is_color(self, name):
        name = name.lower()
        return name in self.list_colors or name in self.color_translations.values()

    def get_list_colors(self, lang="en"):
        if lang == "en":
            return self.list_colors
        elif lang == "id":
            return list(self.color_translations.values())
        else:
            raise ValueError(
                "Bahasa tidak dikenali. Gunakan 'en' untuk Inggris atau 'id' untuk Indonesia."
            )


CM = ColorManager()


async def get_sender(message):
    if message.forward_date:
        if message.forward_sender_name:
            return 1
        elif message.forward_from:
            return message.forward_from.id
        elif message.forward_from_chat:
            return message.forward_from_chat.id
        else:
            return 1
    elif message.from_user:
        return message.from_user.id
    elif message.sender_chat:
        return message.sender_chat.id
    else:
        return 1


async def sender_name(message):
    if message.forward_date:
        if message.forward_sender_name:
            return message.forward_sender_name
        elif message.forward_from:
            return (
                f"{message.forward_from.first_name} {message.forward_from.last_name or ''}"
                if message.forward_from.last_name
                else message.forward_from.first_name
            )

        elif message.forward_from_chat:
            return message.forward_from_chat.title
        else:
            return ""
    elif message.from_user:
        if message.from_user.last_name:
            return f"{message.from_user.first_name} {message.from_user.last_name or ''}"
        else:
            return message.from_user.first_name
    elif message.sender_chat:
        return message.sender_chat.title
    else:
        return ""


async def sender_emoji(message):
    if message.forward_date:
        return (
            ""
            if message.forward_sender_name
            or not message.forward_from
            and message.forward_from_chat
            or not message.forward_from
            else message.forward_from.emoji_status.custom_emoji_id
        )

    return message.from_user.emoji_status.custom_emoji_id if message.from_user else ""


async def sender_username(message):
    if message.forward_date:
        if (
            not message.forward_sender_name
            and not message.forward_from
            and message.forward_from_chat
            and message.forward_from_chat.username
        ):
            return message.forward_from_chat.username
        elif (
            not message.forward_sender_name
            and not message.forward_from
            and message.forward_from_chat
            or message.forward_sender_name
            or not message.forward_from
        ):
            return ""
        else:
            return message.forward_from.username or ""
    elif message.from_user and message.from_user.username:
        return message.from_user.username
    elif (
        message.from_user
        or message.sender_chat
        and not message.sender_chat.username
        or not message.sender_chat
    ):
        return ""
    else:
        return message.sender_chat.username


async def sender_photo(message):
    if message.forward_date:
        if (
            not message.forward_sender_name
            and not message.forward_from
            and message.forward_from_chat
            and message.forward_from_chat.photo
        ):
            return {
                "small_file_id": message.forward_from_chat.photo.small_file_id,
                "small_photo_unique_id": message.forward_from_chat.photo.small_photo_unique_id,
                "big_file_id": message.forward_from_chat.photo.big_file_id,
                "big_photo_unique_id": message.forward_from_chat.photo.big_photo_unique_id,
            }
        elif (
            not message.forward_sender_name
            and not message.forward_from
            and message.forward_from_chat
            or message.forward_sender_name
            or not message.forward_from
        ):
            return ""
        else:
            return (
                {
                    "small_file_id": message.forward_from.photo.small_file_id,
                    "small_photo_unique_id": message.forward_from.photo.small_photo_unique_id,
                    "big_file_id": message.forward_from.photo.big_file_id,
                    "big_photo_unique_id": message.forward_from.photo.big_photo_unique_id,
                }
                if message.forward_from.photo
                else ""
            )

    elif message.from_user and message.from_user.photo:
        return {
            "small_file_id": message.from_user.photo.small_file_id,
            "small_photo_unique_id": message.from_user.photo.small_photo_unique_id,
            "big_file_id": message.from_user.photo.big_file_id,
            "big_photo_unique_id": message.from_user.photo.big_photo_unique_id,
        }
    elif (
        message.from_user
        or message.sender_chat
        and not message.sender_chat.photo
        or not message.sender_chat
    ):
        return ""
    else:
        return {
            "small_file_id": message.sender_chat.photo.small_file_id,
            "small_photo_unique_id": message.sender_chat.photo.small_photo_unique_id,
            "big_file_id": message.sender_chat.photo.big_file_id,
            "big_photo_unique_id": message.sender_chat.photo.big_photo_unique_id,
        }


async def t_or_c(message):
    if message.text:
        return message.text
    elif message.caption:
        return message.caption
    else:
        return ""


async def quotly(messages, kolor):
    if not isinstance(messages, list):
        messages = [messages]
    payload = {
        "type": "quote",
        "format": "png",
        "backgroundColor": kolor,
        "messages": [],
    }
    for message in messages:
        m_dict = {}

        entities = message.entities or message.caption_entities or []
        m_dict["entities"] = [
            {
                "type": entity.type.name.lower(),
                "offset": entity.offset,
                "length": entity.length,
            }
            for entity in entities
        ]

        m_dict["chatId"] = await get_sender(message)
        m_dict["text"] = await t_or_c(message) or ""
        m_dict["avatar"] = True
        m_dict["from"] = {
            "id": await get_sender(message),
            "name": await sender_name(message) or "",
            "username": await sender_username(message) or "",
            "type": message.chat.type.name.lower(),
            "photo": await sender_photo(message) or {},
        }

        if message.reply_to_message:
            reply_text = await t_or_c(message.reply_to_message)
            if reply_text:
                m_dict["replyMessage"] = {
                    "name": await sender_name(message.reply_to_message) or "",
                    "text": reply_text,
                    "chatId": await get_sender(message.reply_to_message),
                }
        else:
            m_dict["replyMessage"] = {}

        if m_dict["text"]:
            payload["messages"].append(m_dict)

    if not payload["messages"]:
        raise QuotlyException(
            "<b>Terjadi Kesalahan Saat membuat Sticker.\nKarena Pesan Teks Tidak Valid.</b>"
        )

    r = await http.post("https://bot.lyo.su/quote/generate.png", json=payload)

    if r.is_error:
        error_message = f"<b>Error <code>{r.status_code}: {r.text}</code></b>"
        raise QuotlyException(error_message)

    try:
        return r.read()
    except ValueError as e:
        error_message = (
            f"<b>Error: Respons tidak valid dari server: <code>{str(e)}</code></b>"
        )
        raise QuotlyException(error_message)


def isArgInt(txt) -> list:
    count = txt
    try:
        count = int(count)
        return [True, count]
    except ValueError:
        return [False, 0]
        