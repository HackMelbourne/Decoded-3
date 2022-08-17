# main.py
import asyncio
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Looks inside the /cogs/ folder and loads up all of our cogs
for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		# run function synchronously using subprocess
		asyncio.run(client.load_extension("cogs." + filename[:-3]))

client.run(TOKEN)
