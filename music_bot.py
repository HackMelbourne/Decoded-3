import os

import discord
import youtube_dl
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix='?')

# music bot 
voice_clients = {}

# youtube best audio options
yt_dl_opts = {'formats': 'beastaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

# option for only audio and no video
ffmpeg_options = {'options': '-vn'}


class MusicBot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        global voice_clients
        channel = ctx.message.author.voice.channel
        voice_clients[ctx.guild.id] = await channel.connect()
        await ctx.send(f'Joined {channel}')

    @commands.command()
    async def leave(self, ctx):
        global voice_clients
        if ctx.guild.id in voice_clients:
            voice_clients[ctx.guild.id].stop()
            del voice_clients[ctx.guild.id]
            await ctx.send('Left')

    @commands.command()
    async def play(self, ctx, url):
        global voice_clients
        if ctx.guild.id not in voice_clients:
            # Join the user's voice channel
            await self.join(ctx)
        # Play the YouTube video audio
        with youtube_dl.YoutubeDL(yt_dl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
        # Send the song to the voice channel
        song = info_dict['formats'][0]['url']
        voice_clients[ctx.guild.id].play(
            discord.FFmpegPCMAudio(song, **ffmpeg_options, executable="C:\\ffmpeg\\ffmpeg.exe")
        )
        await ctx.send(f'Now playing {info_dict["title"]}')
        await ctx.send(info_dict["thumbnails"][0]['url'])

    @commands.command()
    async def stop(self, ctx):
        global voice_clients
        if ctx.guild.id in voice_clients:
            voice_clients[ctx.guild.id].stop()
            await ctx.send('Stopped')
        else:
            await ctx.send('Not in a voice channel')

    @commands.command()
    async def pause(self, ctx):
        global voice_clients
        if ctx.guild.id in voice_clients:
            voice_clients[ctx.guild.id].pause()
            await ctx.send('Paused')
        else:
            await ctx.send('Not in a voice channel')

    @commands.command()
    async def resume(self, ctx):
        global voice_clients
        if ctx.guild.id in voice_clients:
            voice_clients[ctx.guild.id].resume()
            await ctx.send('Resumed')
        else:
            await ctx.send('Not in a voice channel')


# Start the bot
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


# Run the bot
client.add_cog(MusicBot(client))
client.run(TOKEN)
