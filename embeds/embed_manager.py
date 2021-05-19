import os

import discord

from configs import embed_config, general_config

author = os.getenv('AUTHOR')
url = general_config.url
img_url = general_config.img_url

print('\nEmbed URL\'s\nURL: ' + url + '\nImg URL: ' + img_url + '\n')


# Create Base Embed With discord.Embed
def create_embed_(title=None, description=None):
    embed = discord.Embed(
        title=title,
        author=author,
        description=description,
        url=url,
        colour=general_config.embed_colour
    )

    embed.set_thumbnail(
        url=img_url
    )

    embed.set_footer(
        text='FlexBot Limited',
        icon_url=img_url
    )

    # return template embed
    return embed


class EmbedManager:
    def __init__(self):
        self.embed = None
        # Create a static embed dict for load management
        self.embed_dict = {}

    def build_all_static(self):
        # Built loop that uses values from config static builds as inputs

        for key in embed_config.static_builds:
            self.embed_dict[key] = create_embed_(title=key, description=embed_config.static_builds[key][0])
            self.create_statics(key=key)

    def create_statics(self, key):
        for field in embed_config.static_builds[key][1]:
            self.embed_dict[key].add_field(
                name=field[0],
                value=field[1],
                inline=field[2]
            )
