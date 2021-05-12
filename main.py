import discord
from discord.ext import commands
import logging
import cogs

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

PREFIX = '.'
SERVER_NAME = 'Flex Server'
bot = commands.Bot(command_prefix=PREFIX, description='Flex Discord Bot', help_command=None)

bot.add_cog(cogs.greetings_cog.Greeting(bot=bot, server=SERVER_NAME))


@bot.event
async def on_ready():
    game = discord.Activity(type=discord.ActivityType.playing, name="FlexBot")
    await bot.change_presence(activity=game, status=discord.Status.idle)
    print(f'On ready triggered and status is set. Logged in with {bot.user}')


bot.run('secret')
