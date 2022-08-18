# discord-bot-poll-system
<h1 align="center">[Participant's Workbook] Create polling using Discord.py</h1>

<h2>Table of Contents</h2>
<details>
<summary>Table of Contents</summary>

---
- [0. Installing Modules: `discord.py` and `python-dotenv`, `asyncio`, `matplotlib`, `numpy`, `os`, `emoji`](#0-installing-modules)
    - [✅ Task: Install `discord.py`](#-task-install-discordpy)
    - [✅ Task: Install `python-dotenv`](#-task-install-python-dotenv)
    - [✅ Task: Install `asyncio`](#-task-install-asyncio)
    - [✅ Task: Install `matplotlib`](#-task-install-matplotlib)
    - [✅ Task: Install `numpy`](#-task-install-numpy)
    - [✅ Task: Install `os`](#-task-install-os)
    - [✅ Task: Install `emoji`](#-task-install-emoji)
- [1. ✅ Task: Create a Cog for all your 'Poll' commands](#1-create-a-cog-for-all-your-poll-commands)
    - [✅ Task: Import essential modules](#-task-import-essential-modules)
    - [✅ Task: Create a constructor for the Poll Cog](#-task-create-a-constructor-for-the-Poll-Cog)
    - [✅ Task: Get inputs from users before sending back the poll](#-task-get-inputs-from-users-before-sending-back-the-poll)
    - [✅ Task: Send back an Embed as a poll](#-task-send-back-an-embed-as-a-poll)
    - [✅ Task: Use emoji module to convert strings to emojis and add fields and footer](#-task-use-emoji-module-to-convert-strings-to-emojis-and-add-fields-and-footer)
- [2. [💡 Extension] implement web scrapping with Selenium to customise your poll](#2--extension-implement-web-scrapping-to-customise-your-poll)
- [Related Links:](#related-links)

</details>

---

## 0. Installing Modules

> 📝 NOTE: You can skip this step if you're using **Replit** as it
> can [automatically import](https://docs.replit.com/programming-ide/installing-packages#direct-imports) packages/modules
> it for you

* Now we're going to start writing the code for our bot!
* Before we begin creating the bot, we have to install a few modules

  <details>
  <summary><b>🧩 Hint: Accessing the Terminal in VS Code</b></summary>

* There are 2 ways to access the terminal in VS Code:
    1. using the shortcut ```Ctrl + Shift + ` ```
    2. Terminal > New Terminal

    * ![](vscode_access_terminal.gif)

  </details>

### ✅ Task: Install `discord.py`

* `discord.py` is basically a set of tools which will allow us to control our bot with simple function calls.
* you can find the documentation for `discord.py` over [here](https://discordpy.readthedocs.io/en/stable/index.html#)
* to install it, type this into your terminal:
  ```
  pip install -U discord.py
  ```

### ✅ Task: Install `python-dotenv`

* `python-dotenv` is used to access our secret Discord token, which we will store in a `.env` file
* you can find the documentation for it over [here](https://pypi.org/project/python-dotenv/)
* to install it, type this into your terminal:
  ```
  pip install -U python-dotenv
  ```
  
### ✅ Task: Install `asyncio`

* `asyncio` is used to write asynchronous code. Asynchronous code lets you execute a block of code without stopping (or blocking) the entire thread where the action is being executed.  
* you can find the documentation for it over [here](https://docs.python.org/3/library/asyncio.html)
* to install it, type this into your terminal:
  ```
  pip install -U asyncio
  ```
  
### ✅ Task: Install `matplotlib`

* `matplotlib ` is a Python library used to create chart visualization[here](https://matplotlib.org/)
* to install it, type this into your terminal:
  ```
  pip install -U matplotlib
  ```
  
### ✅ Task: Install `os`

* `os` is a module providing functions to interact with the operating system [here](https://docs.python.org/3/library/os.html)
* to install it, type this into your terminal:
  ```
  pip install -U os
  ```
### ✅ Task: Install `emoji`
* `emoji` is a library allowing us to convert string to emoji [here] https://pypi.org/project/emoji/
* to install it, type this into your terminal:
  ```
  pip install -U emoji
  ```
> 🙋 **Ask for help**: Let us know if you run into any errors during installation and we'll try to help you out!

---

## 1. Create a cog for all your poll commands
### ✅ Task: Import essential modules 
 * `discord`, `asyncio`, `matplotlib`, `numpy` are modules we want to use to create a Poll Cog. So please import them: 
    ```
    import discord
    import asyncio
    import matplotlib.pyplot as plt 
    import numpy as np
    from discord.ext import commands
    
    ```
### ✅ Task: Create a constructor for the Poll Cog
* The Poll class is a subclass of `commands.Cog` class. 
* We need a constructor to create the Cog class. This constructor can be done by using `init` method. 
* The `init` method should take the `bot` attribute to store information about our bot. 
    ```
    def __init__(self, bot): 
        self.bot = bot
    ```
### ✅ Task: Get inputs from users before sending back the poll
 * We need to write a function `init_poll` allowing us to create a poll command. A way for us to set the command is using decorator @commands.command(aliases=["p"]) above declaration of the `init_poll` function. This means when a user type `!p` , we will have a poll command. 
 * However, that's not enough as a user need to give a poll question, time for the poll and options for others to vote => give 3 more attributes for `init_poll` include question, time, *options. 
    ```
    async def init_poll(self, ctx, question, time, *options): 
    ```
 * You can see we also need to have `self` and `ctx`. We need `self` because it is a function declared inside the class. We need `ctx` because when user type their `!p` command, having the `ctx` attribute will allow us to have access to the `Context` object of the command. 
 * <img width="977" alt="Screen Shot 2022-08-17 at 8 14 25 pm" src="https://user-images.githubusercontent.com/80389972/185095123-422fab2b-f2b0-4aa8-be60-17b31d73e731.png">
 * Next, we need apply a condition for our poll. You can customise how many options permitted for a poll. In this tutorial, there are maximum 3 options allowed. 
    ```
    if len(options) > 3:
      await ctx.send("The number of options cannot exceed the allowed limit")
    ```
 * you can notice that we are making use of ctx attribute to send back a message to the server. The data type of what is returned from ctx.send(...) is discord.Message. Here is more information about discord.Message: https://discordpy.readthedocs.io/en/stable/api.html#discord.Message
### ✅ Task: Send back an Embed as a poll
 * The discord bot has to send back the message to the server through `ctx.send(embed = Embed)`. 
 * A reason why we cannot send back a string like what we previous did is because our poll have a lot of information like time, question, given options. Hence, it is gonna messy if we put all of them into a string. 
 * Instead, make use of `embed attribute`. To do that, we first need to create an Embed object as following: 
    ```
    embed = discord.Embed(title = question,
                          description= f'Poll will end in {time} seconds :alarm_clock:. There are {len(options)} options:')
    ```
### ✅ Task: Use emoji module to convert strings to emojis and add fields and footer
  * 
