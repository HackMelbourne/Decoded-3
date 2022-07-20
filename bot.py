from discord.ext import commands
import discord

from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!",
                         intents=discord.Intents.all())

    async def setup_hook(self):
        await self.load_extension(f"tictactoe")
        await self.tree.sync(guild=discord.Object(id=996259796426698752))

    async def on_ready(self):
        print("ready...")


bot = Bot()
bot.run(TOKEN)

if __name__ == '__main__':
    pass
