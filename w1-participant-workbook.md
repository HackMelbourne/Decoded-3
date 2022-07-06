<h1 align="center">[Participant's Workbook] Introduction to Discord.py</h1>

> Related Pages: [DecodED 3](./README.md)

---

<h2>Table of Contents</h2>
<details>
<summary>Table of Contents</summary>

- [0. Create a Discord Account and Discord Server](#0-create-a-discord-account-and-discord-server)
  - [Create a Discord Account](#create-a-discord-account)
  - [Create a Discord Server](#create-a-discord-server)
- [1. Create an Application](#1-create-an-application)
- [2. Installing Modules: `discord.py` and `python-dotenv`](#2-installing-modules-discordpy-and-python-dotenv)
- [3. Creating a Bot and Adding it to your server](#3-creating-a-bot-and-adding-it-to-your-server)
  - [Environment Variables](#environment-variables)
- [4. Make the Bot say "Hello, World!"](#4-make-the-bot-say-hello-world)
    - [❓ What are events?](#-what-are-events)
    - [❓ What is `async` and `await`?](#-what-is-async-and-await)
- [5. Adding Commands](#5-adding-commands)
- [6. Cogs](#6-cogs)
- [6. Host your bot on repl.it](#6-host-your-bot-on-replit)
- [Related Links:](#related-links)

</details>

---

## 0. Create a Discord Account and Discord Server
* Before creating our bot, please make sure you create a Discord Account (it's free!) and a Discord Server to test your bot in
### Create a Discord Account

### Create a Discord Server
> 📝 NOTE: Discord servers are sometimes refered to as **'guilds'** in some documentation (because some people confuse the word 'server' with computer servers 🗄️ XD)

## 1. Create an Application
* [Applications Page](https://discord.com/developers/applications)

## 2. Installing Modules: `discord.py` and `python-dotenv`
  * Before we begin creating the bot, we have to install a few modules
  * Install `discord.py`
    * discord.py is a modern, easy to use, feature-rich, and async ready API wrapper for Discord - basically, this is what allows us to connects our code with Discord (TODO someone can rephrase what an API is lol)
    * to install it, type this into your terminal:
      ```
      pip install -U discord.py
      ```
  * Install `python-dotenv`
    * `python-dotenv` is used to access our secret Discord token, which we will store in a `.env` file
    * to install it, type this into your terminal:
      ```
      pip install -U python-dotenv
      ```
  * Let us know if you run into any errors during installation!

## 3. Creating a Bot and Adding it to your server

### Environment Variables
* TODO Why we need environment variables: danger of leaving your keys around
  ```python
  # ./main.py (after the other imports)
  from dotenv import load_dotenv
  load_dotenv()
  TOKEN = os.getenv('TOKEN')
  ```

## 4. Make the Bot say "Hello, World!"
* TODO Slides/Explanation: what are events - what is async and await (extension)
* TODO Slides/Explanation: what are decorators?

💡 
💭
💬
❗

#### ❓ What are events?

#### ❓ What is `async` and `await`?

## 5. Adding Commands


## 6. Cogs
* TODO Slides/Explanation: what and why of cogs

  ```python
  # ./main.py
  from discord.ext import commands
  import os

  client = commands.Bot(command_prefix = "!")

  # Looks inside the /cogs/ folder and loads up all of our cogs
  for filename in os.listdir("./cogs"):
      if filename.endswith(".py"):
          client.load_extension("cogs." + filename[:-3])

  client.run(TOKEN)
  ```

  ```python
  # ./cogs/test.py
  from discord.ext import commands

  class Test(commands.Cog):
      def __init__(self, client):
          self.client = client

      @commands.Cog.listener() # this is a decorator for events/listeners
      async def on_ready(self):
          print(f'We have logged in as {self.client.user}')

      @commands.command() # this is for making a command
      async def hello(self, ctx): # a command that says Hello! (called using !hello)
          await ctx.send(f'Hello!')

      @commands.command() # this is for making a command
      async def ping(self, ctx):
          await ctx.send(f'Pong! {round(self.bot.latency * 1000)}')
          
  def setup(bot): # a extension must have a setup function
      bot.add_cog(Test(bot)) # adding a cog
  ```

## 6. Host your bot on repl.it
* 

## Related Links:
* [Creating a Bot Account | discord.py](https://discordpy.readthedocs.io/en/stable/discord.html)

