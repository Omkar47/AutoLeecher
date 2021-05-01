#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import pyrogram


from tobrot import (
    AUTH_CHANNEL,
    CANCEL_CMD,
    LEECH_CMD,
    YTDL_CMD,
    STATUS_CMD,
    STATS_CMD,
    LOG_CMD,
    SAVE_CMD,
    DELETE_CMD,
    HELP_CMD,
    UPLOAD_CMD,
    EXEC_CMD
)


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(f"Current CHAT ID: <code>{message.chat.id}</code>\n\nYou Can Try Checking @APDLeechBoX")
        # leave chat
        await client.leave_chat(
            chat_id=message.chat.id,
            delete=True
        )
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_msg(client, message):
    await message.reply_text("<b>Read Pinned Message For More help & to Avoid Ban</b>\n\n/help : To See This message" \
    f"\n\n<code>/{LEECH_CMD}</code> : To Leech URI" \
    f"\n\n<code>/{YTDL_CMD}</code> : To Download ytdl Supported Sites" \
    f"\n\n<code>/{SAVE_CMD}</code> : To Save Thumbnail" \
    f"\n\n<code>/{DELETE_CMD}</code> : To Clear Thumbnail" \
    f"\n\n<code>/{LEECH_CMD} archive</code> : To Tar Files" \
    f"\n\n<code>/{LEECH_CMD} unzip</code> : To Unzip/Untar/Unrar Files", quote=True)


async def rename_message_f(client, message):
    inline_keyboard = []
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            text="DONT CLICK HERE",
            url="https://t.me/APDBugs"
        )
    ])
    reply_markup = pyrogram.InlineKeyboardMarkup(inline_keyboard)
    await message.reply_text(
        "I AIN\'T GONNA RENAME YOUR SHIT...",
        quote=True,
        reply_markup=reply_markup
    )
