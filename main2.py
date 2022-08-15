# main.py
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix="!")

# Looks inside the /cogs/ folder and loads up all of our cogs
for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		print("Loaded COG {}".format(filename))
		client.load_extension("cogs." + filename[:-3])

client.run(TOKEN)
