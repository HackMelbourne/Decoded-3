from ast import alias
import discord
import asyncio
import matplotlib.pyplot as plt
import numpy as np
from discord.ext import commands
import emoji


class Poll(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  async def create_bar_chart(self,options, reactions, question):
    totalVotes = 0
    votes = []
    #calculate the number of votes for each option
    for reaction in reactions:
      v=0
      async for _ in reaction.users():
        v+=1
      totalVotes += v
      votes.append(v)

    percentages = [round((vote/totalVotes)* 100, 2) for vote in votes]
    fig, ax = plt.subplots()
    y_pos = np.arange(len(options))
    error = np.random.rand(len(options))
    ax.barh(y_pos, percentages, xerr=error, align='center')
    ax.set_yticks(y_pos, labels=options)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Votes (%)')
    ax.set_title(question)
    plt.savefig('chart.png')


  @commands.command(aliases=["p"])
  async def init_poll(self, ctx, question, time, *options):
    if len(options) > 3:
      await ctx.send("The number of options cannot exceed the allowed limit")
    embed = discord.Embed(title = question,
                          description= f'Poll will end in {time} seconds :alarm_clock:. There are {len(options)} options:')
    tmp = [':one:', ':two:', ':three:'][:len(options)]
    emojis = [emoji.emojize(e, language='alias') for e in tmp]
    for i in range(len(options)):
        emo = emojis[i]
        embed.add_field(name = emo, value = options[i], inline = True)
    embed.add_field(name="Instructions", value="React to cast a vote", inline=False)
    embed.set_footer(text = f'This poll is created by {ctx.author.name}')
    poll = await ctx.send(embed = embed)
    # add emojis as reactions to the poll
    for emo in emojis:
      await poll.add_reaction(emo)
    await asyncio.sleep(int(time))
    #calculate the result of the poll
    message = await ctx.fetch_message(poll.id)
    # create a bar chart as a result
    await self.create_bar_chart(options, message.reactions, question)
    result = discord.Embed(title='Result', description = "Here are the vote results")
    file = discord.File("chart.png")
    result.set_image(url="attachment://chart.png")
    await ctx.send(file=file, embed = result)


async def setup(bot):
    await bot.add_cog(Poll(bot))