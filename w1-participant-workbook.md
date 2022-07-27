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
    * discord.py is basically a set of tools which will allow us to control our bot with simple function calls.
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
<details>
<summary><b>❓ What are environment variables?</b></summary>

When a program is run, it may need information from the operating system to configure its behaviour. This might include the operating system, current running folder, or more important things like passwords to various services (Discord here!). Basically, environment variables are variables/information about the environment its running on. They are a useful tool in providing information to your program, which is separate from your code. Developers commonly use `.env` files to specify these variables.

</details>

* `.env` have several advantages:
1. They help different developers to keep their passwords separate from each other.
1. When using a VCS (GitHub), you can prevent your `.env` file from being uploaded to the internet, thus protecting all of your passwords.

To use a .env file, first make a `.env` file in the same folder as your code:
```python
# File name: .env
# Add comments with '#'
TOKEN=example.token.abc123
```
Then in your code file:
  ```python
  # ./main.py (after the other imports)
  from dotenv import load_dotenv
  load_dotenv()
  TOKEN = os.getenv('TOKEN')
  ```
Try changing the content of your `.env` file and doing `print(TOKEN)`, what happens?
#### **💡 Challenge**
Can you try defining your own environment variable (besides `TOKEN`), and printing it to the console? How about printing the current operating system using only environment variables? (Will need some googling!)

Now that we have the token for our bot, let's add it to our server. Do do this, we will use the official [Discord Applications Page.](https://discord.com/developers/applications)
## 4. Make the Bot say "Hello, World!"
* TODO Slides/Explanation: what are decorators?
* TODO Slides/Explanation: what are events and callbacks - what is async and await (extension)
  ```python
  # 

  ```
* ✅ 

<details>
<summary><b>❓ What are events?</b></summary>

Events are exactly as you would think, stuff that happens that we want to know about. Examples would be someone joining a server, sending a message, or reacting to something.

To 'hook' onto an event, we use a decorator on a function call:
```python
@client.event
async def on_message(message):
  ...
```
The function name tells discord.py what event we're listening to (in this case, messages).

</details>

<details>
<summary><b>❓ What is <code>async</code> and <code>await</code>?</b></summary>

  Often in coding, you will need to perform a task, and wait for the response before you can do anything. An example would be Gmail, the website needs to wait for the mail to send, before telling you it's sent.
  Using `async` on a function lets Python know that this task involves waiting for something:
  ```python
  async def send_mail():
    await login()
    await send()
  ```
  and `await` tells Python to wait for an `async` function to finish before proceeding:
  ```python
  await send_mail()
  print("Your mail was sent!")
  # As opposed to
  send_mail()
  print("This will be printed immediately")
  ```
  In the context of discord.py, we can use `async` on our functions to tell discord.py it's going to do a long-running task, and `await` to do that task:
  ```python
  async def on_join(self, ctx):
    await ctx.send("Welcome to the server!")
  ```

</details>


## 5. Adding Commands
* 

## 6. Cogs
* TODO Slides/Explanation: what and why of [cogs](https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html)

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
* [Python Discord Bot Tutorial – Code a Discord Bot And Host it for Free](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/)
