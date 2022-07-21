from discord.ext import commands
import discord
from dotenv import load_dotenv
import os
import json

load_dotenv()
TOKEN = os.getenv("TOKEN")

GUILDS = os.getenv("GUILDS")
GUILDS = json.loads(GUILDS)
GUILDS = [discord.Object(id=guild) for guild in GUILDS]


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!",
                         intents=discord.Intents.all())
        self.GUILDS = GUILDS
        self.TOKEN = TOKEN

    async def setup_hook(self):
        await self.load_extension(f"tictactoe")
        for guild in self.GUILDS:
            await self.tree.sync(guild=guild)

    async def on_ready(self):
        print("ready...")


bot = Bot()
bot.run(bot.TOKEN)

if __name__ == '__main__':
    pass
