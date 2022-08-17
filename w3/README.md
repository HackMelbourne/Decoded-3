<h1 align="center">[Participant's Workbook] Building a Music Bot</h1>

> Related Pages: [DecodED 3](./README.md)

---

<h2>Table of Contents</h2>
<details>
<summary>Table of Contents</summary>

- [0. Downloading ffmpeg](#0-create-a-discord-account-and-discord-server)
    - [For Windows](#create-a-discord-account)
    - [For Mac](#create-a-discord-server)
- [1. Installing Modules: `youtube_dl`](#1-create-an-application)
- [2. Setting up the join and leave commands](#2-installing-modules-discordpy-and-python-dotenv)
- [3. Streaming audio to discord](#3-creating-a-bot-and-adding-it-to-your-server)
- [4. Pausing and playing audio](#4-make-the-bot-say-hello-world)
- [5. Sending the Youtube Thumbnail](#5-adding-commands)

</details>

---

## 0. Downloading ffmpeg

<details>
<summary><b>❓ What is Lavalink?</b></summary>
Lavalink is a library that allows you to play music on discord using the [Lavalink]() library.


</details>

* We need to download ffmpeg first so that we can stream music.

### For Windows

Simply click on this link and ffmpeg will start
downloading (https://www.gyan.dev/ffmpeg/builds/packages/ffmpeg-2022-07-24-git-39a538f430-full_build.7z)

### For Mac

Simply click on this link and ffmpeg will start downloading (https://evermeet.cx/ffmpeg/ffmpeg-107536-g8daa0fea9f.zip)

## 1. Un-ziping and copying the ffmpeg.exe path

Un-zip the ffmpeg and than open the folder, open bin, from there copy the path of ffmpeg.exe which we will use while
adding ffmpeg.

## 1. Installing Modules: 'youtube_dl'

* Before we begin creating the bot, we have to install a few modules
* Install `youtube_dl`
    * youtube_dl is an open source download manager for youtube video and it will help us play our youtube videos audio
      in real time.
    * to install it, type this into your terminal:
      ```
      pip install youtube_dl
      ```
    * now you need to add some youtube_dl option in your code
      ```python
      # youtube best audio options
      yt_dl_opts = {'formats': 'beastaudio/best'}
      ytdl = youtube_dl.YoutubeDL(yt_dl_opts)
      ```

## 2. Setting up the join and leave commands

* We first need to set up a COG to put all of our code in:

```python
class MusicBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

```

Our bot needs commands to join and leave the current audio server the user is on.
To do this, you can use the on_event functions:

* We now need to make sure that when ever we run the code, we can see that our bot has successfully logged-in. For that
  we need to write a function on_ready.
  ```python
  # Start the bot
    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

  ```

