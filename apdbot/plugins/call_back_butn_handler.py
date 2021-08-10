import logging
import os
import shutil

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)

from pyrogram.types import CallbackQuery
from apdbot.helpers.admin_check import AdminCheck
from apdbot.helpers.download_aria import aria_start
from apdbot.helpers.ytdl_button import ytdl_callback
from apdbot.plugins.status_msg import cancel_msg

async def button(bot, update: CallbackQuery):
    cb_data = update.data
    try:
        g = await AdminCheck(bot, update.message.chat.id, update.from_user.id)
        print(g)
    except:
        pass
    if "|" in cb_data:
        await ytdl_callback(bot, update)
    LOGGER.info(cb_data)
    if cb_data.startswith("cancel"):
        if len(cb_data) > 1:
            i_m_s_e_g = await update.message.reply_text("`Checking..?`", quote=True)
            aria_i_p = await aria_start()
            g_id = cb_data.split()[-1]
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
                await i_m_s_e_g.edit_text(f"`Leech Cancelled by` <a href='tg://user?id={update.from_user.id}'>{update.from_user.first_name}</a>")
            except Exception as e:
                await i_m_s_e_g.edit_text("<i>FAILED</i>\n\n" + str(e) + "\n#error")
            else:
                await update.message.delete()
