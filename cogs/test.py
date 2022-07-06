from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client # defining bot as global var in class

    @commands.Cog.listener() # this is a decorator for events/listeners
    async def on_ready(self):
        print(f'We have logged in as {self.client.user}')

    @commands.command() # this is for making a command
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}')
        
def setup(bot): # a extension must have a setup function
	bot.add_cog(Test(bot)) # adding a cog