import logging

import discord
from discord.ext import commands

from cogs import Greeting, JokeGenerator, RandomSongPicker
from configs import PREFIX, SERVER, SECRET
from setup import main as setup_handler

setup_variables = setup_handler()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=PREFIX, description='Flex Discord Bot', help_command=None)

embed_manager = setup_variables[0]

bot.add_cog(Greeting(bot=bot, embed_manager=embed_manager))
bot.add_cog(JokeGenerator(bot=bot))
bot.add_cog(RandomSongPicker(bot=bot))


@bot.event
async def on_ready():
    game = discord.Activity(type=discord.ActivityType.watching, name=SERVER)
    await bot.change_presence(activity=game, status=discord.Status.online)
    print(f'On ready triggered and status is set. Logged in with {bot.user}')


bot.run(SECRET)
