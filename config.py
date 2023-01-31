# Credits: @tgflash
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/tgflash & t.me/Tgflash

from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")


API_HASH = getenv("API_HASH", "24385183c93a98ae4155c25d9f5f64b2")
API_ID = int(getenv("API_ID", "6296490"))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001473548283]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID", "-1001647004968") or 0)
BOT_VER = "0.2.0@main"
BRANCH = getenv("BRANCH", "main")
CHANNEL = getenv("CHANNEL", "tgflash")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "mongodb+srv://pankajsain:pankaj9024@cluster0.fdc33h6.mongodb.net/?retryWrites=true&w=majorit")
GIT_TOKEN = getenv("GIT_TOKEN", "")
GROUP = getenv("GROUP", "tgflash")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
REPO_URL = getenv("REPO_URL", "https://github.com/mrismanaziz/PyroMan-Userbot")
STRING_SESSION1 = getenv("STRING_SESSION1", "1BJWap1sBu1WDNirSFt2zhK2dhSC6-p2lYSd_wM4uv1vwgUWEliHrqbLBOdMKI0dEm0ZfuXOFFtCB9R1kQSrZSn1aqNiqG-3pD-vljRbJJ8HSYTIHoA-JP0FLJkBZMrmj4juRid2VUG6yaR7m7P_dxcMgCtzghZgeb_AWS8SleFnXFj-73P8Hnv0a2BfaBd9DsfyzaeXvG-QzQNhZGgl_Aceq3v_9sWhBegg10XmdLtmOwy3Wo4OgaCONDeZExE26Vxi40QlZEm0bFGK_3rbSAmogrNl_Sr8qPQA376HNV4sbL62u2wXBPSpRYL-w4E5W55Oi3IiNYk0JKxJHs62z_ZpHfiS_6QI=")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
