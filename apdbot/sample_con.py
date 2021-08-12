import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    # Get these values from my.telegram.org
    # to store the channel ID who are authorized to use the bot
    AUTH = set(int(x) for x in os.environ.get("AUTH", "").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOC = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_SIZE = 50000000
    TG_MAX_SIZE = 2097152000
    FREE_UZR_MAX_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB = os.environ.get("DEF_THUMB", "https://telegra.ph/file/39fb5c2f312f128cb7946.jpg")
    # maximum message length in Telegram
    MAX_MSG_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_TIMEOUT = 3600
    #
    ARIA_STARTED_PORT = int(os.environ.get("ARIA_STARTED_PORT", 6800))
    EDIT_SLEEP_TIME = int(os.environ.get("EDIT_SLEEP_TIME", 1))
    MAX_TIME_TO_WAIT_FOR_START = int(os.environ.get("MAX_TIME_TO_WAIT_FOR_START", 3000))
    MAX_SIZE_TO_SPLIT = int(os.environ.get("MAX_SIZE_TO_SPLIT", 1987152000))
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "█")
    UN_FINISHED_PROGRESS_STR = os.environ.get("UN_FINISHED_PROGRESS_STR", "░")
    TG_OFFENSIVE_API = os.environ.get("TG_OFFENSIVE_API", None)
    CUSTOM_NAME = os.environ.get("CUSTOM_NAME", "")
    #Change Commands IN Conf.py
    #Leech Command
    LEECH_CMD = os.environ.get("LEECH_CMD", "leech")
    #YTDL Command
    YTDL_CMD = os.environ.get("YTDL_CMD", "ytdl")
    #PYTDL Command
    PYTDL_CMD = os.environ.get("PYTDL_CMD", "pytdl")
    #Cancel Command
    CANCEL_CMD = os.environ.get("CANCEL_CMD", "cancel")
    #Status Command
    STATUS_CMD = os.environ.get("STATUS_CMD", "status")
    #Stats Command
    STATS_CMD = os.environ.get("STATS_CMD", "stats")
    #Log Command
    LOG_CMD = os.environ.get("LOG_CMD", "log")
    #Save Thumbnail Command
    SAVE_CMD = os.environ.get("SAVE_CMD", "save")
    #Clear Thumbnail Command
    CLEAR_CMD = os.environ.get("CLEAR_CMD", "clear")
    #Upload Command
    UPLOAD_CMD = os.environ.get("UPLOAD_CMD", "upload")
    #Exec Command
    EXEC_CMD = os.environ.get("EXEC_CMD", "exec")
    #Help Command
    HELP_CMD = os.environ.get("HELP_CMD", "help")
    #
    