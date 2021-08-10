import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)

import time
import asyncio
import json
import math
import os
import shutil
import time
from datetime import datetime

from apdbot import (
    DOWNLOAD_LOC,
    AUTH,
    CUSTOM_NAME
)

from apdbot.helpers.upload_to_tg import upload_to_tg

async def mdp_callback(bot, update):
    #LOGGER.info(update)
    cb_data = update.data
    # youtube_dl extractors
    tg_send_type, mdp_format, cf_name = cb_data.split("!")
    #
    current_user_id = update.message.reply_to_message.from_user.id
    #
    user_working_dir = os.path.join(DOWNLOAD_LOC, str(current_user_id))
    # create download directory, if not exist
    if not os.path.isdir(user_working_dir):
        await bot.delete_messages(
            chat_id=update.message.chat.id,
            message_ids=[
                update.message.message_id,
                update.message.reply_to_message.message_id,
            ],
            revoke=True
        )
        return
    save_ytdl_json_path = user_working_dir + \
        "/" + str("ytdleech") + ".json"
    try:
        with open(save_ytdl_json_path, "r", encoding="utf8") as f:
            md_url = json.load(f)
        os.remove(save_ytdl_json_path)
    except (FileNotFoundError) as e:
        await bot.delete_messages(
            chat_id=update.message.chat.id,
            message_ids=[
                update.message.message_id,
                update.message.reply_to_message.message_id,
            ],
            revoke=True
        )
        return False
    #
    
    custom_file_name = cf_name + "." + mdp_format + ".WEB-DL.-APD-" + ".mkv"
    # https://superuser.com/a/994060
    LOGGER.info(custom_file_name)
    #
    await update.message.edit_caption(
        caption="`Trying to Download...`"
    )
    description = "@APDLeechBox"
    tmp_directory_for_each_user = os.path.join(
        DOWNLOAD_LOC,
        str(update.message.message_id)
    )
    if not os.path.isdir(tmp_directory_for_each_user):
        os.makedirs(tmp_directory_for_each_user)
    download_directory = tmp_directory_for_each_user
    download_directory = os.path.join(tmp_directory_for_each_user, custom_file_name)
    command_to_exec = [
            "streamlink",
            md_url, mdp_format,
            "--hls-segment-threads",
            "10",
            "-o", download_directory
            ]
    LOGGER.info(command_to_exec)
    start = datetime.now()
    process = await asyncio.create_subprocess_exec(
        *command_to_exec,
        # stdout must a pipe to be accessible as process.stdout
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    # LOGGER.info(e_response)
    # LOGGER.info(t_response)
    ad_string_to_replace = "please report this issue on https://yt-dl.org/bug . Make sure you are using the latest version; see  https://yt-dl.org/update  on how to update. Be sure to call youtube-dl with the --verbose flag and include its complete output."
    if e_response and ad_string_to_replace in e_response:
        error_message = e_response.replace(ad_string_to_replace, "")
        await update.message.edit_caption(
            caption=error_message
        )
        return False, None
    if t_response:
        LOGGER.info(t_response)
        # os.remove(save_ytdl_json_path)
        end_one = datetime.now()
        time_taken_for_download = (end_one-start).seconds
        dir_contents = os.listdir(tmp_directory_for_each_user)
        dir_contents.sort()
        download_directory = ""
        if len(dir_contents) >= 1:
            download_directory = os.path.join(tmp_directory_for_each_user, dir_contents[0])
        else:
            await bot.edit_message_text(
                chat_id=update.message.chat.id,
                message_id=update.message.message_id,
                text=t_response + "\n" + e_response
            )
            return False, None
        await update.message.edit_caption(
            caption=f"found {dir_contents} files"
        )
        user_id = update.from_user.id
        #
        LOGGER.info(download_directory)
        final_response = await upload_to_tg(
            update.message,
            download_directory,
            user_id,
            {},
            True
        )
        LOGGER.info(download_directory)
        LOGGER.info(final_response)
        #
        try:
            shutil.rmtree(tmp_directory_for_each_user)
        except:
            pass
        #
        message_to_send = ""
        for key_f_res_se in final_response:
            local_file_name = key_f_res_se
            message_id = final_response[key_f_res_se]
            channel_id = str(update.message.chat.id)[4:]
            private_link = f"https://t.me/c/{channel_id}/{message_id}"
            message_to_send += "📍 <a href='"
            message_to_send += private_link
            message_to_send += "'>"
            message_to_send += local_file_name
            message_to_send += "</a>"
            message_to_send += "\n"
        if message_to_send != "":
            mention_req_user = f"<a href='tg://user?id={user_id}'>Your Requested Files</a>\n\n"
            message_to_send = mention_req_user + message_to_send
            message_to_send = message_to_send + "\n" + "🏅<b>POWERED BY : @APDLEECHBOX</b>\n#UPLOADED"
        else:
            message_to_send = "<i>FAILED</i> To Leech Files."
        await update.message.reply_to_message.reply_text(
            text=message_to_send,
            quote=True,
            disable_web_page_preview=True
            )
