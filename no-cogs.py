# basic bot without cogs

import discord
import os

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)
