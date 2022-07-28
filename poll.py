from functools import total_ordering
from click import command
import discord
import asyncio
import matplotlib.pyplot as plt
import numpy as np
import EmojiCollection

from discord.ext import commands
class Poll(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.emojiCollection = EmojiCollection.EmojiCollection()
  async def create_bar_chart(self,options, reactions, question):
    totalVotes = 0
    votes = []
    #calculate the number of votes for each option
    for reaction in reactions:
      v = await reaction.users().flatten()
      totalVotes += len(v)
      votes.append(len(v))
    
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
    if len(options) > 5:
      await ctx.send("The number of options cannot exceed the allowed limit")
    embed = discord.Embed(title = question,
                          description= f'Poll will end in {time} seconds :alarm_clock:. There are {len(options)} options:')
    emojis = []
    for option in options:
        emoji = self.emojiCollection.search(option)
        embed.add_field(name = emoji, value = option, inline = True)
        emojis.append(emoji)
    embed.add_field(name="Instructions", value="React to cast a vote", inline=False)
    embed.set_footer(text = f'This poll is created by {ctx.author.name}')
    #embed.set_thumbnail(url=)
    self.emojiCollection.quit()
    poll = await ctx.send(embed = embed)
    #add emojis as reactions to the poll
    for emoji in emojis:
      await poll.add_reaction(emoji)
    await asyncio.sleep(int(time))
    #calculate the result of the poll 
    message = await ctx.fetch_message(poll.id)
    #create a bar chart as a result
    await self.create_bar_chart(options, message.reactions, question)
    result = discord.Embed(title='Result', description = "Here are the vote results")
    file = discord.File("chart.png")
    result.set_image(url="attachment://chart.png")
    await ctx.send(file=file, embed = result)

    
  
      