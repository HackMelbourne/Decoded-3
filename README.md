# discord-bot-poll-system
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

# Lesson
1. <bold>Discord bot without dynamic emojis</bold>
- <bold>Goal: </bold>
- <bold>Sections: </bold>
  # # 1. <bold>Create Main.py</bold>
# # # STEP 1: import all the installed packages to your file.
<img width="647" alt="Screen Shot 2022-08-03 at 5 06 30 pm" src="https://user-images.githubusercontent.com/80389972/182545997-e7aa4204-575d-4f84-b89b-87cfdb232aeb.png">

