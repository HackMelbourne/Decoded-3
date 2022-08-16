# discord-bot-poll-system
<h1 align="center">[Participant's Workbook] Create polling using Discord.py</h1>
---

<h2>Table of Contents</h2>
<details>
<summary>Table of Contents</summary>

- [0. Create a Discord Account and Discord Server](#0-create-a-discord-account-and-discord-server)
    - [✅ Task: Create a Discord Account](#-task-create-a-discord-account)
    - [✅ Task: Create a Discord Server](#-task-create-a-discord-server)
- [1. Create an your Bot and Add it to your Server](#1-create-an-your-bot-and-add-it-to-your-server)
    - [✅ Task: Create a Discord Application and Bot, and copy your Token](#-task-create-a-discord-application-and-bot-and-copy-your-token)
    - [✅ Task: Invite your bot to your server](#-task-invite-your-bot-to-your-server)
- [2. Installing Modules: `discord.py` and `python-dotenv`](#2-installing-modules-discordpy-and-python-dotenv)
    - [✅ Task: Install `discord.py`](#-task-install-discordpy)
    - [✅ Task: Install `python-dotenv`](#-task-install-python-dotenv)
- [3. Creating a Bot and Adding it to your server](#3-creating-a-bot-and-adding-it-to-your-server)
    - [✅ Task: Create 2 files: `main.py` and `.env`](#-task-create-2-files-mainpy-and-env)
    - [Environment Variables](#environment-variables)
- [4. Basic Bot](#4-basic-bot)
    - [✅ Task: Bringing the bot to life](#-task-bringing-the-bot-to-life)
    - [Events and Callbacks](#events-and-callbacks)
    - [✅ Task: "Hello, World!"](#-task-hello-world)
    - [💡 Challenge: `Client` attributes](#-challenge-client-attributes)
    - [Receiving Messages](#receiving-messages)
    - [Sending Messages](#sending-messages)
    - [✅ Task: Respond to "!hello" with "Hello, {username}"](#-task-respond-to-hello-with-hello-username)
- [5. Cogs](#5-cogs)
    - [✅ Task: Refactor `main.py` to support Cogs (part 1)](#-task-refactor-mainpy-to-support-cogs-part-1)
    - [✅ Task: Create a Hello Cog](#-task-create-a-hello-cog)
    - [✅ Task: Refactor `main.py` to support Cogs (part 2)](#-task-refactor-mainpy-to-support-cogs-part-2)
- [6. ✅ Task: Create a Cog for all your 'Goodbye' commands](#6--task-create-a-cog-for-all-your-goodbye-commands)
- [7. [💡 Extension] Host your bot on Heroku](#7--extension-host-your-bot-on-heroku)
- [Related Links:](#related-links)

</details>

---
This is the discord bot built by using discord.py library and Selenium package to automate web browser interaction with Python. I also used Math plot library to visualize the voting results as a output. 
What's special about this application is that when a poll maker creates a question and gives suggestions for other members to vote on the discord channel: there will be web site running automatically to search for corresponding emojis from this API: https://emojipedia.org and provide them to the bot. Hence, members can vote by the emoji. After a specific limit of time, the discord bot will close the poll and return the result. 
# Example output: ![Screen Shot 2022-07-26 at 10 49 36 pm](https://user-images.githubusercontent.com/80389972/181009956-22d248ef-0a0a-49d9-859c-c146bacd66b1.png)
CLICK TO THIS LINK TO SEE THE VIDEO: https://www.youtube.com/watch?v=mFfwhWzvYGI
# Set up discord bot
0. Create an empty folder to store your code
1. Sign in developer account: https://discord.com/developers/applications
2. Create new application in the developer dashboard
![Create Application](images/create-application.png)
3. Name your application
![Name Application form](images/name-application.png)
4. Add a bot to the discord application
![Add Bot](images/add-bot-1.png)
5. Generate token for the bot, save the token in a `.env` file within your code folder
![Generate Token](images/token-1.png)
6. Generate url to invite the bot to your server and copy it
![Generate URL](images/url-1.png)
7. Open the link in your browser to authorize the bot to join your server
![Join Server](images/authorize-1.png)
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
