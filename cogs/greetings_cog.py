from discord.ext import commands


class Greeting(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Why Hello There")
