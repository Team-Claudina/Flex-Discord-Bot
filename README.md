<h1 align="center">
	Flex Bot
</h1>

<h5 align="center">
	Small, Clean and Modular
</h5>

<p align="center">
	<a href="https://discord.gg/PtW4HD857Z">
		<img src="https://discordapp.com/api/guilds/368253457129537547/widget.png?style=shield" alt="Discord Server">
	</a>
	<a href="http://makeapullrequest.com">
		<img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg">
	</a>
	<a href="https://github.com/psf/black">
		<img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code Style: Black">
	</a>
</p>

# Overview

Flex bot is designed to be a highly modular single server discord bot.

We decided to ditch the single bot huge functionality design and instead 
to make a bot that is easily modifiable to fit a specific task on a 
single server.

The reason for this is more style than anything else though reliability
and error handling do play a significant role here too.

## Philosophy

Today on most discord servers we see discord bots designed to do everything.
They manage roll's, watch messages, play music, manage embeds etc.

This for some servers is fine, though I've always found such bots hard to
manage and maintain.

The way Flex Bot differs is that it's designed to be highly modular and
easy to clone. The main reason for this is so that each instance of it
can have a specific purpose and can be run easily in a docker image.

Thus if something goes wrong, or a specific one needs maintenance
that single bot can be taken offline and repaired or changed without
bringing the whole servers functionality offline.

## Getting Started

For now run either the `configure.sh` or `configure.bat` files depending
on your system.

This will create the required config files in `./configs`.

Modify these as needed then proceed to just run `main.py` using the
python.exe found in `./.venv/Scripts/`
