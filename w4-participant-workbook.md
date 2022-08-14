<h1 align="center">[Participant's Workbook] Week 4: Memebot</h1>

> Related Pages: [DecodED 3](./README.md)

---

<h1 align="center">Making a meme bot with MongoDB and an external API</h1>
<h2>Table of Contents</h2>
<details>
<summary>Table of Contents</summary>

- [0. Host your bot on repl.it & Flask](#0-host-your-bot-on-replit-&-flask)
  - [Repl.it](#replit)
  - [Flask](#flask)
- [1. Basic knowledge](#1-basic-knowledge)
  - [API & HTTP requests](#api-&-http-requests)
  - [Database](#database)
- [2. Install necessary modules](#2-install-necessary-modules)
  - [requests](#requests)
  - [pymongo](#pymongo)
  - [schema](#schema)
- [3. Making HTTP requests to API](#3-making-http-requests-to-api)
  - [Get](#get)
- [4. Bind event listeners to command](#4-bind-event-listeners-to-command)
  - [Command recognition](#command-recognition)
- [5. Setup MongoDB account](#5-setup-mongodb-account)
  - [MongoDB Atlas](#mongodb-atlas)
  - [MongoDB URI](#mongodb-uri)
- [6. Programmatically connect application to database](#6-programmatically-connect-application-to-database)
  - [Insert](#insert)
  - [Find](#find)
  - [Delete](#delete)
- [7. Defensive programming & error handling](#7-defensive-programming-&-error-handling)
  - [404 Not Found](#404-not-found)
  - [Validation schema](#validation-schema)
  - [DB-lookup non-existent resource](#db-lookup-non-existent-resource)
  - [Error-proof delete](#error-proof-delete)

</details>

---

## 0. Host your bot on repl.it & Flask

### [Repl.it](https://replit.com/~)

-[Host discord bot using repl.it](https://www.codementor.io/@garethdwyer/building-a-discord-bot-with-python-and-repl-it-miblcwejz)

### [Flask](https://flask.palletsprojects.com/en/2.2.x/)

Using the [Flask](https://www.fullstackpython.com/flask.html) framework.
=> To create a server & keep the bot alive for a couple of hours (repl.it kills your hosted bot if not interacted with for a few hours)

- Code for deployment => creating the server

```python
# ./keep_alive.py
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
```

Adding these lines in main.py (before setting up the `TOKEN`)

```python
# ./main.py
from keep_alive import keep_alive
keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
```

## 1. Basic knowledge

> 📝 Before we dive in head-first into the world of wonderful tech, let's get to know the basics first!

- This section assumes you haved followed along at least from step 0 to 6, and has a working basic Discord bot as well as some fundamental understanding of how Discord.py works

### API & HTTP requests

  <details>
  <summary><b>❓ What are API & HTTP requests?</b></summary>

![API illustration](./mdcontent/images/API.png)

- In programming, apps need a way to communicate with each other
- The interface through which data is exchanged is called an API

![HTTP request](./mdcontent/images/HTTP%20request.png)

- Hyper-text Transfer Protocol - rules for transferring data over the internet
- URL - unique resource locator → address of a resource stored somewhere remotely over the internet

![HTTP method](./mdcontent/images/HTTP%20methods.jpeg)

> Status code commonly encountered and will be part of today's program:

- 200 - OK (everything went well!)
- 400 - bad request (URL misspelled) → think address written in Martian
- 404 - Error (specified address empty; not found) → think no one’s home or address points to non-existent house

  </details>

### Database

  <details>
  <summary><b>❓ What is a database?</b></summary>

- For database connection, we’ll use [MongoDB](https://www.mongodb.com) - it’s a free database that’s relatively simple to setup and use
- Database is where we store data; under the hood everything is stored as binary - i.e. 1 & 0
- Internally, each database has a different manner of storing data; some as entries in a table, some a bit differently
- MongoDB stores data as documents (not the MS Word type though!) - data stored as fields in an object

  </details>

## 2. Install necessary modules

### [`requests`](https://requests.readthedocs.io/en/latest)

- Library to make HTTP requests to a specified API endpoint (URL), with some optional parameters (request headers)
  ```
  pip install -U requests
  ```

### [`pymongo`](https://github.com/mongodb/mongo-python-driver)

- Driver library to maintain a connection to MongoDB, with query abilities
  ```
  pip install -U pymongo
  ```

### [`schema`](https://github.com/keleshev/schema)

- Library to validate data structure via creating & reusing schema (blueprint objects)
  ```
  pip install -U schema
  ```

> 📝 Let us know if you run into any errors during installation!

## 3. Making HTTP requests to API

### Get

- Method used to fetch a resource at a specified URL

  - Before we make this request, we need to import the installed library into our Python program

    ```python
    import requests
    ```

  - Let's make a function to make an API call

    ```python
    def get_random_memes(count):
      response = requests.get(f"{API_ROOT}{count}") # String interpolation - this will become "https://meme-api.herokuapp.com/gimme/<count>"
      json_data = json.loads(response.text)
      return json_data
    ```

    > 📝 JSON, short for JavaScript Object Notation, is a file format frequently used for sending data over the internet. As what is actually transfered over is raw text written in JSON format, we have to explicitly parse that text into JSON before we can use it.

  - To actually invoke our API call in our bot command, we simply call this function with the appropriate parameters
    ```python
    fetched_result = get_random_memes(1)
    one_random_meme = fetched_result['memes'][0]
    ```
    > 📝 Part of working with API is working with other people's code, AKA dangerous territory where we have no control over. We have no way of knowing for certain what the desired outcome will be, and the best we can do is to read through their documentation.
  - The following API can be found [here](https://github.com/D3vd/Meme_Api) - have a read through, and see if you can explain why we extract a meme object via `one_random_meme = fetched_result['memes'][0]`

  - Let's extend our API calls to also accept a subreddit name

    ```python
    def get_random_meme_from_subreddits(subReddit, count):
      response = requests.get(f"<Read through the API documentation and see if you can construct the URL here!>")
      json_data = json.loads(response.text)
      return json_data
    ```

  - And same goes to invoking this function...
    > 📝 Let us know if you need a hint!

## 4. Bind event listeners to command

### Command recognition

- Before we get started on any business logic, let's define a client event listener (i.e. user sends message in channel)

```python
@commands.command(name='new')
async def _new(ctx, *args):

  # Recognize first variation of command (i.e. ;;new)
    # Respond accordingly

  # Recognize second variation of command (i.e. ;;new 5)
    # Respond accordingly

  #...

  pass
```

- Let's define our first event listener - when a user messages `;;new`

  - `*args` takes in an arbitrary amount of parameters as a list
  - By accessing how many parameters were extracted from a user's command invocation (i.e. `len(args)`), we can differentiate which variation of the command they were using
  - We would like to respond with a single meme when the command is called without any additional parameter

  ```python
  if (len(arg) == 0):
    random_meme = get_random_memes(1)['memes'][0]
    await ctx.send(random_meme['url']) # Have bot send message to channel - i.e. "respond"
  ```

  > 📝 Host your bot, message `;;new` into the chat, and see if it works!

- A bit trickier, let's define our second event listener - when a user messages `;;new 3`

  - We would like to extract the number of memes (in this case 3, but ideally any numeric value will do!)
    - In this case, the number of passed parameters will be one (i.e. `len(args) == 1`)
    - We extract this number via the first element of the `args` list (i.e. `args[0]`)
  - And respond with the correct number of memes

  ```python
  if (len(args) > 0):
    random_memes = get_random_memes(int(args[0]))['memes']
    random_memes_image_link = [e['url'] for e in random_memes] # Destructure response to get all memes' URLs
    for link in random_memes_image_link: # Iterate over all fetched URLs & respond
      await ctx.send(link)
  ```

  > 📝 `random_memes_image_link = [e['url'] for e in random_memes]` - this particular quirky syntax is Python's list comprehension - it's a really powerful tool to quickly reshape data structure to our use case, if leveraged properly. See if you can reason about this line!

- Moving on to our third event listener - when a user messages `;;subreddit wholesomememes`

  - First, we need to rig this event listener to respond to the right command

  ```python
  @commands.command(name='subreddit')
  async def _subreddit(ctx, arg1):
    subreddit = arg1
  ```

  > 📝 Instead of passing in `*args`, we are now using `arg1`. See if you can reason about this particular change!
  > Hint - notice the intented different behaviour between our two commands

  - With the subreddit name extracted, we can now implement the functionality

  ```python
  random_meme = get_random_meme_from_subreddits(subreddit, 1)
  await ctx.send(random_meme_subreddit['url'])
  ```

  #### **💡 Challenge**

  Right now, our bot assumes the user would always want to fetch a single meme whenever they specify a subreddit name. Can you refactor the code to provide some additional flexibility - i.e. allow the user to specify how many memes to fetch <i>after</i> the subreddit name?

- We have a few event listeners left to define regarding database, but with the knowledge we have right now we can define the command recognition straight away

  - An event listener to respond to `;;save best_meme_ever` -> extract the user-defined name `best_meme_ever` for now; we'll work more on it later
  - `;;load best_meme_ever` -> extract the name `best_meme_ever`
  - `;;delete best_meme_ever` -> `best_meme_ever`
    > 📝 Hint: the name is all the way at the end of the string, so it's actually pretty similar to how we just extracted the subreddit name from our previous event listener

- Different from the rest, our `save` event listener is a bit more quirky

  - We'd like it to save a meme we replied to when calling the command `;;save name_here`
  - We need to rig this behaviour (and provide some fault tolerance while we're at it - i.e. user-friendly error message if broken)

  ```python
  @commands.command(name='save')
  async def _subreddit(ctx, arg1):
    try:
        response = await ctx.channel.fetch_message(ctx.message.reference.message_id) # this reads the message that the command-caller was responding to
        meme_url = response.content # this extracts the meme's URL from the original message
    except print(0):
        await ctx.send("You forgot to reply to a meme, or the meme you replied to wasn't saved in the right format")
        pass
  ```

  - And from there on out, we can refer to the URL of the specified meme simply via the variable `meme_url`

## 5. Setup MongoDB account

### [MongoDB Atlas](https://www.mongodb.com/atlas/database)

<details>
<summary><b>First, we need to create a MongoDB account & a test database</b></summary>

- Click on “try for free”
- Click on “build my first cluster”
- Pick a cloud provider (let's go with AWS)
- Pick the free-tier cluster that is the closest to us
- Wait 7-10 minutes for memory allocation to happen on a physical machine
- Create the database we will use today → click on “Cluster0” >> "Collections" tab >> "Add my own data"
- Give the database a name & the collection a name -> “test_discord_bot”, “memes” → Click on "Create"

</details>

### MongoDB URI

<details>
<summary><b>Now we need to provide our application with access rights</b></summary>

- Click on "Project 0" >> "Connect" >> "Go back"
- Click on “Whitelist IP address" → set the IP address that is allowed to access the database (for this example, let's make it so that everyone can access the database - 0.0.0.0)
- Create a MongoDB user with username & password to login
- Choose a connection method >> "Connect your application"
- Choose "Python" - this will generate the connection string appropriate to use for a Python application >> "version 3.6 or later" >> Copy “connection string only”
- Paste this under <code>MONGODB_URI</code> in <code>.env</code> and import it in our application

</details>

> 📝 Let us know if you run into any errors during the process!

## 6. Programmatically connect application to database

- First we need to create the connection to the database
  - We need to use MongoClient - it's an object that represents the client (us!)'s connection to the database
  - Import it in our code
  ```python
  from pymongo import MongoClient
  ```
  - Create it with the `MONGODB_URI` we saved to our `.env` earlier
  ```python
  cluster = MongoClient(MONGODB_URI)
  ```
  - With it, access the specific `DB` & `COLLECTION` we created earlier for our meme bot
  ```python
  db = cluster[DB]
  collection = db[COLLECTION]
  ```

### Insert

- Before we can insert anything into the database, we need to create a <i>document</i> - basically a Python dictionary, with the keys holding the values we'd like to save

```python
meme1 = {
  "_id": 1, # auto-generated if not provided
  "name": "Leo Dicaprio drinking",
  "url": "https://link_to_meme_img"
}
```

- Now, let's insert our new meme into the database

```python
collection.insert_one(meme1)
```

#### **💡 Challenge**

With the knowledge you know have, can you fill in the `;;save best_meme_ever` event listener we defined earlier to provide the intended functionality?

> 📝 Hint: we would like it to save a meme with the specified name to the database - it should also be saved with the previously-extracted `meme_url`

### Find

- Let's make a find query

```python
results = collection.find_one({"name": "Leo Dicaprio drinking"})
```

- Print out the result and see if it works!

#### **💡 Challenge**

With the knowledge you know have, can you fill in the `;;load best_meme_ever` event listener we defined earlier to provide the intended functionality?

> 📝 Hint: we would like it to load a meme with the specified name from the database

### Delete

- Finally, let's make a delete query

```python
collection.delete_one({"name": "Leo Dicaprio drinking"})
```

> 📝 Delete operation doesn't give a meaningful return value, which means error-proofing this type of operation is a bit more tricky - more on this later

#### **💡 Challenge**

With the knowledge you know have, can you fill in the `;;delete best_meme_ever` event listener we defined earlier to provide the intended functionality?

> 📝 Hint: we would like it to delete a meme with the specified name from the database

## 7. Defensive programming & error handling

- We don’t want anyone to see a nasty bug!
- Bury them deep under our error handler & provide a user-friendly error message instead!

### 404 Not Found

- Our API calls can resolve to an error - in this case, they will throw a `HTTPError` exception
- First, let's import this error definition into our code

```python
from requests.exceptions import HTTPError
```

- Anticipate & intercept this behaviour with a `try/catch` block

```python
try:
  response = requests.get(f"{API_ROOT}{subReddit}/{count}")
except HTTPError as error:
  return error
```

- Sometimes, the error can occur from the server-side - i.e. our API call resolves successfully, but the response is actually an error message (typically denoted by status code `404 Not Found`)
- This error oftentimes result from a malformatted URL, but it's possible that it is caused by a faulty resource (i.e. the URL to the image is still pointing to the right location, but the image is already deleted from the server)
- Let's define our own error handling function

```python
def check_link_die(link):
  try:
    response = requests.get(link)
  except:
    return False
  if(response.status_code == 404):
    return False
  return True
```

- And invoke it recursively whenever we fetch a meme until we get a verified working image

```python
random_meme = get_random_memes(1)['memes'][0]
while(check_link_die(random_meme['url']) == False):
  random_meme = get_random_memes(1)['memes'][0]
```

#### **💡 Challenge**

Locate all meme-fetching operations in our code and refactor them to guarantee we can always get a working meme

> 📝 Let us know if you need a hint!

### Validation schema

- We don't want to insert a faulty meme into our database (i.e. one with a malformatted URL)
- To enforce correct data shape (i.e. what fields it contains, what value in each field is) we define a `schema`
- First, import the necessary modules from the installed library into our program

```python
from schema import Schema, SchemaError, And, Regex
```

- Now let's define our `meme_schema`, AKA what we would like a meme object to look like

```python
meme_schema = Schema({
  "name": str,
  "url":  And(str, Regex("^(https:\/\/i.redd.it\/)\w+\.\w{3}$"))}) # URL must be a string matching the provided RegEx pattern
```

> 📝 Don’t worry about the RegEx - even we don’t fully grasp it! Basically it’s witchtalk in tech, but it is quite useful for whitelisting a certain string pattern. This RegEx pattern here matches `https://i.redd.it/abcdxyz.png` - where `abcxyz` is a variable-length alphanumeric string, and `png` is a 3-character alphanumeric string representing the file format (e.g. `png`, `jpg`)

- Finally, we will validate a meme to our `meme_schema` before posting it to our collection. If it doesn't pass validation, a `SchemaError` exception will be thrown, which we can intercept using the now-familiar syntax `try/catch` block

```python
try:
  meme_schema.validate(saved_meme)
except SchemaError as err:
  await ctx.send(err)
  return
collection.insert_one(saved_meme)
```

### DB-lookup non-existent resource

- If we try to lookup a non-existent meme from the database, the response will be empty
  - If we try to access a named property on an empty data structure, we will get a `TypeError` exception

```python
try:
  found_meme = collection.find_one({"name": lookup_name})
  await ctx.send(found_meme["url"])
except TypeError:
  await ctx.send("Meme not found in database!")
```

### Error-proof delete

<details>
<summary><b>❓ Idempotence - what is it, and what has it got to do with the DELETE operation?</b></summary>

- According to RESTful conventions & standard (rules to conform to when designing API), DELETE is IDEMPOTENT
  - This means they have no side-effect when performed twice (i.e. they aren’t supposed to be aware of whether they achieved the desired effect → whether truly deleted an existing resource, or got brushed off from the database due to referencing a non-existent resource)
  - Unfortunately, this means for work for us - we need to distinguish between a successful deletion operation & a “good try, I attempted” one

</details>

- Our solution is to perform a separate find query beforehand, to identify if the resource we are trying to delete even exists in the first place

#### **💡 Challenge**

Implement the modified, safer version of our delete command - whether or not it succeeds in deleting a resource, the user is informed accordingly afterwards

> 📝 Let us know if you need a hint!
