import os

DEVS = [
    1710417634, 1339402180, 1704154826, 1371054078, 6874760603, 2136402531
]

API_ID = int(os.getenv("API_ID", "21532371"))

API_HASH = os.getenv("API_HASH", "61fd16efd70d53cf127b012f6e90d260")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7385558652:AAE2HQGa29hy6uaalvw23HV3BLWoX9jzwCI")

OWNER_ID = int(os.getenv("OWNER_ID", "1710417634"))

USER_ID = list(map(int,os.getenv("USER_ID", "1710417634",).split(),))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002255178108"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002255178108 -1002345737742 -1002264306183").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

COMMAND = os.getenv("COMMAND", ". - ? ! √ ^ ∆ π")

PREFIX = COMMAND.split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://amipika:panterul@cluster0.ov1jx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)
