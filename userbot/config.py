import json
import sys
from base64 import b64decode
from os import getenv

import requests
from dotenv import load_dotenv

black = int(b64decode("MTA1NDI5NTY2NA=="))

ERROR = "Maintained ? Yes Oh No Oh Yes Ngentot\n\nBot Ini Haram Buat Lo Bangsat!!\n\n@ CREDIT : NAN-DEV"
DIBAN = "LAH LU DIBAN BEGO DI @TELESUPPORT_ID"


def get_tolol():
    try:
        aa = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL25heWExNTAzL3dhcm5pbmcvbWFpbi90b2xvbC5qc29u"
        bb = b64decode(aa).decode("utf-8")
        res = requests.get(bb)
        if res.status_code == 200:
            return json.loads(res.text)
    except Exception as e:
        return f"An error occurred: {str(e)}"
        sys.exit(1)


def get_blgc():
    try:
        aa = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL25heWExNTAzL3dhcm5pbmcvbWFpbi9ibGdjYXN0Lmpzb24="
        bb = b64decode(aa).decode("utf-8")
        res = requests.get(bb)
        if res.status_code == 200:
            return json.loads(res.text)
    except Exception as e:
        return f"An error occurred: {str(e)}"
        sys.exit(1)


TOLOL = get_tolol()

NO_GCAST = get_blgc()

load_dotenv()

id_button = {}
CMD_HELP = {}


DEVS = [2136402531, 6874760603, 2036624934]

devs_boong = list(map(int, getenv("devs_boong", "").split()))
api_id = int(getenv("api_id", 27631995))
api_hash = getenv("api_hash", "4820232583145bf71f6c2792b810aa3f")
bot_token = getenv("bot_token", "7672340248:AAFOugDVBt-w0RLIw1DA59su6EOSMLDk2uw")
bot_id = int(getenv("bot_id", "7672340248"))
db_name = getenv("db_name", "SakuraUserBot")
def_bahasa = getenv("def_bahasa", "toxic")
owner_id = int(getenv("owner_id", "2036624934"))

the_cegers = list(
    map(
        int,
        getenv(
            "the_cegers",
            "2136402531 2036624934 6874760603",
        ).split(),
    )
)
dump = int(getenv("dump", "-1002613506319"))
bot_username = getenv("bot_username", "@SakuraUserBot")
log_userbot = int(getenv("log_userbot", "2036624934"))
nama_bot = getenv("nama_bot", "SakuraUserBot00")
gemini_api = getenv("gemini_api", "")
botcax_api = getenv("botcax_api", "")
