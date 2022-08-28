from discord.ext import commands

class Hello(commands.Cog):  # 👈 cog class called `Hello`
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener() # 👈 this is a decorator for events/listeners
    async def on_ready(self):
        print(f'We have logged in as {self.client.user}')
    
    @commands.command() # this is for making a command
    async def hello(self, ctx): # 👈 called when messages contain `!hello`
        await ctx.send(f'Hi!')

async def setup(bot): # 👈 a extension must have a setup function
    await bot.add_cog(Hello(bot)) # 👈 adding the cog