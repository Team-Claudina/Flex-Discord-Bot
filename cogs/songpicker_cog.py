import random

from discord.ext import commands


class RandomSongPicker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def song_trap(self, ctx):
        with open("cogs/trapsongs.txt") as word_file:
            words = word_file.readlines()
            random_word = words[random.randint(0, len(words)-1)]
            await ctx.send(random_word)
