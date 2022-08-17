import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = 'NzM5MzkwNjI5NjIwMjE5OTg1.G6jXaM.am2j6rhR3c4enHoQIs0koWrDxnktighemgFL9M'

GUILDS = [739390096213803057]
# GUILDS = json.loads(GUILDS)
GUILDS = [discord.Object(id=guild) for guild in GUILDS]


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!",
                         intents=discord.Intents.all())
        self.GUILDS = GUILDS
        self.TOKEN = TOKEN

    async def setup_hook(self):
        await self.load_extension(f"cogs.tictactoe")
        for guild in self.GUILDS:
            await self.tree.sync(guild=guild)

    async def on_ready(self):
        print("ready...")


bot = Bot()
bot.run(bot.TOKEN)

if __name__ == '__main__':
    pass
