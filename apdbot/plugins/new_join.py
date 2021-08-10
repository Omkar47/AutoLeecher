import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)
 
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)
 
from apdbot import (
    AUTH
)
 
 
async def help_msg(client, message):
    await message.reply_text("<b>Read Pinned Message For More help & to Avoid Ban</b>\n\n/help : To See This message" \
    "\n\n<code>/leech@AlPacinov2bot</code> : To Leech URI" \
    "\n\n<code>/ytdl@AlPacinov2bot</code> : To Download ytdl Supported Sites" \
    "\n\n<code>/pytdl@AlPacinov2bot</code> : Download Playlist From YouTube" \
    "\n\n<code>/save@AlPacinov2bot</code> : To Save Thumbnail" \
    "\n\n<code>/clear@AlPacinov2bot</code> : To Clear Thumbnail" \
    "\n\n<code>/leech@AlPacinov2bot archive</code> : To Tar Files" \
    "\n\n<code>/leech@AlPacinov2bot unzip</code> : To Unzip/Untar/Unrar Files", quote=True)