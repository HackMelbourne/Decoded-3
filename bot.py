import json
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
# load environment variables
TOKEN = os.getenv("TOKEN")
GUILDS = os.getenv("GUILDS")
# convert guilds from .env file to discord.py guild objects
GUILDS = json.loads(GUILDS)
GUILDS = [discord.Object(id=guild) for guild in GUILDS]


class Bot(commands.Bot):
    # constructor to initialize object
    def __init__(self, token, guild_list):
        # call parent constructor
        super().__init__(command_prefix="",
                         intents=discord.Intents.default())
        # store bot token
        self.token = token
        # store guild list
        self.guild_list = guild_list

    # load tictactoe game engine COG extension
    async def setup_hook(self):
        await self.load_extension(f"cogs.tictactoe")

        # manually sync slash commands to each guild specified in .env file
        for guild in self.guilds:
            await self.tree.sync(guild=guild)

    # print message when the bot is finished initializing and is
    # ready to be used
    async def on_ready(self):
        print("ready...")


# initialize bot with TOKEN and GUILDS from .env file
bot = Bot(TOKEN, GUILDS)
# run bot with its token
bot.run(bot.token)
