import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


import os

from apdbot import (
    DOWNLOAD_LOC
)


import time
import aria2p
import asyncio
from apdbot.helpers.extract_link_from_message import extract_link
from apdbot.helpers.download_aria import call_apropriate_function, aria_start
from apdbot.helpers.download_from_link import request_download
from apdbot.helpers.display_progress import progress_for_pyrogram
from apdbot.helpers.ytdl_extractor import extract_youtube_dl_formats, extract_zmhdl_formats
from apdbot.helpers.ytplaylist import yt_playlist_downg
from apdbot.helpers.admin_check import AdminCheck
from apdbot.helpers.fix_tcerrocni_images import proc_ess_image_aqon
        
async def incoming_purge_msg(client, message):
    """/purge command"""
    i_m_sefg2 = await message.reply_text("Purging...", quote=True)
    if await AdminCheck(client, message.chat.id, message.from_user.id):
        aria_i_p = await aria_start()
        # Show All Downloads
        downloads = aria_i_p.get_downloads()
        for download in downloads:
            LOGGER.info(download.remove(force=True))
    await i_m_sefg2.delete()

async def incoming_msg(client, message):
    """/leech command"""
    g_id = message.from_user.id
    gu_id = message.from_user.first_name
    credit = await message.reply_text(f"Leeching for : <a href='tg://user?id={g_id}'>{gu_id}</a>", parse_mode="html")
    i_m_sefg = await credit.reply_text("`Processing...`", quote=True)
    is_zip = False
    is_unzip = False
    if len(message.command) > 1:
        if message.command[1] == "archive":
            is_zip = True
        elif message.command[1] == "unzip":
            is_unzip = True
    # get link from the incoming message
    dl_url, cf_name, _, _ = await extract_link(message.reply_to_message, "LEECH")
    LOGGER.info(dl_url)
    LOGGER.info(cf_name)
    if dl_url is not None:
        await i_m_sefg.edit_text("`Extracting/Parsing Link...`")
        # start the aria2c daemon
        aria_i_p = await aria_start()
        LOGGER.info(aria_i_p)
        current_user_id = message.from_user.id
        # create an unique directory
        new_download_location = os.path.join(
            DOWNLOAD_LOC,
            str(current_user_id),
            str(time.time())
        )
        # create download directory, if not exist
        if not os.path.isdir(new_download_location):
            os.makedirs(new_download_location)
        await i_m_sefg.edit_text("`Trying to Download...`")
        # try to download the "link"
        sagtus, err_message = await call_apropriate_function(
            aria_i_p,
            dl_url,
            new_download_location,
            i_m_sefg,
            is_zip,
            cf_name,
            is_unzip,
            message
        )
        if not sagtus:
            # if FAILED, display the error message
            await i_m_sefg.edit_text(err_message)
    else:
        await i_m_sefg.edit_text(
            "**WTF**! This Incorrect Way To Use the bot.\nPlease Read Pinned Messages or Check /help.\n\n"
            f"<b>API Error</b>: {cf_name}"
        )


async def incoming_ytdl(client, message):
    """ /ytdl command """
    i_m_sefg = await message.reply_text("`Processing...`", quote=True)
    # LOGGER.info(message)
    # extract link from message
    custom_file_name = None
    url = None
    youtube_dl_username = None
    youtube_dl_password = None
    dl_url, cf_name, yt_dl_user_name, yt_dl_pass_word = await extract_link(
        message.reply_to_message, "YTDL"
    )
    LOGGER.info(dl_url)
    LOGGER.info(cf_name)
    if dl_url is not None:
        await i_m_sefg.edit_text("`Extracting/Parsing Links...`")
        current_user_id = message.from_user.id
        # create an unique directory
        user_working_dir = os.path.join(DOWNLOAD_LOC, str(current_user_id))
        # create download directory, if not exist
        if not os.path.isdir(user_working_dir):
            os.makedirs(user_working_dir)
        # list the formats, and display in button markup formats
        thumb_image, text_message, reply_markup = await extract_youtube_dl_formats(
            dl_url,
            # cf_name,
            yt_dl_user_name,
            yt_dl_pass_word,
            user_working_dir
        )
        if thumb_image is not None:
            thumb_image = await proc_ess_image_aqon(
                thumb_image,
                user_working_dir
            )
            await message.reply_photo(
                photo=thumb_image,
                quote=True,
                caption=text_message,
                reply_markup=reply_markup
            )
            await i_m_sefg.delete()
        else:
            await i_m_sefg.edit_text(
                text=text_message,
                reply_markup=reply_markup
            )
    else:
        await i_m_sefg.edit_text(
            "**WtF**! This Incorrect Way To Use the bot.\nPlease Read Pinned Messages or Check /help.\n\n"
            f"<b>API Error</b>: {cf_name}"
        )
        
#playlist
async def ytdl_list(client, message):
    """ /pytdl command """
    #i_m_sefg = await message.reply_text("Processing...you should wait🤗", quote=True)
    usr_id = message.from_user.id
    if 'youtube.com/playlist' in message.reply_to_message.text:
        i_m_sefg = await message.reply_text("`Downloading... You should Wait 🤗`", quote=True)
        await yt_playlist_downg(message.reply_to_message, i_m_sefg)