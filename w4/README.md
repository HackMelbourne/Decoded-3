# discord-bot-poll-system
<h1 align="center">[Participant's Workbook] Create polling using Discord.py</h1>

<h2>Table of Contents</h2>
<details>
<summary>Table of Contents</summary>

---
- [0. Installing Modules: `discord.py` and `python-dotenv`, `asyncio`, `matplotlib`, `numpy`, `os`](#0-installing-modules)
    - [✅ Task: Install `discord.py`](#-task-install-discordpy)
    - [✅ Task: Install `python-dotenv`](#-task-install-python-dotenv)
    - [✅ Task: Install `asyncio`](#-task-install-asyncio)
    - [✅ Task: Install `matplotlib`](#-task-install-matplotlib)
    - [✅ Task: Install `numpy`](#-task-install-numpy)
    - [✅ Task: Install `os`](#-task-install-os)
- [1. ✅ Task: Create a Cog for all your 'Poll' commands](#1-create-a-cog-for-all-your-poll-commands)
    - [✅ Task: Import essential modules](#-task-import-essential-modules)
    - [✅ Task: Create a constructor for the Poll Cog](#-task-create-a-constructor-for-the-Poll-Cog)
    - [✅ Task: Create a poll based on inputs given by users](#-task-create-a-poll-based-on-inputs-given-by-users)
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
### ✅ Task: Create a poll based on inputs given by users
 * We need to write a function `init_poll` allowing us to create a poll command. A way for us to set the command is using decorator @commands.command(aliases=["p"]) above declaration of the `init_poll` function. This means when a user type `!p` , we will have a poll command. 
 * However, that's not enough as a user need to give a poll question, time for the poll and options for others to vote => give 3 more attributes for `init_poll` include question, time, *options. 
    ```
    async def init_poll(self, ctx, question, time, *options): 
    ```
 * You can see we also need to have `self` and `ctx`. We need `self` because it is a function declared inside the class. We need `ctx` because when user type their `!p` command, having the `ctx` attribute will allow us to have access to the `Context` object of the command. 
 * <img width="977" alt="Screen Shot 2022-08-17 at 8 14 25 pm" src="https://user-images.githubusercontent.com/80389972/185095123-422fab2b-f2b0-4aa8-be60-17b31d73e731.png">

    
This is the discord bot built by using discord.py library and Selenium package to automate web browser interaction with Python. I also used Math plot library to visualize the voting results as a output. 
What's special about this application is that when a poll maker creates a question and gives suggestions for other members to vote on the discord channel: there will be web site running automatically to search for corresponding emojis from this API: https://emojipedia.org and provide them to the bot. Hence, members can vote by the emoji. After a specific limit of time, the discord bot will close the poll and return the result. 
# Example output: ![Screen Shot 2022-07-26 at 10 49 36 pm](https://user-images.githubusercontent.com/80389972/181009956-22d248ef-0a0a-49d9-859c-c146bacd66b1.png)
CLICK TO THIS LINK TO SEE THE VIDEO: https://www.youtube.com/watch?v=mFfwhWzvYGI

# Installation 
There are 3 important components needed to install: python3 + web automation + discord bot. 
1. Python3: 
- Install python3: https://www.python.org/downloads/
3. Web Automation: 
- First install selenium by running this command in cmd: pip install selenium 
- Since the application uses Chrome Driver as the web driver version 104, so please make sure that you install the Driver version 104 and Google Chrome 104 to your desktop. Here are the links: 
- https://chromedriver.chromium.org/downloads
- https://www.google.com/intl/en_au/chrome/beta/
4. Discord Bot 
- Please install these follow packages: discord, asyncio, matplotlib, numpy, os, dot.env
- For example: run "pip install discord"

# Lessons
# 1. Discord bot without dynamic emojis 
# 1. Create Main.py
    STEP 1: import some already installed packages to your file (you will know why when we start using them). 
    <img width="627" alt="Screen Shot 2022-08-03 at 8 06 19 pm" src="https://user-images.githubusercontent.com/80389972/182582832-1443fd7a-d7da-4b57-8659-10c24505d685.png">
    STEP 2: create the discord bot. You can see we make use of commands module that we imported initially to create the discord bot here. You can put other string for the command prefix, for example, command_prefix = "." instead of "$". 
   <img width="627" alt="Screen Shot 2022-08-03 at 7 24 56 pm" src="https://user-images.githubusercontent.com/80389972/182574182-de000381-dddc-44f6-9734-53b5ed6c9e76.png">  
    STEP 3: create an asynchronous event listener that let us knows when our bot is ready. "The bot is ready" will print out when our bot starts running later on. You can see we are making use of 
  <img width="627" alt="Screen Shot 2022-08-03 at 8 00 08 pm" src="https://user-images.githubusercontent.com/80389972/182581448-0fbab704-a3a6-4e03-981c-224d609345c3.png">
  STEP 4: Finally, loading the token that generated in the "Set up discord bot" before.
  to run our bot: 
  <img width="627" alt="Screen Shot 2022-08-03 at 8 10 29 pm" src="https://user-images.githubusercontent.com/80389972/182583404-4dfece4e-fb96-4f13-9b7f-eb2569533baa.png">
  
# 2. Create Poll.py
STEP 1: again, import some installed packages to the file. 
   <img width="627" alt="Screen Shot 2022-08-03 at 8 39 51 pm" src="https://user-images.githubusercontent.com/80389972/182588850-16ac0bda-ad44-4dca-b25c-2af89186ba93.png">
  
STEP 2: declare the subclass of commands.Cog.
   <img width="627" alt="Screen Shot 2022-08-03 at 8 41 31 pm" src="https://user-images.githubusercontent.com/80389972/182589158-977adf2f-297e-47bc-9990-26b768459a79.png">
    - You can see __int__ method is the constructor of our class to create the Poll object later on in the Main.py file. We will need to have pass the already created bot object in the Main.py file later so that why we have to add it as an argument here. 
    
STEP 3: Now, it is time for us to declare a function and that function is decorated by discord.ext.commands.command to transform into to be discord.ext.commands.Command. 
<img width="933" alt="Screen Shot 2022-08-03 at 8 43 51 pm" src="https://user-images.githubusercontent.com/80389972/182589633-5fada6a8-e95e-4720-a66d-adaddec9eea0.png">
    - Inside the decorator, you can see we passed "p" as an argument for "aliases". "aliases" is an array of string and it is an attribute of discord.ext.commands.Command class. It allows us to have mutilple names for our commands. You can add another string, for example, "poll" into that array. 
