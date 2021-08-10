import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import aiohttp

from pyrogram.types import MessageEntity
import requests
from apdbot.plugins.headers import headers
import apdbot.plugins.urls
import os

from apdbot import (
    TG_OFFENSIVE_API
)

token_url1 = "https://useraction.zee5.com/tokennd"
search_api_endpoint = "https://gwapi.zee5.com/content/details/"
platform_token = "https://useraction.zee5.com/token/platform_tokens.php?platform_name=web_app"
token_url2 = "https://useraction.zee5.com/token"
stream_baseurl = "https://zee5vodnd.akamaized.net"

async def zee5(message):
    LOGGER.info(message)
    link = message.text.split('/')[-1]
    LOGGER.info(link)
    w = link
    req1 = requests.get(token_url1, headers=headers).json()
    req2 = requests.get(platform_token).json()["token"]
    headers["X-Access-Token"] = req2
    req3 = requests.get(token_url2, headers=headers).json()       
    r1 = requests.get(search_api_endpoint + w,headers=headers, params={"translation":"en", "country":"IN"}).json()
    g1 = (r1["hls"][0].replace("drm", "hls") + req1["video_token"])
    finalurl = stream_baseurl+g1
    title = r1["title"]
    img_url = r1["image_url"]
    LOGGER.info(finalurl)
    return finalurl, title, img_url