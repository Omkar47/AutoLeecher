import os

from apdbot import DOWNLOAD_LOC

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
#from PIL import Image


async def save_thumb(client, message):
    thumbnail_location = os.path.join(
        DOWNLOAD_LOC,
        "thumbnails"
    )
    thumb_image_path = os.path.join(
        thumbnail_location,
        str(message.from_user.id) + ".jpg"
    )
    ismgs = await message.reply_text("`Processing...`")
    if message.reply_to_message is not None:
        if not os.path.isdir(thumbnail_location):
            os.makedirs(thumbnail_location)
        download_location = thumbnail_location + "/"
        downloaded_file_name = await client.download_media(
            message=message.reply_to_message,
            file_name=download_location
        )
        # https://stackoverflow.com/a/21669827/4723940
        Image.open(downloaded_file_name).convert("RGB").save(downloaded_file_name)
        metadata = extractMetadata(createParser(downloaded_file_name))
        height = 0
        if metadata.has("height"):
            height = metadata.get("height")
        # resize image
        # ref: https://t.me/PyrogramChat/44663
        img = Image.open(downloaded_file_name)
        # https://stackoverflow.com/a/37631799/4723940
        # img.thumbnail((320, 320))
        img.resize((320, height))
        img.save(thumb_image_path, "JPEG")
        # https://pillow.readthedocs.io/en/3.1.x/reference/Image.html#create-thumbnails
        os.remove(downloaded_file_name)
        await ismgs.edit(
            "Custom video / file thumbnail saved. " + \
            "This image will be used in the upload, till /clear."
        )
    else:
        await message.edit("Reply to a photo to save custom thumbnail")


async def clear_thumb(client, message):
    thumbnail_location = os.path.join(
        DOWNLOAD_LOC,
        "thumbnails"
    )
    thumb_image_path = os.path.join(
        thumbnail_location,
        str(message.from_user.id) + ".jpg"
    )
    ismgs = await message.reply_text("`Processing...`")
    if os.path.exists(thumb_image_path):
        os.remove(thumb_image_path)
    await ismgs.edit("✅ `Custom thumbnail cleared Succesfully.`")
