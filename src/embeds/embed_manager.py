import discord

from src.configs import AUTHOR, URL, IMG_URL, EMBED_COLOUR, STATIC_BUILDS

print('\nEmbed URL\'s\nURL: ' + URL + '\nImg URL: ' + IMG_URL + '\n')


# Create Base Embed With discord.Embed
def create_embed_(title=None, description=None):
    embed = discord.Embed(
        title=title,
        author=AUTHOR,
        description=description,
        url=URL,
        colour=EMBED_COLOUR
    )

    embed.set_thumbnail(
        url=IMG_URL
    )

    embed.set_footer(
        text='FlexBot Limited',
        icon_url=IMG_URL
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

        for key in STATIC_BUILDS:
            self.embed_dict[key] = create_embed_(title=key, description=STATIC_BUILDS[key][0])
            self.create_statics(key=key)

    def create_statics(self, key):
        for field in STATIC_BUILDS[key][1]:
            self.embed_dict[key].add_field(
                name=field[0],
                value=field[1],
                inline=field[2]
            )
