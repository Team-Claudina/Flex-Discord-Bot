from discord.ext import commands


class Greeting(commands.Cog):
    def __init__(self, bot, server="Flex Server"):
        super().__init__()
        self.bot = bot
        self.server = server

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send('Welcome To {server}'.format(server=self.server))

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Why Hello There")
