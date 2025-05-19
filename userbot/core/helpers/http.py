from asyncio import gather

import aiohttp
import httpx
from aiohttp import ClientSession


async def setup():
    global aiosession
    aiosession = ClientSession()


http = httpx.AsyncClient(
    http2=True,
    verify=False,
    timeout=httpx.Timeout(40),
)


BASE = "https://batbin.me/"


dev_paste = {
    "nekobin": {
        "URL": "https://nekobin.com/api/documents",
        "RAV": "result.key",
        "GAS": "https://github.com/nekobin/nekobin",
    },
    "pasty": {
        "URL": "https://pasty.lus.pm/api/v2/pastes",
        "HEADERS": {
            "User-Agent": "PyroGramBot/6.9",
            "Content-Type": "application/json",
        },
        "RAV": "id",
        "GAS": "https://github.com/lus/pasty",
        "AVDTS": "modificationToken",
    },
    "pasting": {
        "URL": "https://pasting.codes/api",
    },
}


async def create_session():
    return aiohttp.ClientSession()


async def get(session, url: str, *args, **kwargs):
    async with session.get(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data


async def head(session, url: str, *args, **kwargs):
    async with session.head(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data


async def post(session, url: str, *args, **kwargs):
    async with session.post(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data


async def multiget(session, url: str, times: int, *args, **kwargs):
    return await gather(*[get(session, url, *args, **kwargs) for _ in range(times)])


async def multihead(session, url: str, times: int, *args, **kwargs):
    return await gather(*[head(session, url, *args, **kwargs) for _ in range(times)])


async def multipost(session, url: str, times: int, *args, **kwargs):
    return await gather(*[post(session, url, *args, **kwargs) for _ in range(times)])


async def resp_get(session, url: str, *args, **kwargs):
    return await get(session, url, *args, **kwargs)


async def resp_post(session, url: str, *args, **kwargs):
    return await post(session, url, *args, **kwargs)


async def paste(content: str):
    async with aiohttp.ClientSession() as session:
        resp = await post(session, f"{BASE}api/v2/paste", json={"content": content})
        if not resp["success"]:
            return
        return BASE + resp["message"]
        