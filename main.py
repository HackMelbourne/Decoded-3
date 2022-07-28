from ast import alias
import discord
import os
from discord.ext import commands
import poll
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.members =   True
intents.reactions = True
#bot object
bot = commands.Bot(command_prefix = "$", intents = intents)
client = discord.Client()

# client gets ready 
@bot.event
async def on_ready():
  print("The bot is ready.")

#bot listens to messages sent from members
@bot.event
async def on_message(message):
  if message.content == "hello":
    await message.channel.send("pies are better than cakes. change my mind.")
  await bot.process_commands(message)

#add poll to the current bot
bot.add_cog(poll.Poll(bot))
bot.run(os.environ.get('TOKEN'))

