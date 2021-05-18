import os


def env_setup():
    try:
        with open('.env') as env_file:
            env_lines = env_file.readlines()
            for line in env_lines:
                try:
                    env_comp = line.split(' = ')
                    os.environ[env_comp[0]] = env_comp[1]
                finally:
                    print(line + ' Wrote')

            print('Successfully wrote ENV')
    finally:
        print('ENV Setup Completed')


def main():
    env_setup()
