# Inspired by https://github.com/afazio1/robotic-nation-proj/blob/main/projects/discord-bot/new-music-bot/music-yt.py

import os
import subprocess
import time

import discord
import requests
import wavelink
from discord.ext import commands
from dotenv import load_dotenv


class MusicBot(commands.Cog):
    voice_clients = {}

    def __init__(self, client):
        self.client = client

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

    @commands.command()
    async def leave(self, ctx):
        if ctx.guild.id in self.voice_clients:
            await self.voice_clients[ctx.guild.id].stop()
            del self.voice_clients[ctx.guild.id]
            await ctx.send('Left')
        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, *, search: wavelink.YouTubeTrack):
        if ctx.guild.id not in self.voice_clients:
            # Join the user's voice channel
            await self.join(ctx)
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

    @commands.command()
    async def stop(self, ctx):
        if ctx.guild.id in self.voice_clients:
            await self.voice_clients[ctx.guild.id].stop()
            await ctx.send('Stopped')
        else:
            await ctx.send('Not in a voice channel')

    @commands.command()
    async def pause(self, ctx):
        if ctx.guild.id in self.voice_clients:
            await self.voice_clients[ctx.guild.id].pause()
            await ctx.send('Paused')
        else:
            await ctx.send('Not in a voice channel')

    @commands.command()
    async def resume(self, ctx):
        if ctx.guild.id in self.voice_clients:
            await self.voice_clients[ctx.guild.id].resume()
            await ctx.send('Resumed')
        else:
            await ctx.send('Not in a voice channel')

    # Start the bot
    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as')
        print(self.client.user.name)
        print(self.client.user.id)
        print('------')
        # Try start Lavafront server
        subprocess.Popen(["./jdk-13.0.2/bin/java", "-jar", "Lavalink.jar"])
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


def setup(bot):
    bot.add_cog(MusicBot(bot))


if __name__ == '__main__':
    load_dotenv()
    TOKEN = os.getenv('TOKEN')

    client = commands.Bot(command_prefix='!')
    client.add_cog(MusicBot(client))
    client.run(TOKEN)
