import discord
import os
from discord.ext import commands
import poll
from dotenv import load_dotenv

load_dotenv()
#bot object
bot = commands.Bot(command_prefix = "$", intents = intents)
client = discord.Client()

# client gets ready 
@bot.event
async def on_ready():
  print("The bot is ready.")

#add poll to the current bot
bot.add_cog(poll.Poll(bot))
bot.run(os.environ.get('TOKEN'))

