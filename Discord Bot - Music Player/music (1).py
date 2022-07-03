import discord
from discord.ext import commands
# we will import youtube dl to use youtube features
import youtube_dl

class music(commands.Cog):
  def __init__(self, client):
    self.client = client 

  @commands.command()
  async def join(self, ctx):
    if ctx.author.voice is None:
      await ctx.send("You're not in a voice channel!")
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
      await voice_channel.connect()
    else:
      await ctx.voice_client.moce_to(voice_channel)

  @commands.command()
  async def disconnect(self, ctx):
      await ctx.voice_client.disconnect()

  @commands.command()
  async def play(self, ctx, url):
    ctx.voice_client.stop()
    #FFMPEG HANDELS the streaming of music in discord 
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconect_dealy_max 5', 'options': '-vn'}
    #YDL is just to make sure the audio comes in best streaming quality
    YDL_OPTIONS = {'format':"bestaudio"}
    vc = ctx.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url, download=False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegAudio.from_probe(url2, **FFMPEG_OPTIONS)
      vc.play(source)
  # to pasue the music
  @commands.command()
  async def pause(self, ctx):
      await ctx.voice_client.pause()
      await ctx.send("Paused")
  # to resume the music
  @commands.command()
  async def resume(self, ctx):
      await ctx.voice_client.resume()
      await ctx.send("Resumed")

def setup(client):
  client.add_cog(music(client))