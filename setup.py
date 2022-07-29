from src.embeds import EmbedManager
from src.log import setup_logger

def embed_setup() -> EmbedManager:
	"""
	Creates main embed manager then builds all static embeds
	
	:return (EmbedManager) Instance of embed manager
	"""
	embed_manager = EmbedManager()
	embed_manager.build_all_static()
	return embed_manager

def log_setup():
	"""
	Sets up main logger with name 'discord'

	:return (None)
	"""
	setup_logger(log_level="DEBUG", logfile="logs/main_bot_log.log", logger_name="discord")
