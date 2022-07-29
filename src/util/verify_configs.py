# TODO: Create system to verify validity of configs

import configs
import requests
import validators
import re
import src.log as log

class VerifyConfigs:
	def __init__(self, exclude: list = [""]):
		"""
		Returns an object that verifies each of the items in the config file

		To exclude certain checks pass the names of the configs in a list

		:param (list) exclude: List of items to exclude from being checked

		:return (bool) Wether or not the bot should be allowed to start up or not.
		"""
		self.validated = True
		self.exclude = exclude
		self.logger = log.fetch_logger()
		self.check_alpha = re.compile('^([a-z]\s)*$', re.IGNORECASE)

		self.verify()

	def verify(self):
		"""
		Runs the verifications

		:return (None)
		"""
		if "BOT_NAME" not in self.exclude:
			self.verify_name()
		if "URL" not in self.exclude:
			self.verify_url()
		if "IMG_URL" not in self.exclude:
			self.verify_image()
		if "PREFIX" not in self.exclude:
			self.verify_prefix()
		if "SERVER" not in self.exclude:
			self.verify_server()
		if "SECRET" not in self.exclude:
			self.verify_secret()

	def verify_name(self) -> bool:
		"""
		Verifies the name in configs.BOT_NAME

		:return (bool) Whether the name was successfully validated or not
		"""
		if not self.check_alpha(configs.BOT_NAME):
			self.logger.critical("Failed to validate BOT_NAME") 
			self.validated = False
			return False
		
		self.logger.log("Successfully validated BOT_NAME")
		return True

	def verify_url(self) -> bool:
		"""
		Verifies the URL in configs.URL

		:return (bool) Whether the url was successfully validated or not
		"""
		if not validators.url(configs.URL):
			self.logger.critical("Failed to validate URL: URL entered is not a valid URL")
			return False

		page_request = requests.get(configs.URL, allow_redirects=True)
		if page_request.status_code != 200:
			self.logger.critical("Failed to validate URL: Could not find page URL")
			return False
		
		self.logger.log("Successfully validated URL")
		return True

	def verify_image(self) -> bool:
		"""
		Verifies the image URL in configs.URL_IMG

		:return (bool) Whether the image url was successfully validated or not
		"""
		def set_image_to_default():
			configs.IMG_URL = 'https://i.imgur.com/3qfzFxX.png'

		configs.IMG_URL.removesuffix('/')
		file_type = configs.IMG_URL.split('.')[-1]

		if file_type not in configs.SUPPORTED_IMG_TYPES:
			self.logger.critical("Image File type not supported, reverting to default")
			set_image_to_default()
			return False

		file_request = requests.get(configs.IMG_URL, allow_redirects=True)
		if file_request.status_code != 200:
			self.logger.critical("Could not find image on the web, reverting to default")
			set_image_to_default()
			return False

		self.logger.log("Successfully validated IMG_URL")
		return True

	def verify_prefix(self) -> bool:
		if configs.PREFIX == "":
			self.logger.error("PREFIX Error please check")
			self.validated = False
			return False
		
		self.logger.debug("Successfully validated PREFIX")
		return True
	
	def verify_server(self) -> bool:
		"""
		Verifies the server name in configs.SERVER

		:return (bool) Whether the server name was successfully validated or not
		"""

		if not self.check_alpha(configs.SERVER):
			self.logger.critical("Failed to validate SERVER") 
			self.validated = False
			return False
		
		self.logger.log("Successfully validated SERVER")
		return True

	def verify_secret(self) -> bool:
		"""
		Verifies the server secret in configs.SECRET

		:return (bool) Whether the secret was successfully validated or not
		"""
		if len(configs.SECRET) != 70:
			self.logger.critical("SECRET error: Secret is not 70 characters long")
			return False
		
		self.logger.log("Successfully validated SECRET")
		return True
	