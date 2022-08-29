import discord
import os

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(msg):
    # print(msg.content)
    if msg.author == client.user:
        return
    if msg.content.startswith('$hello'):
        await msg.channel.send(f'Hello, {msg.author.name}!')

client.run(TOKEN)
