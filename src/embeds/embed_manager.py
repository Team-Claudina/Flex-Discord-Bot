import discord

from configs.embed_config import AUTHOR, URL, IMG_URL, EMBED_COLOUR, STATIC_BUILDS

print('\nEmbed URL\'s\nURL: ' + URL + '\nImg URL: ' + IMG_URL + '\n')


def create_embed_(title: str = None, description: str = None) -> discord.Embed:
    """
    Creates a default discord embed to be added to

    :param (str) title: The title to be placed at the top of the standardized embed
    :param (str) description: The standardized embed description

    :return (discord.Embed) The created template embed
    """
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
