import json
import os

import requests
from discord.ext import commands
from dotenv import load_dotenv
from pymongo import MongoClient
from requests.exceptions import HTTPError
from schema import Schema, SchemaError, And, Regex

load_dotenv()

TOKEN = os.getenv('TOKEN')
COMMAND = os.getenv('DISCORD_COMMAND_ROOT')
BOTNAME = os.getenv('BOT_NAME')
API_ROOT = os.getenv('MEME_API_ROOT')
MONGODB_URI = os.getenv('MONGODB_URI')
DB = os.getenv('DB')
COLLECTION = os.getenv('COLLECTION')

collection = MongoClient(MONGODB_URI)[DB][COLLECTION]


# all commands that this bot will respond to will begin with ";;bot_name"
# bot = commands.Bot(command_prefix=COMMAND + BOTNAME, strip_after_prefix=True, intents=discord.Intents.all())

def get_random_memes(count):
    try:
        response = requests.get(f"{API_ROOT}{count}")
    except HTTPError as error:
        raise error
    json_data = json.loads(response.text)
    return json_data


def get_random_meme_from_subreddits(subReddit, count):
    try:
        response = requests.get(f"{API_ROOT}{subReddit}/{count}")
    except HTTPError as error:
        raise error
    if (response.status_code == 404 or response.status_code == 400):
        raise HTTPError(response.text)
    json_data = json.loads(response.text)
    return json_data


def check_link_die(link):
    try:
        response = requests.get(link)
    except:
        return False
    if (response.status_code == 404):
        return False
    return True


meme_schema = Schema({
    "name": str,
    "url": And(str, Regex("^(https:\/\/i.redd.it\/)\w+\.\w{3}$"))})


class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx, *args):
        # ;;random
        if (len(args) == 0):
            random_meme = get_random_memes(1)['memes'][0]
            while (check_link_die(random_meme['url']) == False):
                random_meme = get_random_memes(1)['memes'][0]
            await ctx.send(random_meme['url'])

        # ;;random 5
        if (len(args) > 0):
            try:
                random_memes = get_random_memes(int(args[0]))['memes']
            except:
                await ctx.send("Unrecognized command. Pretty sure that wasn't a number :)")
                pass
            random_memes_image_link = [e['url'] for e in random_memes]
            for link in random_memes_image_link:
                if (check_link_die(link) == False):
                    continue
                else:
                    await ctx.send(link)
        pass

    @commands.command()
    async def meme_subreddit(self, ctx, arg1):
        subreddit = arg1
        try:
            random_meme = get_random_meme_from_subreddits(subreddit, 1)
            random_meme_subreddit = random_meme['memes'][0]
            while (check_link_die(random_meme_subreddit['url']) == False):
                random_meme = get_random_meme_from_subreddits(subreddit, 1)
                random_meme_subreddit = random_meme['memes'][0]
            await ctx.send(random_meme_subreddit['url'])
        except HTTPError as err:
            await ctx.send('Subreddit not found')
            pass
        pass

    @commands.command()
    async def save_meme(self, ctx, arg1):
        try:
            response = await ctx.channel.fetch_message(ctx.message.reference.message_id)
            meme_url = response.content
        except print(0):
            await ctx.send("You forgot to reply to a meme, or the meme you replied to wasn't saved in the right format")
            pass
        saved_name = arg1
        saved_meme = {
            "name": saved_name,
            "url": meme_url,
        }
        try:
            meme_schema.validate(saved_meme)
        except SchemaError as err:
            await ctx.send(err)
            pass
        collection.insert_one(saved_meme)
        await ctx.send("Saved to database!")
        pass

    @commands.command()
    async def load_meme(self, ctx, arg1):
        lookup_name = arg1
        try:
            found_meme = collection.find_one({"name": lookup_name})
            await ctx.send(found_meme["url"])
        except TypeError:
            await ctx.send("Meme not found in database!")
            pass
        pass

    @commands.command()
    async def delete_meme(self, ctx, arg1):
        lookup_name = arg1
        try:
            found_meme = collection.find_one({"name": lookup_name})
        except TypeError:
            await ctx.send("Meme not found in database!")
            pass
        collection.delete_one(found_meme)
        await ctx.send("Meme was deleted from database!")
        pass


async def setup(bot):
    await bot.add_cog(Meme(bot))
