<h1 align="center">[Participant's Workbook] Building a Music Bot</h1>

> Related Pages: [DecodED 3](./README.md)

---

<h2>Table of Contents</h2>
<details>
<summary>Table of Contents</summary>

- [0. what is Lavalink](#0-create-a-discord-account-and-discord-server)
    - [For Windows](#create-a-discord-account)
    - [For Mac](#create-a-discord-server)
- [1. Installing Modules: `youtube_dl`](#1-create-an-application)
- [2. Setting up the join and leave commands](#2-installing-modules-discordpy-and-python-dotenv)
- [3. Streaming audio to discord](#3-creating-a-bot-and-adding-it-to-your-server)
- [4. Pausing and playing audio](#4-make-the-bot-say-hello-world)
- [5. Sending the Youtube Thumbnail](#5-adding-commands)

</details>

---

## 0. What is Lavalink and setting it up

<details>
<summary><b>❓ What is Wavelink and Lavalink?</b></summary>

Wavelink is a library that allows you to play music with discord.py using
the [Lavalink](https://github.com/freyacodes/Lavalink) library.

Lavalink is a server application which allows you to search and stream audio directly between a source and a destination
without too much overhead!

</details>

## 1. Installing Modules

* Before we begin creating the bot, we have to install a few modules

* Install wavelink
    * Just simply type this in your terminal
  ```
  pip install wavelink
  ```

We're hoping you already have a basic hello bot set up from the first workshop!

* Now we need to start the bot by adding some import statement in our code.

```python
import os
import subprocess
import time

import discord
import requests
import wavelink
from discord.ext import commands
```

## 2. Setting up the join and leave commands

* We first need to set up a COG to put all of our code in:

```python
class MusicBot(commands.Cog):
    voice_clients = {}

    def __init__(self, client):
        self.client = client
```

You may notice an extra `voice_clients` dictionary. This is where we will store all the active song sessions we're
playing 🎵

* The first step for a music bot is being able to join the current voice channel. Let's make a command called `join`
  that does just that:

```python
@commands.command()
async def join(self, ctx: commands.Context):
    # Leave current channel
    if ctx.voice_client is not None:
        await ctx.voice_client.disconnect()
    if not ctx.message.author.voice:
        await ctx.send('You are not in a voice channel')
        return
    channel = ctx.message.author.voice.channel
    self.voice_clients[ctx.guild.id] = await channel.connect(cls=wavelink.Player())
    await ctx.send(f'Joined {channel}')
```

Let's break this down.
The code does the following:

1. First we check if we're currently connected to a voice channel. If we are, we gotta leave
2. We then check if the author of the message is in a voice channel. If they aren't, we send a reminder to join and stop
   there
3. If all is good, we grab the channel they're in and join the party 🥳. It's important that we set wavelink as our audio
   source here, as that's where our music is coming from.
    1. Take note of how we store the audio client in the `voice_clients` dictionary. This will be important later.
4. Finally, we text the user that we joined.

* We also need to make sure that users can ask our bot to leave. We can do this with the following:

```python
@commands.command()
async def leave(self, ctx):
    if ctx.guild.id in self.voice_clients:
        await self.voice_clients[ctx.guild.id].stop()
        del self.voice_clients[ctx.guild.id]
        await ctx.send('Left')
    if ctx.voice_client is not None:
        await ctx.voice_client.disconnect()
```

Let's break this down:

1. Let's check if we're in the voice channel to begin with in this guild. If we are, let's stop our player and delete
   our voice client.
2. We can then disconnect and send a message saying that we left ;-;

## 3. Pausing and playing Music

Let's get to the fun part. Playing (and pausing) music!

```python
# To play the music  
@commands.command()
async def play(self, ctx, *, search: wavelink.YouTubeTrack):
    if ctx.guild.id not in self.voice_clients:
        # Join the user's voice channel
        await self.join(ctx)
    if ctx.guild.id not in self.voice_clients:
        return
    voice = self.voice_clients[ctx.guild.id]
    await voice.play(search)
    embed = discord.Embed(
        title=voice.source.title,
        url=voice.source.uri,
        author=ctx.author,
        description=f"Playing {voice.source.title} in {voice.channel}"

    )
    embed.set_image(url=voice.source.thumbnail)
    await ctx.send(embed=embed)


# To stop the music
@commands.command()
async def stop(self, ctx):
    if ctx.guild.id in self.voice_clients:
        await self.voice_clients[ctx.guild.id].stop()
        await ctx.send('Stopped')
    else:
        await ctx.send('Not in a voice channel')


# To pause the music
@commands.command()
async def pause(self, ctx):
    if ctx.guild.id in self.voice_clients:
        await self.voice_clients[ctx.guild.id].pause()
        await ctx.send('Paused')
    else:
        await ctx.send('Not in a voice channel')


# To resume the music
@commands.command()
async def resume(self, ctx):
    if ctx.guild.id in self.voice_clients:
        await self.voice_clients[ctx.guild.id].resume()
        await ctx.send('Resumed')
    else:
        await ctx.send('Not in a voice channel')

```

Now when ever you will add '!paused' in discord it will pause the music and when you will add '!resumed' it will resume
the song again.

## 4. Starting the bot

* Now comes the fun part where we make the bot.

```python

# Start the bot
@commands.Cog.listener()
async def on_ready(self):
    print('Logged in as')
    print(self.client.user.name)
    print(self.client.user.id)
    print('------')
    # Try start Lavafront server
    subprocess.Popen(["java", "-jar", "Lavalink.jar"])
    # wait for port to open
    while True:
        try:
            r = requests.get('http://localhost:2333')
            break
        except requests.exceptions.ConnectionError:
            print("Waiting for lavalink to go live...")
            time.sleep(1)
            continue

    async def connect_wavefront():
        await self.client.wait_until_ready()
        await wavelink.NodePool.create_node(
            bot=self.client,
            host='localhost',
            port=2333,
            password='youshallnotpass'
        )

    self.client.loop.create_task(connect_wavefront())


@commands.Cog.listener()
async def on_wavelink_node_ready(self, node: wavelink.Node):
    print(f'Connected to wavefront! ID: {node.identifier}')

```

## 5. Adding token

* We are almost there, we just need to add the token of the bot before we start playing our favourite songs.

```python
def setup(bot):
    bot.add_cog(MusicBot(bot))


if __name__ == '__main__':
    load_dotenv()
    TOKEN = os.getenv('TOKEN')

    client = commands.Bot(command_prefix='!')
    client.add_cog(MusicBot(client))
    client.run(TOKEN)

```
