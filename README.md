<h1 align="center">DecodED 3</h1>

> 👋 Hello and welcome to the third workshop of Decoded 3. In this workshop, we will make a poll command. 
<h2>Table of Contents</h2>
<details>
<summary>Table of Contents</summary>

- [0. Create a Discord Account and Discord Server](#0-create-a-discord-account-and-discord-server)
  - [Create a Discord Account](#create-a-discord-account)
  - [Create a Discord Server](#create-a-discord-server)
- [1. Create an Application](#1-create-an-application)
- [2. Installing Modules:](#2-installing-modules)
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

## 2. Installing modules: 
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
* Install these following modules with the same command: os, selenium, emoji, asyncio, matplotlib, numpy
* Let us know if you run into any errors during installation!
## 3. Web Automation using Selenium

### Selenium 
<details>
<summary><b>❓Why do we need to do web automation for this tutorial?</b></summary>
  Image a user wants to make a poll by typing this command on the already set up discord server - $p "what is your most favourite food?" 10 pasta pizza burger with 10 is the time limit for the poll. The discord bot will create a poll and it needs to generate emojis 1️⃣ 2️⃣ 3️⃣ for members to react to vote. However, fixed generated emojis like 1️⃣ 2️⃣ 3️⃣ look too boring and they do not always suit the context; in this case, we are asking for food, so our poll will look much more appealing with those 3 emojis 🍝 🍕 🍔. When we change the poll question, our bot should return emojis dynamically based on the context. For example, "which animal do you like most?" monkey cat tiger--> 🐒 🐈 🐅 should be returned. 
  SELENIUM WILL HELP US FETCH EMOJIS AUTOMATICALLY + DYNAMICALLY 
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
