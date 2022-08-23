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
<summary><b>❓ What is Lavalink?</b></summary>
Lavalink is a library that allows you to play music on discord using the [Lavalink]() library.

## 1. Installing Modules

* Before we begin creating the bot, we have to install a few modules

* Install discord and dotenv
  * Just simply type this in your terminal
  ```
  pip install discord 
  ```
  ```
  pip install dotenv
  ```

* Now we need to start the bot by adding some import statement in our code. 
```python
import os
import subprocess
import time
import discord
import requests
import wavelink
from discord.ext import commands
from dotenv import load_dotenv
```

## 2. Setting up the join and leave commands

* We first need to set up a COG to put all of our code in:

```python
class MusicBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

```

* We now need to make sure that when ever we run the code, we can see that our bot has successfully logged-in and also let us know if we didn't join the voice channel. For that
  we can simply use this code.
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

* We also need to make sure that our bot leave. So for that we can simple use this code.
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

## 3. Pausing and playing Music
* Now we need our bot to pause and play the music. We can do that simply by using this code.
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
Now when ever you will add '!paused' in discord it will pause the music and when you will add '!resumed' it will resume the song again. 


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
