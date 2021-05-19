import os
from embeds import EmbedManager


def env_setup():
    try:
        with open('.env') as env_file:
            env_lines = env_file.readlines()
            for line in env_lines:
                env_comp = line.split(' = ')
                if env_comp[0] != 'SECRET':
                    env_comp[1] = env_comp[1][1:-2]

                os.environ[env_comp[0]] = env_comp[1]
                print('Wrote ' + env_comp[1])

            print('Successfully wrote ENV\n')
    finally:
        print('ENV Setup Completed\n')


def embed_setup():
    embed_manager = EmbedManager()
    embed_manager.build_all_static()
    return embed_manager


def main():
    env_setup()
    embed_manager = embed_setup()
    return [embed_manager]
