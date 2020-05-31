# bot.py
import os
import random
import discord
import json
import urllib.request
import requests

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GIPHY_API_KEY = os.getenv('GIPHY_API_KEY')

bot = commands.Bot(command_prefix='=')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name="commands", help="Lists out all commands")
async def commands(ctx):
    command_help = "Available commands : b99, joke, gif, yomama. \n For command help, use '=help <command_name>'"
    await ctx.send(command_help)

@bot.command(name="b99", help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!', 'cool cool cool cool cool cool', 'Noice', 'Toit', 'Nine Nine',
        'indeed indeed indeed indeed'
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name="gif")
async def giphy(ctx, search):

    e = discord.Embed()
    search = search.replace(' ', '+')
    api = "http://api.giphy.com/v1/gifs/search?q=" + search + "&api_key=" + GIPHY_API_KEY + "&limit=5"
    data=json.loads(urllib.request.urlopen(api).read())
    _url=data['data'][0]['images']['original']['url']
    print(_url)
    e.set_image(url=_url)

    await ctx.send(embed=e)

@bot.command(name="yomama")
async def yomama(ctx):
    req = requests.get('https://api.yomomma.info/')
    data = req.json()
    await ctx.send(data['joke'])

@bot.command(name="joke", help="Responds with a random dark joke")
async def joke(ctx):
    req = requests.get('https://sv443.net/jokeapi/v2/joke/Dark?type=twopart')
    data = req.json()
    joke = data['setup'] + " \n" + data['delivery']
    await ctx.send(joke)


bot.run(TOKEN)