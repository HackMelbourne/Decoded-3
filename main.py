import os
from dotenv import load_dotenv
from discord.ext import commands
import discord
import asyncio

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix = "!", intents = discord.Intents.all()) # instead of a client, we create a Bot instance

# 👇 Looks inside the /cogs/ folder and loads up all of our cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        asyncio.run(client.load_extension("cogs." + filename[:-3]))  # calls the cog's `setup()` function

client.run(TOKEN)