import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import asyncio
import os
import time
import sys
import traceback
import shutil
import io
import psutil

from apdbot import (
    MAX_MSG_LENGTH,
    AUTH,
    BOT_TIME,
    LOGGER
)


from apdbot.helpers.admin_check import AdminCheck
from apdbot.helpers.download_aria import call_apropriate_function, aria_start
from apdbot.helpers.upload_to_tg import upload_to_tg

from apdbot.helpers.display_progress import (
    TimeFormatterr,
    humanbytes
)

async def status_msg(client, message):
    aria_i_p = await aria_start()
    # Show All Downloads
    downloads = aria_i_p.get_downloads()
    #
    DOWNLOAD_ICON = "🔻"
    UPLOAD_ICON = "🔺"
    #
    msg = ""
    for download in downloads:
        downloading_dir_name = "NA"
        try:
            downloading_dir_name = str(download.name)
        except:
            pass
        if download.status == 'active':
            total_length_size = str(download.total_length_string())
            progress_percent_string = str(download.progress_string())
            down_speed_string = str(download.download_speed_string())
            up_speed_string = str(download.upload_speed_string())
            download_current_status = str(download.status)
            e_t_a = str(download.eta_string())
            current_gid = str(download.gid)
            #
            msg += f"<b>File Name</b> : <u>{downloading_dir_name}</u>"
            msg += "\n"
            msg += f"<b>Total Size</b> : {total_length_size}"
            msg += " | "
            msg += f"<b>Progress</b> : {progress_percent_string}"
            msg += "\n"
            msg += f"<b>Speed</b> : {down_speed_string} {DOWNLOAD_ICON}"
            msg += " / "
            msg += f"{up_speed_string} {UPLOAD_ICON}"
            msg += "\n"
            msg += f"<b>ETA</b> : {e_t_a}"
            msg += "\n"
            msg += f"<b>Status</b> : {download_current_status}"
            msg += "\n"
            msg += f"<b>Cancel CMD</b> : <code>/cancel {current_gid}</code>"
            msg += "\n"
            msg += "\n\n"
        #LOGGER.info(msg)
 
    if msg == "":
        msg = "🤷‍♂️ No Active Torrents 🤷"
 
    currentTime = TimeFormatterr((time.time() - BOT_TIME))
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    sent = humanbytes(psutil.net_io_counters().bytes_sent)
    recv = humanbytes(psutil.net_io_counters().bytes_recv)
 
    ms_g = f"<b>Bot Uptime</b> : <code>{currentTime}</code>\n" \
        f"<b>Total disk space</b> : <code>{total}</code>\n" \
        f"<b>Used</b> : <code>{used}</code>\n" \
        f"<b>Free</b> : <code>{free}</code>\n" \
        f"<b>Total Downloaded Data</b> : <code>{recv}</code>\n"
    #LOGGER.info(ms_g)
 
    msg = ms_g + "\n" + msg
    LOGGER.info(msg)
    if len(msg) > MAX_MSG_LENGTH:
        with io.BytesIO(str.encode(msg)) as out_file:
            out_file.name = "status.text"
            await client.send_document(
                chat_id=message.chat.id,
                document=out_file,
            )
    else:
        await message.reply_text(msg, quote=True)


async def cancel_msg(client, message):
    if len(message.command) > 1:
        # /cancel command
        i_m_s_e_g = await message.reply_text("`Processing....`", quote=True)
        aria_i_p = await aria_start()
        g_id = message.command[1].strip()
        LOGGER.info(g_id)
        try:
            downloads = aria_i_p.get_download(g_id)
            file_name = downloads.name
            LOGGER.info(downloads)
            LOGGER.info(downloads.remove(force=True, files=True))
            if os.path.exists(file_name):
                if os.path.isdir(file_name):
                    shutil.rmtree(file_name)
                else:
                    os.remove(file_name)
            await i_m_s_e_g.edit_text(f"Leech Cancelled by <a href='tg://user?id={update.from_user.id}'>{update.from_user.first_name}</a>")
        except Exception as e:
            await i_m_s_e_g.edit_text("<i>FAILED</i>\n\n" + str(e) + "\n#error")
        else:
            await update.message.delete()


async def exec_msg(client, message):
    if message.from_user.id in AUTH:
        DELAY_BETWEEN_EDITS = 0.3
        PROCESS_RUN_TIME = 100
        cmd = message.text.split(" ", maxsplit=1)[1]

        reply_to_id = message.message_id
        if message.reply_to_message:
            reply_to_id = message.reply_to_message.message_id

        start_time = time.time() + PROCESS_RUN_TIME
        process = await asyncio.create_subprocess_shell(
            cmd,
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
        OUTPUT = f"**QUERY:**\n__Command:__\n`{cmd}` \n__PID:__\n`{process.pid}`\n\n**stderr:** \n`{e}`\n**Output:**\n{o}"

        if len(OUTPUT) > MAX_MSG_LENGTH:
            with open("exec.text", "w+", encoding="utf8") as out_file:
                out_file.write(str(OUTPUT))
            await client.send_document(
                chat_id=message.chat.id,
                document="exec.text",
                caption=cmd,
                disable_notification=True,
                reply_to_message_id=reply_to_id
            )
            os.remove("exec.text")
            await message.delete()
        else:
            await message.reply_text(OUTPUT)


async def upload_doc(client, message):
    imsegd = await message.reply_text(
        "`Processing Request...`"
    )
    if message.from_user.id in AUTH:
        if " " in message.text:
            recvd_command, local_file_name = message.text.split(" ", 1)
            recvd_response = await upload_to_tg(
                imsegd,
                local_file_name,
                message.from_user.id,
                {}
            )
            LOGGER.info(recvd_response)
    await imsegd.delete()
    
    
async def upload_log_file(client, message):
    await message.reply_document(
        "log.log"
    )


async def stats_msg(client, message):
    msg = ""
    currentTime = TimeFormatterr((time.time() - BOT_TIME))
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    sent = humanbytes(psutil.net_io_counters().bytes_sent)
    recv = humanbytes(psutil.net_io_counters().bytes_recv)
 
    ms_g = f"<b>Bot Uptime</b> : <code>{currentTime}</code>\n" \
        f"<b>Total disk space</b> : <code>{total}</code>\n" \
        f"<b>Used</b> : <code>{used}</code>\n" \
        f"<b>Free</b> : <code>{free}</code>\n" \
        f"<b>Total Downloaded Data</b> : <code>{recv}</code>\n" \
        f"<b>Total Uploaded Data</b> : <code>{sent}</code>\n"
    #LOGGER.info(ms_g)
    await message.reply_text(ms_g, quote=True)
    