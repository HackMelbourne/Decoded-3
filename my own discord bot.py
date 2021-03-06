import asyncio

import discord
import youtube_dl

token = 'OTk3MDIzNzcwNTM3NjI3Njgw.GSbnw_.YwoZBo5S4L1MIdkM8-obEgxKoTB5c8kiW3qH1g'

client = discord.Client()

# making a bot that block censored words
# censored word list 
block_words = ["peepee", "poopoo"]

@client.event 
async def on_message2(msg):

    if msg.author != client.user:
        for text in block_words:
            if "Moderator" not in str(msg.author.roles) and text in str(msg.content.lower()):
                await msg.delete()
                return

# music bot 
voice_clients = {}

#youtube best audio options
yt_dl_opts = {'formats': 'beastaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

#option for only audio and no video
ffmpeg_options = {'options': '-vn'}

#main music bot
@client.event
async def on_message(msg):
    if msg.content.startswith('?play'):
        try:
            voice_client = await msg.author.voice.channel.connect()
            voice_clients[voice_client.guild.id] = voice_client
        except Exception as ex:
            raise ex
        # so that if the user dont put a space between the play and link
        try:
            url = msg.content.split()[1]

            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

            song = data['formats'][0]['url']
            player = discord.FFmpegPCMAudio(song, **ffmpeg_options, executable="C:\\ffmpeg\\ffmpeg.exe")

            voice_clients[msg.guild.id].play(player)
        except Exception as ex:
            raise ex

    if msg.content.startswith("?pause"):
        try:
            voice_clients[msg.guild.id].pause()
        except Exception as err:
                print(err)

    if msg.content.startswith("?resume"):
        try:
            voice_clients[msg.guild.id].resume()
        except Exception as err:
                print(err)

    if msg.content.startswith("?stop"):
        try:
            voice_clients[msg.guild.id].stop()
            await voice_clients[msg.guild.id].disconnect()

        except Exception as err:
                print(err)

client.run(token)

