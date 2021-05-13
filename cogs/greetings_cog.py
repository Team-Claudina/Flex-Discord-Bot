# Import Necessary Dependencies
from discord.ext import commands


# Create Class For Greetings
class Greeting(commands.Cog):
    # Give Definition To Self And Bring In Bot
    def __init__(self, bot, prefix, server="Flex Server"):
        super().__init__()
        self.bot = bot
        self.PREFIX = prefix
        self.server = server

    # Create Listener For Message On User Join
    @commands.Cog.listener()
    async def on_member_join(self, member):
        # TODO: Embed Welcome Message And Help Command
        await member.send('Welcome To {server}'.format(server=self.server))

    # Create Listener For Greeting Command Aliases And Responses
    @commands.command(aliases=['hi', 'hello', 'greetings'])
    async def greet_(self, ctx):
        # TODO: Print Nicely Formatted Hello Message With Multi Message Prevention
        await ctx.send('Hello there {member_nick}\nPlease type {PREFIX}help for command list.'
                       .format(member_nick=ctx.message.author.nick, PREFIX=self.PREFIX))
        print('Greeted {member_nick}'.format(member_nick=ctx.member.nick))
