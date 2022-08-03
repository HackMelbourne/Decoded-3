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

# Lessons
# 1. Discord bot without dynamic emojis 
#  STEP BY STEPS: 
  1. <bold>Create Main.py</bold>
    <bold>STEP 1</bold>: import all the already installed packages to your file (you will know why when we start using them). 
    <img width="627" alt="Screen Shot 2022-08-03 at 8 06 19 pm" src="https://user-images.githubusercontent.com/80389972/182582832-1443fd7a-d7da-4b57-8659-10c24505d685.png">
     
    <bold>STEP 2: </bold>create the discord bot.
      - Firstly, we need to create the bot object. You can see we make use of commands module that we imported initially to create the discord bot here. You can put other string for the command prefix, for example, command_prefix = "." instead of "$". 
<img width="627" alt="Screen Shot 2022-08-03 at 7 24 56 pm" src="https://user-images.githubusercontent.com/80389972/182574182-de000381-dddc-44f6-9734-53b5ed6c9e76.png">  
    <bold>STEP 3: </bold> create an asynchronous event listener that let us knows when our bot is ready. "The bot is ready" will print out when our bot starts running later on. You can see we are making use of 
<img width="627" alt="Screen Shot 2022-08-03 at 8 00 08 pm" src="https://user-images.githubusercontent.com/80389972/182581448-0fbab704-a3a6-4e03-981c-224d609345c3.png">
  <bold>STEP 4: </bold> Finally, loading the token that generated in the <bold>Set up discord bot</bold> section 
  to run our bot: 
  
<img width="627" alt="Screen Shot 2022-08-03 at 8 10 29 pm" src="https://user-images.githubusercontent.com/80389972/182583404-4dfece4e-fb96-4f13-9b7f-eb2569533baa.png">

      

