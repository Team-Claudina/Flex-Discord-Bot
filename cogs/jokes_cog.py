import json
import requests
from discord.ext import commands


class JokeGenerator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joke(self, ctx):
        response = json.loads(requests.get("https://tambalapi.herokuapp.com").json())
        await ctx.message.send(response[0]["joke"])

    @commands.command()
    async def chuck(self, ctx):
        response = requests.get("http://api.icndb.com/jokes/random").text
        await ctx.message.send(":rofl: {}".format(json.loads(response)["value"]["joke"]))
