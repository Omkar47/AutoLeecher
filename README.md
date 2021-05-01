# Telegram Torrent Leecher 🔥🤖

```I HAVEN'T TESTED THIS REPO JUST RANDOML EDITED THIS 

SO BUGGES ARE CONFIRM THERE MAYBE NOT REPO NOT EVEN GONNA WORK ANY MORE :[

DO LET ME KNOW IF ANY BUGS AT PULL REQUESTS OR CONTACT ME AT @APDBUGS
```

A Telegram Torrent (and youtube-dl) Leecher based on [Pyrogram](https://github.com/pyrogram/pyrogram)

## installing

### The Easy Way

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


### The Eas(iest) Way

- Install Docker by following the [official docker docs](https://docs.docker.com/engine/install/debian/)

- Start docker daemon [skip if already running]:
```sh
dockerd
```
- Build Docker image:
```sh
docker build . -t public-leech
```
- Run the image:
```sh
docker run public-leech
```

It is not recommended to use "sudo", un-necessarily, in a GNU/Linux system.
GNU/Linux Permissions are highly customisable, and it is generally not required to have "ROOT" permission, ~~unless you know what you are doing~~.
You can still install all the dependencies in your system [with ROOT permissions], but please be aware of the potential issues when doing so. The installed packages may conflict with the system package manager's installed packages, which can cause trouble down the road and errors when upgrading conflicting packages.
**You have been warned.**



### The Legacy Way
Simply clone the repository and run the main file:

```sh
git clone https://github.com/SpEcHiDe/PublicLeech.git
cd PublicLeech
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create config.py appropriately>
python3 -m tobrot
```

### an example config.py 👇
```py
from tobrot.sample_config import Config

class Config(Config):
  TG_BOT_TOKEN = ""
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
  AUTH_CHANNEL = -1001234567890
```

### Variable Explanations

##### Mandatory Variables

* `TG_BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.

* `APP_ID`
* `API_HASH`: Get these two values from [my.telegram.org/apps](https://my.telegram.org/apps).
  * N.B.: if Telegram is blocked by your ISP, try our [Telegram bot](https://telegram.dog/UseTGXBot) to get the IDs.

* `AUTH_CHANNEL`: Create a Super Group in Telegram, add `@GoogleIMGBot` to the group, and send /id in the chat, to get this value.

##### Optional Configuration Variables

* `DOWNLOAD_LOCATION`

* `MAX_FILE_SIZE`

* `TG_MAX_FILE_SIZE`

* `FREE_USER_MAX_FILE_SIZE`

* `MAX_TG_SPLIT_FILE_SIZE`

* `CHUNK_SIZE`

* `MAX_MESSAGE_LENGTH`

* `PROCESS_MAX_TIMEOUT`

* `ARIA_TWO_STARTED_PORT`

* `EDIT_SLEEP_TIME_OUT`

* `MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START`

## Variables to Edit Commands

* `LEECH_CMD`

* `YTDL_CMD`

* `CANCEL_CMD`

* `STATUS_CMD`

* `LOG_CMD`

* `SAVE_CMD`

* `DELETE_CMD`

* `UPLOAD_CMD`

* `EXEC_CMD `

* `HELP_CMD`

## Available Commands

* `/ytdl`: This command should be used as reply to a [supported link](https://ytdl-org.github.io/youtube-dl/supportedsites.html)

* `/leech`: This command should be used as reply to a magnetic link, a torrent link, or a direct link. [this command will SPAM the chat and send the downloads a seperate files, if there is more than one file, in the specified torrent]

* `/leech archive`: This command should be used as reply to a magnetic link, a torrent link, or a direct link. [This command will create a .tar.gz file of the output directory, and send the files in the chat, splited into PARTS of 1024MiB each, due to Telegram limitations]


## How to Use?

* send any one of the available command, as a reply to a valid link.

* if file is larger than 2000MB, [read this](https://t.me/c/1434259219/113).

* if file is a TAR archive, [read this](https://t.me/c/1434259219/104) to know how to uncompress.


## Issues or Feature Requests

* search for known issues, [here](https://t.me/c/1434259219/118).

* add issues / feature requests, [here](https://github.com/SpEcHiDe/PublicLeech/issues/new).


## Credits, and Thanks to
* [me](https://telegram.dog/APDBUGS)
* [SPECHIDE](https://github.com/SpEcHIDe/PublicLeech)
* [Dan Tès](https://telegram.dog/haskell) for his [Pyrogram Library](https://github.com/pyrogram/pyrogram)
* [Robots](https://telegram.dog/Robots) for their [@UploadBot](https://telegram.dog/UploadBot)
* [@AjeeshNair](https://telegram.dog/AjeeshNait) for his [torrent.ajee.sh](https://torrent.ajee.sh)
* [@gotstc](https://telegram.dog/gotstc), @aryanvikash, [@HasibulKabir](https://telegram.dog/HasibulKabir) for their TORRENT groups
* [![CopyLeft](https://telegra.ph/file/b514ed14d994557a724cb.jpg)](https://telegra.ph/file/fab1017e21c42a5c1e613.mp4 "CopyLeft Credit Video")
