<h1 align="center">[Participant's Workbook] Building a Music Bot</h1>

> Related Pages: [DecodED 3](./README.md)

---

<h2>Table of Contents</h2>
<details>
<summary>Table of Contents</summary>

- [0. Downloading ffmpeg](#0-create-a-discord-account-and-discord-server)
    - [For Windows](#create-a-discord-account)
    - [For Mac](#create-a-discord-server)
- [1. Installing Modules: `youtube_dl`](#1-create-an-application)
- [2. Setting up the join and leave commands](#2-installing-modules-discordpy-and-python-dotenv)
- [3. Streaming audio to discord](#3-creating-a-bot-and-adding-it-to-your-server)
- [4. Pausing and playing audio](#4-make-the-bot-say-hello-world)
- [5. Sending the Youtube Thumbnail](#5-adding-commands)

</details>

---

## 0. Downloading ffmpeg

<details>
<summary><b>❓ What is ffmpeg?</b></summary>
FFmpeg is a free and open-source software project consisting of a suite of libraries and programs for handling video, audio, and other multimedia files and streams. At its core is the command-line ffmpeg tool itself, designed for processing of video and audio files.


</details>

* We need to download ffmpeg first so that we can stream music.

### For Windows

Simply click on this link and ffmpeg will start
downloading (https://www.gyan.dev/ffmpeg/builds/packages/ffmpeg-2022-07-24-git-39a538f430-full_build.7z)

### For Mac

Simply click on this link and ffmpeg will start downloading (https://evermeet.cx/ffmpeg/ffmpeg-107536-g8daa0fea9f.zip)

## 1. Un-ziping and copying the ffmpeg.exe path

Un-zip the ffmpeg and than open the folder, open bin, from there copy the path of ffmpeg.exe which we will use while
adding ffmpeg.

## 1. Installing Modules: 'youtube_dl'

* Before we begin creating the bot, we have to install a few modules
* Install `youtube_dl`
    * youtube_dl is an open source download manager for youtube video and it will help us play our youtube videos audio
      in real time.
    * to install it, type this into your terminal:
      ```
      pip install youtube_dl
      ```
     * now you need to add some youtube_dl option in your code 
       ```python
       # youtube best audio options
       yt_dl_opts = {'formats': 'beastaudio/best'}
       ytdl = youtube_dl.YoutubeDL(yt_dl_opts)
       ```
## 2. Setting up the join and leave commands

* We first need to make a client varible. It will help us intaract with the discord api.
  ```python 
  client = commands.Bot(command_prefix='?')
  ``` 
 
* We now need to make sure that when ever we run the code, we can see that our bot has successfully logged-in. For that we need to write a function on_ready.
  ```python
  # Start the bot
    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

  ```

## 3. Creating a Bot and Adding it to your server

### Environment Variables

<details>
<summary><b>❓ What are environment variables?</b></summary>

When a program is run, it may need information from the operating system to configure its behaviour. This might include
the operating system, current running folder, or more important things like passwords to various services (Discord
here!). Basically, environment variables are variables/information about the environment its running on. They are a
useful tool in providing information to your program, which is separate from your code. Developers commonly use `.env`
files to specify these variables.

</details>

* `.env` have several advantages:

1. They help different developers to keep their passwords separate from each other.
1. When using a VCS (GitHub), you can prevent your `.env` file from being uploaded to the internet, thus protecting all
   of your passwords.

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

Can you try defining your own environment variable (besides `TOKEN`), and printing it to the console? How about printing
the current operating system using only environment variables? (Will need some googling!)

Now that we have the token for our bot, let's add it to our server. Do do this, we will use the
official [Discord Applications Page.](https://discord.com/developers/applications)

## 4. Make the Bot say "Hello, World!"

* TODO Slides/Explanation: what are decorators?
* TODO Slides/Explanation: what are events and callbacks - what is async and await (extension)
  ```python
  # 

  ```
* ✅

<details>
<summary><b>❓ What are events?</b></summary>

Events are exactly as you would think, stuff that happens that we want to know about. Examples would be someone joining
a server, sending a message, or reacting to something.

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

Often in coding, you will need to perform a task, and wait for the response before you can do anything. An example would
be Gmail, the website needs to wait for the mail to send, before telling you it's sent.
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

In the context of discord.py, we can use `async` on our functions to tell discord.py it's going to do a long-running
task, and `await` to do that task:

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
