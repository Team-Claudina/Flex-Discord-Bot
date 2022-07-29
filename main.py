import discord
from discord.ext import commands

from src.cogs import Greeting, JokeGenerator, RandomSongPicker
from src.configs import PREFIX, SERVER, SECRET
from src.log import fetch_logger
from setup import embed_setup, setup_logger

setup_logger()
embed_manager = embed_setup()

logger = fetch_logger('discord')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=PREFIX, description='Flex Discord Bot', help_command=None)

bot.add_cog(Greeting(bot=bot, embed_manager=embed_manager))
bot.add_cog(JokeGenerator(bot=bot))
bot.add_cog(RandomSongPicker(bot=bot))


@bot.event
async def on_ready():
    game = discord.Activity(type=discord.ActivityType.watching, name=SERVER)
    await bot.change_presence(activity=game, status=discord.Status.online)
    logger.log(f'On ready triggered and status is set. Logged in with {bot.user}')


bot.run(SECRET)
