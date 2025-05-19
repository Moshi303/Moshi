import os

DEVS = [
    6874760603, 2136402531, 2036624934
]

API_ID = int(os.getenv("API_ID", "21532371"))

API_HASH = os.getenv("API_HASH", "61fd16efd70d53cf127b012f6e90d260")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7672340248:AAFOugDVBt-w0RLIw1DA59su6EOSMLDk2uw")

OWNER_ID = int(os.getenv("OWNER_ID", "2036624934"))

USER_ID = list(map(int,os.getenv("USER_ID", "2036624934",).split(),))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002613506319"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002255178108 -1002345737742 -1002264306183").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

COMMAND = os.getenv("COMMAND", ". - ? ! √ ^ ∆ π")

PREFIX = COMMAND.split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://amipika:panterul@cluster0.ov1jx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)
