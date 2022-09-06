<h1 align="center">TicTacToe Bot</h1>

---

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Object Oriented Concepts](#object-oriented-concepts)
    - [Class and Objects](#class-and-objects)
    - [Inheritance](#inheritance)
- [0. Installing Dependencies](#0-installing-dependencies)
    - [discord.py](#discordpy)
    - [numpy](#numpy)
    - [Installation](#installation)
- [1. Creating Bot Object](#1-creating-bot-object)
    - [How to obtain guild id?](#how-to-obtain-guild-id)
    - [Create `.env` file](#create-env-file)
    - [Create `bot.py`](#create-botpy)
    - [Load environment variables](#load-environment-variables)
    - [Bot class](#bot-class)
        - [What is `self`?](#what-is-self)
        - [What is `super()`?](#what-is-super)
- [2. Create TicTacToe Button](#2-create-tictactoe-button)
- [3. Create TicTacToe Board](#3-create-tictactoe-board)
- [4. TicTacToe Buttons handle click](#4-tictactoe-buttons-handle-click)
- [5. Game Logic](#5-game-logic)
- [6. Create Slash Commands](#6-create-slash-commands)

---

## Object Oriented Concepts

### Class and objects

<br />
<img src="images/class.png" width="500" />
<br />

A class is an abstract blueprint used to create more specific objects. On the other hand, an object is an instance
derived from a class.

[learn more](https://realpython.com/python3-object-oriented-programming/)

### Inheritance

<br />
<img src="images/inheritance.png" width="500"/>
<br />

Inheritance is one of the most important aspects of OOP. It allows classes to inherit features of other classes. Put
another way, parent classes extend attributes and behaviors to child classes. Inheritance supports code reusability.

[learn more](https://realpython.com/python3-object-oriented-programming/)

---

## 0. Installing Dependencies

### discord.py

For this workshop we will be mainly working with the latest discord.py library which is a wrapper for discord's API.
Basically a library which will allow us to control our bot with simple function calls.

[documentation](https://discordpy.readthedocs.io/en/stable/index.html)

### numpy

We will also be using the numpy library which allows us to easily work with multidimensional arrays. A 2D-array will be
the underlying data structure we use to represent a tictactoe board.

[documentation](https://numpy.org/doc/stable/)

### Installation

We have simplified the process of installing the libraries needed for this workshop. Simply run the command bellow in
your terminal shell.

`pip install -r requirements.txt`

---

## 1. Creating Bot Object

For this workshop, think of guilds as discord severs. Discord slash commands take 2-3 hours to sync globally across all
guilds. To overcome this limitation, we need to specify specific guild ids where the commands we define will sync
instantly.

### How to obtain guild id?

0. Enable developer mode on discord settings. This setting can be found under "Advanced".
1. Right-click on the guild icon.
2. Select "Copy ID".

### Create `.env` file

The `.env` file will contain our environment variables. The `.env` file should have the following format.

```
TOKEN=bot token here
GUILDS=[guild ids here separated by commas]
```

### Create `bot.py`

Create a file named `bot.py`. This file will contain our bot object. We also need to import a couple of libraries.

```python
import json
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
```

### Load environment variables

Load `TOKEN` and `GUILDS` environment variables.

```python
load_dotenv()
# load environment variables
TOKEN = os.getenv("TOKEN")
GUILDS = os.getenv("GUILDS")
# convert guilds from .env file to discord.py guild objects
GUILDS = json.loads(GUILDS)
GUILDS = [discord.Object(id=guild) for guild in GUILDS]
```

### Bot class

The `Bot` class we define inherits methods and attributes defined by the `commands.Bot` class provided by the discord.py
library. We are essentially extending the functionality of the class provided by the libraries by adding our own
attributes and methods. We also need to define a `setup_hook()` method to load the COG extension which contains the
tictactoe game engine. This method will also sync the slash commands to each guild specified in `.env` file.

```Python
class Bot(commands.Bot):
    # constructor to initialize object
    def __init__(self, token, guild_list):
        # call parent constructor
        super().__init__(command_prefix="",
                         intents=discord.Intents.default())
        # store bot token
        self.token = token
        # store guild list
        self.guild_list = guild_list

    # load tictactoe game engine COG extension
    async def setup_hook(self):
        await self.load_extension(f"cogs.tictactoe")

        # manually sync slash commands to each guild specified in .env file
        for guild in self.guilds:
            await self.tree.sync(guild=guild)

    # print message when the bot is finished initializing and is
    # ready to be used
    async def on_ready(self):
        print("ready...")
```

#### What is `self`?

`self` is simply a keyword used to represent an instance (object) of the given class.

#### What is `super()`?

`super()` is a reference to superclass (parent) objects.

## 2. Create TicTacToe Button

We wil now create our `TicTacToeButton` class. The objects from this class will represent the clickable buttons of the
TicTacToe board. The class will inherit the `discord.ui.Button` class from the discord.py library.

We will first initialise the style and position of the button:

create our button class

```python
class TicTacToeButton(discord.ui.Button):

```

```python
def __init__(self, row, col):
    super().__init__(style=discord.ButtonStyle.secondary, label=" ", row=row)
    self.row = row
    self.col = col
```

The different styles of a discord button can be
found [here](https://user-images.githubusercontent.com/88476243/141746269-aaea9f9b-8f8e-4c59-9b67-75ec6e19d878.png)

## 3. Create TicTacToe Board

The `TicTacToe` class represents the TicTacToe board users play on. It inherits the `discord.ui.View` class from the
discord.py library.

The TicTacToe board will need to store state of the board:

1. Player objects of current players
2. Specify current player (by default player1 starts first)
3. Create board
   two-dimensional list initialized using numpy library
4. Fill board with tictactoe buttons defined earlier

Thus the initialisation for the Board:

```python
def __init__(self, player_1, player_2):
    super().__init__()
    self.player_1 = player_1
    self.player_2 = player_2
    self.current_player = self.player_1
    self.board = np.zeros((SIZE, SIZE))

    for row in range(SIZE):
        for col in range(SIZE):
            self.add_item(TicTacToeButton(row, col))
```

## 4. TicTacToe Buttons handle click

The code for handling button clicks needs to be placed within this function (as per the docs) under
the `TicTacToeButton` class:

```Python
async def callback(self, interaction):
```

This function is called whenever the button is clicked. Here are some of the variables you might need to make the
required changes for a button click:

```Python
interaction.user  # The user that's clicking the button
self.style  # The style of the current button
self.label  # The text on the current button
self.disabled  # Specifies whether the button is disabled: True / False
self.view.board[self.row][self.col]  # The current state of the game board (as defined in Step 3)
self.view.current_player  # The current player that's supposed to play
```

Here's what should be included within this function:

- Update color and label of button to color of player that clicked
- Disable the button to prevent further interaction
- Update tictactoe board
    - 1 if player1 clicked
    - -1 if player2 clicked
- Response to acknowledge click of button

At the end of the function, you will need to update the board to reflect the latest changes. You can also include a
message at the top the board by specifying a `content`. This is done like so:

```Python
await interaction.response.edit_message(content=content, view=self.view)
```

## 5. Game Logic

Create the tictactoe logic for deciding a winner within a function called `check_winner(self)` that's placed inside
the `TicTacToe` class.

You can access the current state of the board by using `self.board`.

<details>
<summary>Hint #1</summary>
Take the sum for a given row/column if its equal to size of the board then we know there is a winner

```
[[1,1,1],
[0,0,0],
[0,0,0]]
```

</details>

<details> 
<summary>Hint #2</summary>
We also have to check for diagonal winners using list indexing

```
[[0,0,1],
[0,1,0],
[1,0,0]]
```

</details>

## 6. Create Slash Commands

### TicTacToe Class and slash commands

As a final step to bring our tictactoe bot to life, we will use slash commands to interface with our bot. We now create
a `TicTacToe` class which inherits methods and attributes from the `commands.Cog` class provided by the library. This
allows us to store the tictactoe game engine as a COG in its own file.

```python
class TicTacToe(commands.Cog):
    # constructor to store bot object
    def __init__(self, bot):
        self.bot = bot

    # specify slash command name and description
    @app_commands.command(
        name="tictactoe",
        description="Play a game of TicTacToe"
    )
    # specify slash command parameter description
    @app_commands.describe(
        opponent="User you want to play with"
    )
    # function is run every time a slash command is issued
    # specify that the slash command parameter will be a discord member
    async def tictactoe(self, interaction, opponent: discord.Member):
        # player_1 is the user that issued the slash command
        player_1 = interaction.user
        # player_2 is the opponent specified in the slash command
        player_2 = opponent

        # make sure user does not challenger itself or the bot
        if player_1 == player_2 or player_2.bot:
            await interaction.response.send_message(
                "you cannot challenge that user")
        else:
            # acknowledge command by responding with a message and sending a
            # tictactoe board view
            await interaction.response.send_message(
                f":game_die: `{player_1.display_name}` **VS** `{player_2.display_name}`\n\n"
                f"{player_1.mention}, select your move:",
                view=TicTacToeView(player_1, player_2))
```

[lean more about type hints](https://www.pythontutorial.net/python-basics/python-type-hints/)

### Setup COGS

Finally, we have to create a `setup` function which gets called whenever this COG extension is loaded.

```python
async def setup(bot):
    # add COG extension to calling bot
    await bot.add_cog(
        TicTacToe(bot),
        # calling bot's guild list
        guilds=bot.guild_list
    )
```

## 7. Run the bot

Now back to the `bot.py` file we previously created, we can now instantiate a bot with the TOKEN and GUILDS we have
specified in the .env file. After that we can simply run the bot.

```python
# initialize bot with TOKEN and GUILDS from .env file
bot = Bot(TOKEN, GUILDS)
# run bot with its token
bot.run(bot.token)
```
