from discord.ext import commands


class Greeting(commands.Cog):
    def __init__(self, bot, prefix, server="Flex Server"):
        super().__init__()
        self.bot = bot
        self.PREFIX = prefix
        self.server = server

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send('Welcome To {server}'.format(server=self.server))

    @commands.command(aliases=['hi', 'hello', 'greetings'])
    async def greet_(self, ctx):
        await ctx.send('Hello there {member_nick}\nPlease type {PREFIX}help'.format(member_nick=ctx.member.nick,
                                                                                    PREFIX=self.PREFIX))
        print('Greeted {member_nick}'.format(member_nick=ctx.member.nick))
