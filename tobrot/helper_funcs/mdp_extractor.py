import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


import asyncio
from apdbot.helpers.display_progress import humanbytes
import json
import re
import os
import time
import pyrogram

from apdbot import (
    DEF_THUMB
)

async def mdp_url(url, cf_name, user_working_dir):
    thumb_image = DEF_THUMB
    PROCESS_RUN_TIME = 100
    cmd = [
        "streamlink",
        url
        ]
    LOGGER.info(cmd)
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    e = stderr.decode()
    if not e:
        e = "No Error"
        o = stdout.decode()
        if not o:
            o = "No Output"
        else:
            _o = o.split("\n")
            o = "`\n".join(_o)
    LOGGER.info({o})
    if re.search(r'Available streams', o):
        msg_to_export = o.split("Available streams:",1)[1]
    else:
        msg_to_export = "Failed To Extract Streams"
    inline_keyboard = []
    md_url = url
    save_ytdl_json_path = user_working_dir + \
        "/" + str("ytdleech") + ".json"
    with open(save_ytdl_json_path, "w", encoding="utf8") as outfile:
        json.dump(md_url, outfile, ensure_ascii=False)
    LOGGER.info(md_url)
    cb_string_low = "{}!{}!{}".format("video", "worst", cf_name)
    cb_string_best = "{}!{}!{}".format("video", "best", cf_name)
    cb_string_96 = "{}!{}!{}".format("video", "96p", cf_name)
    cb_string_144 = "{}!{}!{}".format("video", "144p", cf_name)
    cb_string_240 = "{}!{}!{}".format("video", "240p", cf_name)
    cb_string_360 = "{}!{}!{}".format("video", "360p", cf_name)
    cb_string_480 = "{}!{}!{}".format("video", "480p", cf_name)
    cb_string_576 = "{}!{}!{}".format("video", "576p", cf_name)
    cb_string_720 = "{}!{}!{}".format("video", "720p", cf_name)
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            "MP4 🎥 " + "(" + "worst" + ")", callback_data=cb_string_low.encode("UTF-8"))
    ])
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            "MP4 🎥 " + "(" + "best" + ")", callback_data=cb_string_best.encode("UTF-8"))
    ])
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            "MP4 🎥 " + "(" + "96p" + ")", callback_data=cb_string_96.encode("UTF-8"))
    ])
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            "MP4 🎥 " + "(" + "144p" + ")", callback_data=cb_string_144.encode("UTF-8"))
    ])
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            "MP4 🎥 " + "(" + "240p" + ")", callback_data=cb_string_240.encode("UTF-8"))
    ])
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            "MP4 🎥 " + "(" + "360p" + ")", callback_data=cb_string_360.encode("UTF-8"))
    ])
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            "MP4 🎥 " + "(" + "480p" + ")", callback_data=cb_string_480.encode("UTF-8"))
    ])
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            "MP4 🎥 " + "(" + "576p" + ")", callback_data=cb_string_576.encode("UTF-8"))
    ])
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            "MP4 🎥 " + "(" + "720p" + ")", callback_data=cb_string_720.encode("UTF-8"))
    ])
    reply_markup = pyrogram.InlineKeyboardMarkup(inline_keyboard)
    #LOGGER.info(reply_markup)
    if re.search(r'Available streams', o):
        msg_to_export = o.split("Available streams:",1)[1]
        succss_mesg = f"""<i>Available Formats : {msg_to_export}</i>"""
    else:
        msg_to_export = "Failed To Extract Streams"
        reply_markup = None
        succss_mesg = f"""Select the desired format: 👇
            <i>Available Formats : {msg_to_export}</i>"""
    return thumb_image, succss_mesg, reply_markup