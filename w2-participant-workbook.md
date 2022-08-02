<h1 align="center">[Participant's Workbook] Introduction to Discord.py</h1>

> Related Pages: [DecodED 3](./README.md)

---

<h2>Table of Contents</h2>
<details>
<summary>Table of Contents</summary><h1 align="center">[Participant's Workbook] Introduction to Discord.py</h1>

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

## 1. Create Bot Object
* [Applications Page](https://discord.com/developers/applications)

Follow the steps outlined in the previous workshops [insert link]

Since we will be using a special thingy called 'slash commands', our bot class will look slightly different.

The bot class we create inherits methods and attributes defined by the Bot class provided by the library. We need to add our bot token and guilds to the class for the class to work. We also need to define a `setup_hook` method to intitialize the COGS which contains the tictactoe game engine.

To create our guild attribute and bot token:
    - We first need to create an environment file (link)

 discord slash commands take 1-2 hours to sync globally (for every guild). We can pass in specific guilds where the commands we create will sync instantly.

Here's an example of a completed Bot Class
```
    class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!",
                         intents=discord.Intents.all())
        self.GUILDS = GUILDS
        self.TOKEN = TOKEN

    async def setup_hook(self):
        await self.load_extension(f"tictactoe")
        for guild in self.GUILDS:
            await self.tree.sync(guild=guild)

    async def on_ready(self):
        print("ready...")
```

## 3. Create TicTacToe Button

    Use button class from discord py library.
    Specify button style, label, and row.
    Button needs to store its position in the board. (row, col)


## 4. Create TicTacToe Board
  Use view class from discord py library.
  Store player objects in the board.
  Specify current player. (default player1 starts first)
    create board
    - 2d list of 0s using numpy

    fill board with tictactoe buttons defined earlier


## 5. Game Logic

    Create the tictactoe logic for deciding a winner within a function called `check_winner` that's placed inside the TicTacToe Board class.
    (hint) Using numpy we check for vertical and horizontal winners
    (hint) take the sum for a given row/column if its equal to size of the board then we know there is a winner
    (hint) We also have to check for diagonal winners using list indexing

## 6. TicTacToe Buttons handle click

    The code for this needs to be placed within a function `async def callback(self, interaction)`, as stated in the docs
    
    Here's what should be included within this function:
    - Check if the right player is clicking
    - Update color and label of button to color of player that clicked
    - Disable the button to prevent further interaction
    - Update tictactoe board 
        - 1 if player1 clicked
        - -1 if player2 clicked
    - Response to acknowledge click of button

## 7. Create Commands (https://gist.github.com/lykn/bac99b06d45ff8eed34c2220d86b6bf4)
    - define the command name and description
    - define user input (discord member)
    - define the user input description
    - acknowledge command by sending tictactoe board view

    ```python
    class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="tictactoe",
        description="Play a game of TicTacToe"
    )
    @app_commands.describe(
        opponent="User you want to play with"
    )
    async def tictactoe(self, interaction, opponent: discord.Member):
        player_1 = interaction.user
        player_2 = opponent

        if player_1 == player_2 or player_2.bot:
            await interaction.response.send_message("you cannot challenge that user")
        else:
            await interaction.response.send_message(
                f":game_die: `{player_1.display_name}` **VS** `{player_2.display_name}`\n\n{player_1.mention}, select your move:",
                view=TicTacToe(player_1, player_2))
    ```


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
