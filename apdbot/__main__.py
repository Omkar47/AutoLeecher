# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import os

from apdbot import (
    DOWNLOAD_LOC,
    BOT_TOKEN,
    APP_ID,
    API_HASH,
    AUTH,
    CANCEL_CMD,
    LEECH_CMD,
    YTDL_CMD,
    PYTDL_CMD,
    STATUS_CMD,
    STATS_CMD,
    LOG_CMD,
    SAVE_CMD,
    CLEAR_CMD,
    HELP_CMD,
    UPLOAD_CMD,
    EXEC_CMD
)

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler

from apdbot.plugins.incoming_msg import incoming_msg, incoming_ytdl, ytdl_list
from apdbot.plugins.status_msg import (
    status_msg,
    cancel_msg,
    exec_msg,
    upload_doc,
    upload_log_file,
    stats_msg
)

from apdbot.plugins.new_join import help_msg
from apdbot.plugins.call_back_butn_handler import button
from apdbot.plugins.custom_thumb import (
    save_thumb,
    clear_thumb
)

if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(DOWNLOAD_LOC):
        os.makedirs(DOWNLOAD_LOC)
    #
    app = Client(
        "APDBot",
        bot_token=BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        workers=343
    )
    #
    incoming_msg_handler = MessageHandler(
        incoming_msg,
        filters=filters.command([f"{LEECH_CMD}"]) & filters.chat(chats=AUTH)
    )
    app.add_handler(incoming_msg_handler)
    #
    incoming_ytdl_handler = MessageHandler(
        incoming_ytdl,
        filters=filters.command([f"{YTDL_CMD}"]) & filters.chat(chats=AUTH)
    )
    app.add_handler(incoming_ytdl_handler)
    #
    incoming_youtube_playlist_dl_handler = MessageHandler(
        ytdl_list,
        filters=filters.command([f"{PYTDL_CMD}"]) & filters.chat(chats=AUTH)
    )
    app.add_handler(incoming_youtube_playlist_dl_handler)
    #
    status_msg_handler = MessageHandler(
        status_msg,
        filters=filters.command([f"{STATUS_CMD}"]) & filters.chat(chats=AUTH)
    )
    app.add_handler(status_msg_handler)
    #
    stats_msg_handler = MessageHandler(
        stats_msg,
        filters=filters.command([f"{STATS_CMD}"]) & filters.chat(chats=AUTH)
    )
    app.add_handler(stats_msg_handler)
    #
    cancel_msg_handler = MessageHandler(
        cancel_msg,
        filters=filters.command([f"{CANCEL_CMD}"]) & filters.chat(chats=AUTH)
    )
    app.add_handler(cancel_msg_handler)
    #
    exec_msg_handler = MessageHandler(
        exec_msg,
        filters=filters.command([f"{EXEC_CMD}"]) & filters.chat(chats=AUTH)
    )
    app.add_handler(exec_msg_handler)
    #
    upload_doc_handler = MessageHandler(
        upload_doc,
        filters=filters.command([f"{UPLOAD_CMD}"]) & filters.chat(chats=AUTH)
    )
    app.add_handler(upload_doc_handler)
    #
    call_back_butn_handler = CallbackQueryHandler(
        button
    )
    app.add_handler(call_back_butn_handler)
    #
    save_thumb_handler = MessageHandler(
        save_thumb,
        filters=filters.command([f"{SAVE_CMD}"]) & filters.chat(chats=AUTH)
    )
    app.add_handler(save_thumb_handler)
    #
    clear_thumb_handler = MessageHandler(
        clear_thumb,
        filters=filters.command([f"{CLEAR_CMD}"]) & filters.chat(chats=AUTH)
    )
    app.add_handler(clear_thumb_handler)
    #
    upload_log_handler = MessageHandler(
        upload_log_file,
        filters=filters.command([f"{LOG_CMD}"]) & filters.chat(chats=AUTH)
    )
    app.add_handler(upload_log_handler)
    #
    help_msg_handler = MessageHandler(
        help_msg,
        filters=filters.command([f"{HELP_CMD}"]) & filters.chat(chats=AUTH)
    )
    app.add_handler(help_msg_handler)
    #
    help_msg_handler = MessageHandler(
        help_msg,
        filters=filters.command(["help"]) & filters.chat(chats=AUTH)
    )
    app.add_handler(help_msg_handler)
    #
    app.run()
