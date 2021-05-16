import discord
from discord.ext import commands
import logging
from cogs import greetings_cog
from var import venv
from cogs import jokes_cog

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.all()

PREFIX = 'flex '
SERVER_NAME = 'Flex Server'
SECRET = venv.secret
bot = commands.Bot(command_prefix=PREFIX, description='Flex Discord Bot', help_command=None)

bot.add_cog(greetings_cog.Greeting(bot=bot, server=SERVER_NAME, prefix=PREFIX))
#bot.add_cog(JokeGenerator(bot))



@bot.event
async def on_ready():
    game = discord.Activity(type=discord.ActivityType.playing, name="To Pouli tou :D")
    await bot.change_presence(activity=game, status=discord.Status.online)
    print(f'On ready triggered and status is set. Logged in with {bot.user}')


bot.run(SECRET)
#def setup(bot):
    #bot.add_cog(JokeGenerator(bot))
