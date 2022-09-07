# discord-bot-poll-system
<h1 align="center">[Participant's Workbook] Create polling using Discord.py</h1>

<h2>Table of Contents</h2>
<details>
<summary>Table of Contents</summary>

---
- [1. Installing Modules: `discord.py` and `python-dotenv`, `asyncio`, `matplotlib`, `numpy`, `os`, `emoji`](#1-installing-modules)
    - [✅ Task: Install `discord.py 2.0 version`](#-task-install-discordpy)
    - [✅ Task: Install `python-dotenv`](#-task-install-python-dotenv)
    - [✅ Task: Install `asyncio`](#-task-install-asyncio)
    - [✅ Task: Install `matplotlib`](#-task-install-matplotlib)
    - [✅ Task: Install `numpy`](#-task-install-numpy)
    - [✅ Task: Install `os`](#-task-install-os)
    - [✅ Task: Install `emoji`](#-task-install-emoji)
- [2. Enable Privilege Gateway Intents](#2-enable-privilege-gateway-intents)
    - [✅ Task: Enable Privilege Gateway Intents](#-enable-privilege-gateway-intents)
- [3. ✅ Task: Create a Cog for all your 'Poll' commands](#3-create-a-cog-for-all-your-poll-commands)
    - [📚 Outcome: What are we building for this task?](#-outcome-what-are-we-building-for-this-task)
    - [✅ Task: Set up all the files](#-set-up-all-the-files)
    - [✅ Task: Import essential modules](#-task-import-essential-modules)
    - [✅ Task: Create a constructor for the Poll Cog](#-task-create-a-constructor-for-the-Poll-Cog)
    - [✅ Task: Get inputs from users before sending back the poll](#-task-get-inputs-from-users-before-sending-back-the-poll)
    - [✅ Task: Send back an Embed as a poll](#-task-send-back-an-embed-as-a-poll)
    - [✅ Task: Use emoji module to convert strings to emojis and add fields and footer](#-task-use-emoji-module-to-convert-strings-to-emojis-and-add-fields-and-footer)
    - [✅ Task: Add emojis to complete the poll and set time for users to vote](#-task-add-emojis-to-complete-the-poll-and-set-time-for-users-to-vote)
- [2. [💡 Extension] implement web scrapping with Selenium to customise your poll](#2--extension-implement-web-scrapping-to-customise-your-poll)
- [Related Links:](#related-links)

</details>

---

## 1. Installing Modules

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

### ✅ Task: Install `discord.py` 2.0 

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
## 2. Enable Privilege Gateway Intents
 * Click onto this link and enable all the Priviledged Gateway Intents [here]https://discord.com/developers/applications/994103517436465212/bot
## 3. Create a main2.py file 
### ✅ Task: Create a main2.py file where we set up our bot. 
 * Import all the modules: asyncio, os, discord, load_dotenv, commands
   ```
    import discord
    import asyncio
    import os
    from discord.ext import commands
    from dotenv import load_dotenv
   ```
 * get Token from our .env file
   ```
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
 * set up your bot 
   ```
    client = commands.Bot(command_prefix="!", intents= discord.Intents.all())
   ```
   https://discordpy.readthedocs.io/en/stable/ext/commands/api.html?highlight=commands%20bot#bots
   By having, discord.Intents.all() -> we let all bot knows that we enable all intent settings including: message_contents, members, presences
 * read python files in the "cogs" folder. Later on, we will have python files in our cogs folder and we need to make our bot to be aware of them. 
   ```
    for filename in os.listdir('./cogs'):
        if filename.endswith("py"):
            asyncio.run(client.load_extension(f"cogs.{filename[:-3]}")
            print("Loaded COG {}".format(filename))
    client.run(TOKEN)
   ```
  * https://discordpy.readthedocs.io/en/stable/ext/commands/api.html?highlight=load_extension#discord.ext.commands.Bot.load_extension
  
## 3. Create a cog for all your poll commands
### 📚 Outcome: What are we building for this task?
    
   <img width="262" alt="Screen Shot 2022-08-18 at 11 41 38 pm" src="https://user-images.githubusercontent.com/80389972/185410733-fcaf554b-ad0f-42c4-ab50-1db2ac15dec6.png">
   
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
  ```
  class Poll(commands.Cog):
* We need a constructor to create the Cog class. This constructor can be done by using `init` method. 
* The `init` method should take the `bot` attribute to store information about our bot. 
    ```
    class Poll(commands.Cog):
        def __init__(self, bot): 
            self.bot = bot
    ```
### ✅ Task: Get inputs from users before sending back the poll
 * We need to write a function `init_poll` allowing us to create a poll command. A way for us to set the command is using decorator @commands.command(aliases=["p"]) above declaration of the `init_poll` function. This means when a user type `!p` or `!init_poll` , we will have a poll command. 
 * However, that's not enough as a user need to give a poll question, time for the poll and options for others to vote => give 3 more attributes for `init_poll` include question, time, *options. 
    ```
    class Poll(commands.Cog):
        def __init__(self, bot): 
            self.bot = bot
         @commands.command(aliases=["p"])
         async def init_poll(self, ctx, question, time, *options): 
    ```
 * You can see we also need to have `self` and `ctx`. We need `self` because it is a function declared inside the class. We need `ctx` because when user type their `!p` command, having the `ctx` attribute will allow us to have access to the `Context` object of the command. 
 * <img width="977" alt="Screen Shot 2022-08-17 at 8 14 25 pm" src="https://user-images.githubusercontent.com/80389972/185095123-422fab2b-f2b0-4aa8-be60-17b31d73e731.png">
 * Next, we need apply a condition for our poll. You can customise how many options permitted for a poll. In this tutorial, there are maximum 3 options allowed. 
    ```
    class Poll(commands.Cog):
        def __init__(self, bot): 
            self.bot = bot
         @commands.command(aliases=["p"])
         async def init_poll(self, ctx, question, time, *options): 
            if len(options) > 3:
              await ctx.send("The number of options cannot exceed the allowed limit")
            if not time.isdigit():
              await ctx.send("Time if of type number. Please provide a number.")
    ```
 * you can notice that we are making use of ctx attribute to send back a message to the server. The data type of what is returned from ctx.send(...) is discord.Message. Here is more information about discord.Message: https://discordpy.readthedocs.io/en/stable/api.html#discord.Message
### ✅ Task: Send back an Embed as a poll
 * The discord bot has to send back the message to the server through `ctx.send(embed = Embed)`. 
 * A reason why we cannot send back a string like what we previous did is because our poll have a lot of information like time, question, given options. Hence, it is gonna messy if we put all of them into a string. 
 * Instead, make use of `embed attribute`. To do that, we first need to create an Embed object as following: 
    ```
     class Poll(commands.Cog):
        def __init__(self, bot): 
            self.bot = bot
         @commands.command(aliases=["p"])
         async def init_poll(self, ctx, question, time, *options): 
            
            if len(options) > 3:
              await ctx.send("The number of options cannot exceed the allowed limit")
            if not time.isdigit():
              await ctx.send("Time if of type number. Please provide a number.")
            embed = discord.Embed(title = question, description= f'Poll will end in {time} seconds :alarm_clock:. There are {len(options)} options:')
    ```
### ✅ Task: Use emoji module to convert strings to emojis and add fields and footer
  * To generate a list of 3 emojis: 1️⃣, 2️⃣, 3️⃣ , we need to generate a list of string and convert them to emojis
    ```
    tmp = [':one:', ':two:', ':three:']
    emojis = [emoji.emojize(e, language='alias') for e in tmp]
    ```
    ```
     class Poll(commands.Cog):
        def __init__(self, bot): 
            self.bot = bot
         @commands.command(aliases=["p"])
         async def init_poll(self, ctx, question, time, *options): 
            if len(options) > 3:
              await ctx.send("The number of options cannot exceed the allowed limit")
            if not time.isdigit():
              await ctx.send("Time if of type number. Please provide a number.")
            embed = discord.Embed(title = question, description= f'Poll will end in {time} seconds :alarm_clock:. There are {len(options)} options:')
            tmp = [':one:', ':two:', ':three:']
            emojis = [emoji.emojize(e, language='alias') for e in tmp]
      ```
  * Because 1️⃣, 2️⃣, 3️⃣ are recent emojis added to the emoji package. The old ones are usually faces: 😊, ☺️, etc . Hence DO NOT FORGET         `language='alias'` to convert strings to the package. 
  * Next, we want to add option fields. Run a for loop for it: 
    ```
     for i in range(len(options)):
        emo = emojis[i]
        embed.add_field(name = emo, value = options[i], inline = True)
    ```
    ```
    class Poll(commands.Cog):
        def __init__(self, bot): 
            self.bot = bot
         @commands.command(aliases=["p"])
         async def init_poll(self, ctx, question, time, *options): 
            if len(options) > 3:
              await ctx.send("The number of options cannot exceed the allowed limit")
            if not time.isdigit():
              await ctx.send("Time if of type number. Please provide a number.")
            embed = discord.Embed(title = question, description= f'Poll will end in {time} seconds :alarm_clock:. There are {len(options)} options:')
            tmp = [':one:', ':two:', ':three:']
            emojis = [emoji.emojize(e, language='alias') for e in tmp]
            for i in range(len(options)):
                emo = emojis[i]
                embed.add_field(name = emo, value = options[i], inline = True)
     ```
  * Our poll looks much nicer if 3 choices are horizontally aligned. Hence DO NOT FORGET `inline = True`. 
  * Then, add another field for instruction: 
   ```
     class Poll(commands.Cog):
        def __init__(self, bot): 
            self.bot = bot
         @commands.command(aliases=["p"])
         async def init_poll(self, ctx, question, time, *options): 
            if len(options) > 3:
              await ctx.send("The number of options cannot exceed the allowed limit")
            if not time.isdigit():
              await ctx.send("Time if of type number. Please provide a number.")
            embed = discord.Embed(title = question, description= f'Poll will end in {time} seconds :alarm_clock:. There are {len(options)} options:')
            tmp = [':one:', ':two:', ':three:']
            emojis = [emoji.emojize(e, language='alias') for e in tmp]
            for i in range(len(options)):
                emo = emojis[i]
                embed.add_field(name = emo, value = options[i], inline = True)
            embed.add_field(name="Instructions", value="React to cast a vote", inline=False)
   ```
  * Finally, add footer by following instruction below: 
  <img width="686" alt="Screen Shot 2022-08-19 at 12 02 19 am" src="https://user-images.githubusercontent.com/80389972/185414356-f10ff468-3ed7-4a7f-8d57-f492f46b3250.png">
  
### ✅ Task: Add emojis to complete the poll and set time for users to vote
 * Add emojis for users to vote 
   ```
    for emo in emojis:
      await poll.add_reaction(emo)
    ```
 * Finally we can set the the time limit for the vote 
    ```
    await asyncio.sleep(int(time))
    ```


### ✅ Task: Outputting a bar chart to show the result of the poll
  * Import libraries
    ```
    import matplotlib.pyplot as plt
    import numpy as np
    ```
  * Tally the reactions to the poll
    ```
    totalVotes = 0
    votes = []

    #calculate the number of votes for each option
    for reaction in reactions:
      # Start at -1 to exclude the vote of the bot
      v = -1

      async for _ in reaction.users():
        v += 1

      totalVotes += v
      votes.append(v)

    # Calculates percentage of votes for each option
    percentages = [round((vote/totalVotes)* 100, 2) for vote in votes]
    ```
  * Initialise the function to create bar chart
    ```
    fig, ax = plt.subplots()
    y_pos = np.arange(len(options))
    ax.barh(y_pos, percentages, align='center')
    ax.set_yticks(y_pos, labels=options)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Votes (%)')
    ax.set_title(question)
    plt.savefig('chart.png')
    ```
  * 