import discord
from discord.ext import commands
import music

#install pakage 'PyNacl'

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range (len(cogs)):
  cogs[i].setup(client)

client.run('Your Discord Bot token ID')