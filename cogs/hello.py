from discord.ext import commands


class Hello(commands.Cog):
    def __init__(self, client):
        self.client = client  # defining bot as global var in class

    @commands.Cog.listener()  # this is a decorator for events/listeners
    async def on_ready(self):
        print(f'We have logged in as {self.client.user}')

    @commands.command()  # this is for making a command
    async def hello(self, ctx):
        print(ctx)
        await ctx.send(f'Hi!')


async def setup(bot):  # an extension must have a setup function
    await bot.add_cog(Hello(bot))  # adding a cog
