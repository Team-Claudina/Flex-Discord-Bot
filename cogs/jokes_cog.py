
import requests, discord, json
from discord.ext import commands


class JokeGenerator:

    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def joke(self, ctx):
        response = json.loads(requests.get("https://tambalapi.herokuapp.com").text)
        await ctx.message.edit(content=":rofl: {}".format(response[0]["joke"]))


    @commands.command(pass_context=True)
    async def chuck(self, ctx):
        response = requests.get("http://api.icndb.com/jokes/random").text
        await ctx.message.edit(content=":rofl: {}".format(json.loads(response)["value"]["joke"]))


def setup(bot):
    bot.add_cog(JokeGenerator(bot))
