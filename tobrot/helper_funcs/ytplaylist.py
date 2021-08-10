import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)
 
 
import os
import shutil
import asyncio
import subprocess
import requests
from apdbot.helpers.upload_to_tg import upload_to_tg
from apdbot import (
    DOWNLOAD_LOC
)
 
 
async def yt_playlist_downg(message, i_m_sefg):
    url = message.text
    usr = message.message_id
    user = message.from_user.id
    messa_ge = i_m_sefg.reply_to_message
    fol_der = f"{usr}youtube"
    print(url)
    print(usr)
    print(messa_ge)
    print(fol_der)
    try:
        os.mkdir(fol_der)
    except:
        pass
    cmd = ["yt-dlp", "-i", "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4", "-o", f"{fol_der}/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s", f"{url}"]
    gau_tam = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    gau, tam = await gau_tam.communicate()
    LOGGER.info(gau.decode('utf-8'))
    LOGGER.info(tam.decode('utf-8'))
    e_response = tam.decode().strip()
    ad_string_to_replace = "please report this issue on https://yt-dl.org/bug . Make sure you are using the latest version; see  https://yt-dl.org/update  on how to update. Be sure to call youtube-dl with the --verbose flag and include its complete output."
    if e_response and ad_string_to_replace in e_response:
        error_message = e_response.replace(ad_string_to_replace, "")
        await i_m_sefg.edit_text(
            error_message
        )
        return False, None
    else:
        final_response = await upload_to_tg(i_m_sefg, fol_der, usr, {})
        print(final_response)
    try:
        shutil.rmtree(fol_der)
    except:
        pass
    message_to_send = ""
    for key_f_res_se in final_response:
        local_file_name = key_f_res_se
        l_f_name = local_file_name.replace("_", " ")
        message_id = final_response[key_f_res_se]
        channel_id = str(message.chat.id)[4:]
        private_link = f"https://t.me/c/{channel_id}/{message_id}"
        message_to_send += "📍 <a href='"
        message_to_send += private_link
        message_to_send += "'>"
        message_to_send += l_f_name
        message_to_send += "</a>"
        message_to_send += "\n"
    if message_to_send != "":
        mention_req_user = f"<a href='tg://user?id={user}'>Your Requested Files</a>\n\n"
        message_to_send = mention_req_user + message_to_send
        message_to_send = message_to_send + "\n" + "🏅<b>POWERED BY : @APDLEECHBOX</b> #UPLOADED"
        LOGGER.info(message_to_send)
    else:
            message_to_send = "<i>FAILED</i> to Upload Files. 😞😞"
    await message.reply_text(
        text=message_to_send,
        quote=True,
        disable_web_page_preview=True
    )
