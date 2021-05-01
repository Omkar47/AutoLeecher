import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    # Get these values from my.telegram.org
    # to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = set(int(x) for x in os.environ.get("AUTH_CHANNEL", "").split())
    # For Admin Commands add user IDs 
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 1572864000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://telegra.ph/file/39fb5c2f312f128cb7946.jpg")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    #
    ARIA_TWO_STARTED_PORT = int(os.environ.get("ARIA_TWO_STARTED_PORT", 6800))
    EDIT_SLEEP_TIME_OUT = int(os.environ.get("EDIT_SLEEP_TIME_OUT", 1))
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = int(os.environ.get("MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START", 600))
    MAX_TG_SPLIT_FILE_SIZE = int(os.environ.get("MAX_TG_SPLIT_FILE_SIZE", 1072864000))
    #Change Commands IN Config.py
    #Leech Command
    LEECH_CMD = os.environ.get("LEECH_CMD", "leech")
    #YTDL Command
    YTDL_CMD = os.environ.get("YTDL_CMD", "ytdl")
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
    #Delete Thumbnail Command
    DELETE_CMD = os.environ.get("DELETE_CMD", "delete")
    #Upload Command
    UPLOAD_CMD = os.environ.get("UPLOAD_CMD", "upload")
    #Exec Command
    EXEC_CMD = os.environ.get("EXEC_CMD", "exec")
    #Help Command
    HELP_CMD = os.environ.get("HELP_CMD", "help")
    #
