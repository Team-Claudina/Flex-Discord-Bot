from embeds import EmbedManager


def embed_setup():
    embed_manager = EmbedManager()
    embed_manager.build_all_static()
    return embed_manager


def main():
    embed_manager = embed_setup()
    return [embed_manager]
