import discord
from discord.ext import commands
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

prefix = '.'
bot = commands.Bot(command_prefix=prefix, description='Flex Discord Bot', help_command=None)


@bot.event
async def on_ready():
    game = discord.Activity(type=discord.ActivityType.watching, name="FlexBot")
    await bot.change_presence(activity=game, status=discord.Status.idle)
    print(f'On ready triggered and status is set. Logged in with {bot.user}')


bot.run('secret')
