from pymongo import MongoClient
import os
from dotenv import load_dotenv
import discord
import requests
from requests.exceptions import HTTPError
import json
from schema import Schema, SchemaError, And, Regex

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
COMMAND = os.getenv('DISCORD_COMMAND_ROOT')
SUBREDDIT_COMMAND = os.getenv('DISCORD_COMMAND_SUBREDDIT')
DB_SAVE_COMMAND = os.getenv('DISCORD_COMMAND_DB_SAVE')
DB_LOAD_COMMAND = os.getenv('DISCORD_COMMAND_DB_LOAD')
DB_DELETE_COMMAND = os.getenv('DISCORD_COMMAND_DB_DELETE')
API_ROOT = os.getenv('MEME_API_ROOT')
MONGODB_URI = os.getenv('MONGODB_URI')
DB = os.getenv('DB')
COLLECTION = os.getenv('COLLECTION')
client = discord.Client()

collection = MongoClient(MONGODB_URI)[DB][COLLECTION]


def get_random_memes(count):
    try:
        response = requests.get(f"{API_ROOT}{count}")
    except HTTPError as error:
        return error
    json_data = json.loads(response.text)
    return json_data


def get_random_meme_from_subreddits(subReddit, count):
    try:
        response = requests.get(f"{API_ROOT}{subReddit}/{count}")
    except HTTPError as error:
        return error
    if(response.status_code == 404):
        return 'fail'
    json_data = json.loads(response.text)
    return json_data


def check_link_die(link):
    try:
        response = requests.get(link)
    except:
        return False
    if(response.status_code == 404):
        return False
    return True


meme_schema = Schema({
    "name": str,
    "url":  And(str, Regex("^(https:\/\/i.redd.it\/)\w+\.\w{3}$"))})


@client.event
async def on_message(message):
    if (message.content == COMMAND):
        random_meme = get_random_memes(1)['memes'][0]
        while(check_link_die(random_meme['url']) == False):
            random_meme = get_random_memes(1)['memes'][0]
        await message.channel.send(random_meme['url'])

    if(message.content.startswith(COMMAND + ' ') and len(message.content) <= len(COMMAND) + 2 and message.content[-1].isnumeric()):
        random_memes = get_random_memes(int(message.content[-1]))['memes']
        random_memes_image_link = [e['url'] for e in random_memes]
        for link in random_memes_image_link:
            if(check_link_die(link) == False):
                continue
            else:
                await message.channel.send(link)

    if(message.content.startswith(SUBREDDIT_COMMAND)):
        subreddit = message.content[len(SUBREDDIT_COMMAND)+1:]
        random_meme = get_random_meme_from_subreddits(subreddit, 1)
        try:
            if(random_meme["code"] == 400):
                await message.channel.send('Subreddit not found')
                return
        except KeyError:
            random_meme_subreddit = random_meme['memes'][0]
            while(check_link_die(random_meme_subreddit['url']) == False):
                random_meme = get_random_meme_from_subreddits(subreddit, 1)
                random_meme_subreddit = random_meme['memes'][0]
            await message.channel.send(random_meme_subreddit['url'])

    # TODO: error handling for ineligible meme to save
    if(message.content.startswith(DB_SAVE_COMMAND)):
        saved_name = message.content[len(DB_SAVE_COMMAND)+1:]
        saved_meme = {
            "name": saved_name,
            # TODO: extract previous message sent by bot & extract meme url (for now hardcode eligible url)
            "url": "https://i.redd.it/jfmjabdkj4g91.jpg",
        }
        try:
            meme_schema.validate(saved_meme)
        except SchemaError as err:
            await message.channel.send(err)
            return
        collection.insert_one(saved_meme)
        await message.channel.send("Saved to database!")

    if(message.content.startswith(DB_LOAD_COMMAND)):
        lookup_name = message.content[len(DB_LOAD_COMMAND)+1:]
        try:
            found_meme = collection.find_one({"name": lookup_name})
            await message.channel.send(found_meme["url"])
        except TypeError:
            await message.channel.send("Meme not found in database!")

    if(message.content.startswith(DB_DELETE_COMMAND)):
        lookup_name = message.content[len(DB_DELETE_COMMAND)+1:]
        try:
            found_meme = collection.find_one({"name": lookup_name})
            found_meme["url"]
        except TypeError:
            await message.channel.send("Meme not found in database!")
            return
        collection.delete_one(found_meme)
        await message.channel.send("Meme was deleted from database!")

client.run(TOKEN)
