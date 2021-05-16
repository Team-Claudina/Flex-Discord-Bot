import json
import requests
import random
from discord.ext import commands


class JokeGenerator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joke(self, ctx):
        joke_list = json.loads(requests.get("https://tambalapi.herokuapp.com").text)
        joke_num = random.randint(0, len(joke_list))
        await ctx.send(joke_list[joke_num]["joke"])

    @commands.command()
    async def chuck(self, ctx):
        response = requests.get("http://api.icndb.com/jokes/random").text
        await ctx.message.send(":rofl: {}".format(json.loads(response)["value"]["joke"]))